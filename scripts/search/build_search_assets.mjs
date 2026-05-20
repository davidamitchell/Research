import { build } from 'esbuild';
import path from 'node:path';

const root = path.resolve(process.cwd());
const outdir = path.join(root, 'scripts', 'search', 'dist');

const common = {
  bundle: true,
  format: 'esm',
  platform: 'browser',
  target: ['es2020'],
  minify: true,
  sourcemap: false,
  logLevel: 'info',
};

await build({
  ...common,
  entryPoints: [path.join(root, 'scripts', 'search', 'src', 'search-runtime.js')],
  outfile: path.join(outdir, 'search-runtime.js'),
});

await build({
  ...common,
  entryPoints: [path.join(root, 'scripts', 'search', 'src', 'search-worker.js')],
  outfile: path.join(outdir, 'search-worker.js'),
});
