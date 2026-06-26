// Floating hover-card for conlang references (dictionary / gloss / example).
// Progressive enhancement: every trigger is a real link, so with JS disabled a
// click still navigates to the entry. With JS, hover/focus/tap shows a preview
// card without leaving the page.
(function () {
  if (typeof document === 'undefined') return;

  let card;
  let hideTimer;

  function ensureCard() {
    if (card) return card;
    card = document.createElement('div');
    card.className = 'cl-hovercard';
    card.setAttribute('role', 'tooltip');
    card.hidden = true;
    card.addEventListener('mouseenter', () => clearTimeout(hideTimer));
    card.addEventListener('mouseleave', scheduleHide);
    document.body.appendChild(card);
    return card;
  }

  function show(trigger) {
    const title = trigger.getAttribute('data-card-title');
    const body = trigger.getAttribute('data-card-body');
    if (!title && !body) return;
    clearTimeout(hideTimer);
    const c = ensureCard();
    c.innerHTML = '';
    if (title) {
      const h = document.createElement('div');
      h.className = 'cl-hovercard__title';
      h.textContent = title;
      c.appendChild(h);
    }
    if (body) {
      const p = document.createElement('div');
      p.className = 'cl-hovercard__body';
      p.textContent = body;
      c.appendChild(p);
    }
    c.hidden = false;
    position(c, trigger);
  }

  function position(c, trigger) {
    const r = trigger.getBoundingClientRect();
    const margin = 8;
    // Measure after making visible.
    const cw = c.offsetWidth;
    const ch = c.offsetHeight;
    let left = window.scrollX + r.left;
    left = Math.min(left, window.scrollX + document.documentElement.clientWidth - cw - margin);
    left = Math.max(left, window.scrollX + margin);
    // Prefer above; fall back to below if it would clip the top.
    let top = window.scrollY + r.top - ch - margin;
    if (r.top - ch - margin < 0) top = window.scrollY + r.bottom + margin;
    c.style.left = left + 'px';
    c.style.top = top + 'px';
  }

  function scheduleHide() {
    clearTimeout(hideTimer);
    hideTimer = setTimeout(() => {
      if (card) card.hidden = true;
    }, 120);
  }

  const triggerFor = (el) => (el.closest ? el.closest('.cl-ref[data-card-title]') : null);

  document.addEventListener('mouseover', (e) => {
    const t = triggerFor(e.target);
    if (t) show(t);
  });
  document.addEventListener('mouseout', (e) => {
    if (triggerFor(e.target)) scheduleHide();
  });
  document.addEventListener('focusin', (e) => {
    const t = triggerFor(e.target);
    if (t) show(t);
  });
  document.addEventListener('focusout', (e) => {
    if (triggerFor(e.target)) scheduleHide();
  });
  // Touch: first tap previews, second tap (the native link) navigates.
  document.addEventListener(
    'touchstart',
    (e) => {
      const t = triggerFor(e.target);
      if (t) show(t);
      else if (card) card.hidden = true;
    },
    { passive: true }
  );
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && card) card.hidden = true;
  });
})();
