// @ts-check
import { readFileSync } from 'node:fs';
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import remarkConlang from './src/plugins/remark-conlang.mjs';

// Inline client scripts so they ship on every page without a separate request or
// base-path juggling. Order matters: diacritics.js defines window.Diacritics,
// which search-diacritics.js consumes, so it must come first.
const inlineScript = (rel) => readFileSync(new URL(rel, import.meta.url), 'utf8');
const headJS = [
  inlineScript('./src/scripts/diacritics.js'),
  inlineScript('./src/scripts/hovercard.js'),
  inlineScript('./src/scripts/search-diacritics.js'),
].join('\n;\n');

// Project Pages deploy at https://mattschinn.github.io/ref_grammar/.
// base must match the repo name; site is the user/org Pages origin.
export default defineConfig({
	site: 'https://mattschinn.github.io',
	base: '/ref_grammar',
	markdown: {
		remarkPlugins: [remarkConlang],
	},
	integrations: [
		starlight({
			title: 'Conlang Reference Grammar',
			customCss: [
				'./src/styles/site-theme.css',
				'./src/styles/hovercard.css',
				'./src/styles/diacritic-typer.css',
			],
			head: [
				// EB Garamond (body/conlang serif) loaded from Google Fonts, mirroring
				// the standalone typer tool. Brill (the IPA-glyph fallback) is self-hosted
				// via @font-face in site-theme.css.
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' } },
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: true } },
				{
					tag: 'link',
					attrs: {
						rel: 'stylesheet',
						href: 'https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&display=swap',
					},
				},
				{ tag: 'script', content: headJS },
			],
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/mattschinn/ref_grammar' },
			],
			sidebar: [
				{ label: 'Reference', items: [{ autogenerate: { directory: 'reference' } }] },
				{ label: 'Dictionary', items: [{ autogenerate: { directory: 'dictionary' } }] },
				{ label: 'Quick reference', items: [{ autogenerate: { directory: 'quickref' } }] },
				{ label: 'Tools', items: [{ autogenerate: { directory: 'tools' } }] },
			],
		}),
	],
});
