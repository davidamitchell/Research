function escapeHtml(value) {
  return String(value || '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

function normalizeForSearch(value) {
  return String(value || '')
    .normalize('NFKD')
    .replaceAll(/\p{M}+/gu, '')
    .toLowerCase()
    .replaceAll(/[^a-z0-9]+/g, ' ')
    .trim();
}

function tokenizeSearchText(value) {
  const normalized = normalizeForSearch(value);
  return normalized ? normalized.split(/\s+/) : [];
}

function scoreSearchMatch(query, searchableText) {
  const queryTokens = tokenizeSearchText(query);
  if (!queryTokens.length) return 0;

  const text = normalizeForSearch(searchableText);
  if (!text) return 0;

  const textTokens = text.split(/\s+/);
  const textTokenSet = new Set(textTokens);

  let score = 0;
  let matched = 0;

  queryTokens.forEach((token) => {
    if (!token) return;

    const forms = [token];
    if (token.endsWith('ies') && token.length > 3) forms.push(`${token.slice(0, -3)}y`);
    if (token.endsWith('es') && token.length > 3) forms.push(token.slice(0, -2));
    if (token.endsWith('s') && token.length > 3) forms.push(token.slice(0, -1));

    let best = 0;
    let tokenMatched = false;

    for (const form of forms) {
      if (!form) continue;

      if (textTokenSet.has(form)) {
        tokenMatched = true;
        best = Math.max(best, 18);
        break;
      }

      if (text.includes(form)) {
        tokenMatched = true;
        best = Math.max(best, 14);
      } else {
        for (const tokenInText of textTokens) {
          if (tokenInText.startsWith(form) || form.startsWith(tokenInText)) {
            tokenMatched = true;
            best = Math.max(best, 10);
            break;
          }
        }
      }

      if (best >= 18) break;
    }

    if (tokenMatched) {
      matched += 1;
      score += best;
    }
  });

  if (matched === 0) return 0;
  if (matched < queryTokens.length && score < 80) return 0;
  return score;
}

function debounce(fn, waitMs) {
  let timer = null;
  return (...args) => {
    if (timer) clearTimeout(timer);
    timer = setTimeout(() => fn(...args), waitMs);
  };
}

class SearchController {
  constructor({ mode, inputId, resultsId, statusId, limit }) {
    this.mode = mode;
    this.input = document.getElementById(inputId);
    this.resultsEl = document.getElementById(resultsId);
    this.statusEl = document.getElementById(statusId);
    this.limit = limit;
    this.items = [];
    this.ready = false;
    this.booting = false;

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
      this.input.value = params.get('q') || '';
      this.ensureReady();
    }
  }

  setStatus(message) {
    if (this.statusEl) this.statusEl.textContent = message || '';
  }

  async ensureReady() {
    if (this.ready || this.booting || !this.input) return;
    this.booting = true;
    this.setStatus('Loading search index…');

    try {
      const response = await fetch('/Research/search-index.json');
      if (!response.ok) throw new Error(`Failed to fetch index: ${response.status}`);
      const payload = await response.json();
      this.items = Array.isArray(payload?.items) ? payload.items : [];
      this.ready = true;
      this.booting = false;
      if (this.input.value.trim()) this.search();
      else this.setStatus('');
    } catch (error) {
      this.booting = false;
      this.setStatus(error instanceof Error ? error.message : 'Search failed to initialize.');
    }
  }

  search() {
    if (!this.ready || !this.input) return;

    const query = this.input.value.trim();
    if (!query) {
      this.renderResults([]);
      this.setStatus('');
      if (this.mode === 'full') history.replaceState(null, '', window.location.pathname);
      return;
    }

    const scored = this.items
      .map((item, index) => {
        const searchBlob = `${item.title || ''} ${item.question_excerpt || ''} ${String(item.tags || []).replaceAll(',', ' ')}`;
        return { item, score: scoreSearchMatch(query, searchBlob), index };
      })
      .filter((entry) => entry.score > 0)
      .sort((a, b) => (b.score - a.score) || (a.index - b.index))
      .slice(0, this.limit)
      .map((entry) => ({ ...entry.item, score: entry.score }));

    this.renderResults(scored);

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
      const tags = (item.tags || []).map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`).join('');
      const excerpt = item.findings_excerpt || item.question_excerpt || '';
      const url = item.url || `/Research/research/${item.slug}.html`;
      return `<a class="card" href="${escapeHtml(url)}"><div class="card-title">${escapeHtml(item.title)}</div><div class="card-meta">${escapeHtml(item.added)}</div><div class="card-tags">${tags}</div><div class="card-excerpt">${escapeHtml(excerpt)}</div></a>`;
    });

    this.resultsEl.innerHTML = cards.join('');
    if (!results.length) this.setStatus('No results found.');
    else this.setStatus(`${results.length} result${results.length === 1 ? '' : 's'}`);
  }
}

new SearchController({
  mode: 'full',
  inputId: 'search-input',
  resultsId: 'search-results',
  statusId: 'results-count',
  limit: 20,
});

new SearchController({
  mode: 'landing',
  inputId: 'landing-search',
  resultsId: 'landing-search-results',
  statusId: 'landing-search-status',
  limit: 6,
});
