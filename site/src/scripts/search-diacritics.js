// Live diacritic conversion for the Starlight (Pagefind) search box. The site's
// search index stores the conlang's diacritic forms, but those marks are hard to
// type, so we let the reader type the same postfix ASCII triggers the typer uses
// (e.g. `cancio1n`, `a:`) and convert the query in place before Pagefind reads it.
//
// Mechanism: a capture-phase `input` listener on the document runs BEFORE
// Pagefind's own (bubble-phase) handler. We rewrite the input's value to the
// converted form, so Pagefind searches the diacritic text with no re-dispatch
// (which would loop). Requires window.Diacritics from diacritics.js, inlined
// ahead of this script in astro.config.mjs.
(function () {
  if (typeof document === 'undefined') return;

  const isSearchInput = (el) =>
    el &&
    el.tagName === 'INPUT' &&
    (el.classList.contains('pagefind-ui__search-input') ||
      (el.closest && el.closest('.pagefind-ui')));

  document.addEventListener(
    'input',
    (e) => {
      const el = e.target;
      if (!isSearchInput(el)) return;
      const D = window.Diacritics;
      if (!D || typeof D.convert !== 'function') return;

      const converted = D.convert(el.value, { strict: false, stack: false });
      if (converted === el.value) return;

      el.value = converted;
      // Keep the caret at the end — triggers are postfix, so the user is always
      // typing at the tail of the query.
      try {
        const end = converted.length;
        el.setSelectionRange(end, end);
      } catch (_) {
        /* setSelectionRange not supported on some input types — ignore */
      }
    },
    true // capture phase: run before Pagefind's handler
  );
})();
