import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests/ui',
  timeout: 90_000,
  retries: 0,
  use: {
    baseURL: 'http://127.0.0.1:4173',
    trace: 'retain-on-failure',
  },
  webServer: {
    command:
      "bash -lc 'npm run build:search-assets && python scripts/build_site.py && rm -rf /tmp/research-site && mkdir -p /tmp/research-site && cp -R docs /tmp/research-site/Research && python -m http.server 4173 --directory /tmp/research-site'",
    port: 4173,
    timeout: 300_000,
    reuseExistingServer: true,
  },
});
