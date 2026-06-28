import { cpSync, existsSync } from 'node:fs';

const src = '.qz-boot';
const dst = 'quartz';

// Untracked-but-needed pieces upstream provides (engine + build config).
// Our customized files (content/, quartz.config.yaml, quartz.lock.json,
// package-lock.json, package.json, *.ts, custom.scss) stay as committed.
const items = [
  'quartz',                       // the engine source dir
  'tsconfig.json',
  'globals.d.ts',
  'index.d.ts',
  'quartz.config.default.yaml',
];

for (const it of items) {
  const from = `${src}/${it}`;
  const to = `${dst}/${it}`;
  if (!existsSync(from)) { console.log(`skip (missing): ${it}`); continue; }
  cpSync(from, to, { recursive: true });
  console.log(`copied: ${it}`);
}
console.log('assemble: done');
