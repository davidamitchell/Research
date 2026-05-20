import { create, insertMultiple, search as oramaSearch } from '@orama/orama';
import { pipeline } from '@xenova/transformers';

let state = {
  ready: false,
  db: null,
  embedder: null,
  modelConfig: null,
};

function post(type, payload = {}) {
  self.postMessage({ type, ...payload });
}

function toVectorArray(output) {
  if (!output) return [];
  if (Array.isArray(output)) return output;
  if (output.data) return Array.from(output.data);
  return [];
}

async function initEngine(indexUrl) {
  if (state.ready) {
    post('ready');
    return;
  }

  post('status', { message: 'Loading search index…' });
  const response = await fetch(indexUrl);
  if (!response.ok) {
    throw new Error(`Failed to fetch index: ${response.status}`);
  }
  const payload = await response.json();
  const items = payload?.items ?? [];
  const vectors = payload?.vectors ?? [];
  const modelConfig = payload?.model ?? {};
  const dimension = Number(modelConfig.dimension ?? 0);

  if (!items.length || items.length !== vectors.length || dimension <= 0) {
    throw new Error('Invalid vector index payload.');
  }

  post('status', { message: 'Building vector database…' });
  const schema = {
    id: 'string',
    slug: 'string',
    title: 'string',
    full_title: 'string',
    added: 'string',
    question_excerpt: 'string',
    findings_excerpt: 'string',
    url: 'string',
    tags: 'string[]',
    thread_slugs: 'string[]',
    embedding: `vector[${dimension}]`,
  };

  const docs = items.map((item, idx) => ({
    ...item,
    embedding: vectors[idx],
  }));

  const db = await create({ schema });
  await insertMultiple(db, docs);

  post('status', { message: 'Loading browser model…' });
  const embedder = await pipeline(
    'feature-extraction',
    String(modelConfig.browser_model_id || 'Xenova/all-MiniLM-L6-v2'),
  );

  state = {
    ready: true,
    db,
    embedder,
    modelConfig,
  };
  post('ready');
}

async function runSearch(query, limit, requestId) {
  if (!state.ready || !state.db || !state.embedder) {
    post('error', { message: 'Search engine is not initialized.', requestId });
    return;
  }

  const trimmed = query.trim();
  if (!trimmed) {
    post('results', { results: [], requestId });
    return;
  }

  const output = await state.embedder(trimmed, {
    pooling: String(state.modelConfig?.pooling || 'mean'),
    normalize: Boolean(state.modelConfig?.normalize ?? true),
  });
  const vector = toVectorArray(output);

  if (!vector.length) {
    post('error', { message: 'Failed to embed query.', requestId });
    return;
  }

  const result = await oramaSearch(state.db, {
    mode: 'vector',
    vector: {
      property: 'embedding',
      value: vector,
    },
    limit,
  });

  const rows = (result?.hits ?? []).map((hit) => ({
    ...(hit.document || {}),
    score: hit.score ?? 0,
  }));
  post('results', { results: rows, requestId });
}

self.onmessage = async (event) => {
  const { type } = event.data || {};

  try {
    if (type === 'init') {
      await initEngine(event.data.indexUrl);
      return;
    }

    if (type === 'search') {
      await runSearch(
        String(event.data.query || ''),
        Number(event.data.limit || 20),
        Number(event.data.requestId || 0),
      );
    }
  } catch (error) {
    post('error', {
      message: error instanceof Error ? error.message : 'Search worker failure.',
      requestId: Number(event.data?.requestId || 0),
    });
  }
};
