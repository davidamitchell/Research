function escapeHtml(value) {
  return String(value || '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

function debounce(fn, waitMs) {
  let timer = null;
  return (...args) => {
    if (timer) clearTimeout(timer);
    timer = setTimeout(() => fn(...args), waitMs);
  };
}

class VectorSearchController {
  constructor({
    mode,
    inputId,
    resultsId,
    statusId,
    limit,
  }) {
    this.mode = mode;
    this.input = document.getElementById(inputId);
    this.resultsEl = document.getElementById(resultsId);
    this.statusEl = document.getElementById(statusId);
    this.limit = limit;
    this.ready = false;
    this.booting = false;
    this.requestId = 0;
    this.worker = null;

    if (!this.input || !this.resultsEl) return;

    this.input.addEventListener('focus', () => this.ensureReady());
    this.input.addEventListener(
      'input',
      debounce(() => {
        this.ensureReady();
        this.search();
      }, 120),
    );

    if (this.mode === 'full') {
      const params = new URLSearchParams(window.location.search);
      const initial = params.get('q') || '';
      this.input.value = initial;
      if (initial) {
        this.ensureReady();
      }
    }
  }

  setStatus(message) {
    if (this.statusEl) {
      this.statusEl.textContent = message || '';
    }
  }

  ensureReady() {
    if (this.ready || this.booting || !this.input) return;
    this.booting = true;
    this.setStatus('Initializing semantic search…');

    this.worker = new Worker('/Research/assets/search-worker.js', { type: 'module' });
    this.worker.onmessage = (event) => {
      const { type } = event.data || {};

      if (type === 'status') {
        this.setStatus(event.data.message || 'Initializing search…');
        return;
      }

      if (type === 'ready') {
        this.ready = true;
        this.booting = false;
        this.setStatus('');
        if (this.input?.value.trim()) this.search();
        return;
      }

      if (type === 'results') {
        if (Number(event.data.requestId) !== this.requestId) return;
        this.renderResults(event.data.results || []);
        return;
      }

      if (type === 'error') {
        if (event.data.requestId && Number(event.data.requestId) !== this.requestId) return;
        this.booting = false;
        this.setStatus(event.data.message || 'Search failed to initialize.');
      }
    };

    this.worker.postMessage({ type: 'init', indexUrl: '/Research/search-index.json' });
  }

  search() {
    if (!this.worker || !this.input) return;

    const query = this.input.value.trim();
    if (!query) {
      this.renderResults([]);
      if (this.mode === 'full') this.setStatus('');
      return;
    }

    if (!this.ready) {
      this.setStatus('Initializing semantic search…');
      return;
    }

    this.requestId += 1;
    this.setStatus('Searching…');
    this.worker.postMessage({
      type: 'search',
      query,
      limit: this.limit,
      requestId: this.requestId,
    });

    if (this.mode === 'full') {
      const params = new URLSearchParams();
      params.set('q', query);
      history.replaceState(null, '', `${window.location.pathname}?${params.toString()}`);
    }
  }

  renderResults(results) {
    const query = this.input?.value.trim() || '';

    if (this.mode === 'landing') {
      if (!query || !results.length) {
        this.resultsEl.style.display = 'none';
        this.resultsEl.innerHTML = '';
        this.setStatus('');
        return;
      }

      const rows = results.map((item) => {
        const url = item.url || `/Research/research/${item.slug}.html`;
        return `<a class="search-preview-item" href="${escapeHtml(url)}"><span>${escapeHtml(item.title)}</span><span class="search-preview-date">${escapeHtml(item.added)}</span></a>`;
      });
      rows.push(
        `<a class="search-see-all" href="/Research/search.html?q=${encodeURIComponent(query)}">see all results →</a>`,
      );
      this.resultsEl.innerHTML = rows.join('');
      this.resultsEl.style.display = 'block';
      this.setStatus('');
      return;
    }

    const cards = results.map((item) => {
      const tags = (item.tags || [])
        .map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`)
        .join('');
      const excerpt = item.findings_excerpt || item.question_excerpt || '';
      const url = item.url || `/Research/research/${item.slug}.html`;
      return `<a class="card" href="${escapeHtml(url)}"><div class="card-title">${escapeHtml(item.title)}</div><div class="card-meta">${escapeHtml(item.added)}</div><div class="card-tags">${tags}</div><div class="card-excerpt">${escapeHtml(excerpt)}</div></a>`;
    });

    this.resultsEl.innerHTML = cards.join('');
    if (!query) {
      this.setStatus('');
    } else if (!results.length) {
      this.setStatus('No results found.');
    } else {
      this.setStatus(`${results.length} result${results.length === 1 ? '' : 's'}`);
    }
  }
}

new VectorSearchController({
  mode: 'full',
  inputId: 'search-input',
  resultsId: 'search-results',
  statusId: 'results-count',
  limit: 20,
});

new VectorSearchController({
  mode: 'landing',
  inputId: 'landing-search',
  resultsId: 'landing-search-results',
  statusId: 'landing-search-status',
  limit: 6,
});
