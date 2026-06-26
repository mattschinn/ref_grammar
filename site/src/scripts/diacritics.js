// Shared diacritic-conversion engine. Ported from
// tools/diacritic-typer/diacritic_typer.html so the site search bar and the
// in-site typer page share one implementation. Exposes a global rather than ES
// exports so it can be concatenated into the inlined <head> script alongside
// hovercard.js and search-diacritics.js (see astro.config.mjs).
//
// Postfix triggers: type the base letter, then the trigger. See the cheat sheet
// on the typer page. NEW vs. the standalone tool: `:` adds a diaeresis to
// vowels (a: -> ä, o: -> ö, …).
(function () {
  if (typeof window === 'undefined') return;

  const COMBINING = {
    acute:      '́',
    grave:      '̀',
    ogonek:     '̨',
    tilde:      '̃',
    caron:      '̌',
    circumflex: '̂',
    diaeresis:  '̈',
  };

  const RULES = {};

  function addRule(num, letters, mark, precomposedSet) {
    for (const letter of letters) {
      const hasPrecomposed = precomposedSet ? precomposedSet.has(letter) : true;
      RULES[`${num}:${letter}`] = { mark, precomposed: hasPrecomposed };
    }
  }

  // 1 = acute: á é í ó ú ý ẃ ś ŕ ń ḿ all precomposed; x-acute is not
  addRule(1, 'srnmaeiouyw', COMBINING.acute, new Set('srnmaeiouyw'));
  addRule(1, 'x', COMBINING.acute, new Set());

  // 4 = grave: à è ì ò ù ỳ ẁ all precomposed
  addRule(4, 'aeiouyw', COMBINING.grave, new Set('aeiouyw'));

  // 2 = nasalization
  addRule(2, 'aeou', COMBINING.ogonek, new Set('aeou'));
  addRule(2, 'i', COMBINING.tilde, new Set('i'));
  addRule(2, 'y', COMBINING.tilde, new Set('y'));
  addRule(2, 'w', COMBINING.tilde, new Set());

  // 3 = ligatures
  RULES['3:a'] = { replacement: 'æ', upperReplacement: 'Æ', precomposed: true };
  RULES['3:e'] = { replacement: 'œ', upperReplacement: 'Œ', precomposed: true };
  RULES['3:o'] = { replacement: 'œ', upperReplacement: 'Œ', precomposed: true };

  // 5 = háček on s r n: š ř ň all precomposed
  addRule(5, 'srn', COMBINING.caron, new Set('srn'));

  // 9 = thorn/eth
  RULES['9:t'] = { replacement: 'þ', upperReplacement: 'Þ', precomposed: true };
  RULES['9:d'] = { replacement: 'ð', upperReplacement: 'Ð', precomposed: true };

  // c = circumflex on vowels+w/y: â ê î ô û ŵ ŷ all precomposed
  addRule('c', 'aeiouwy', COMBINING.circumflex, new Set('aeiouwy'));

  // d = diaeresis on vowels: ä ë ï ö ü ÿ all precomposed (Ÿ = U+0178)
  addRule('d', 'aeiouy', COMBINING.diaeresis, new Set('aeiouy'));

  // Ligatures as stacking bases
  RULES['1:æ'] = { mark: COMBINING.acute, precomposed: true };
  RULES['1:œ'] = { mark: COMBINING.acute, precomposed: false };

  function computeTriggerMask(text, stack) {
    const chars = Array.from(text);
    const triggers = new Array(chars.length).fill(false);
    const receivers = new Array(chars.length).fill(false);
    let prevLetterIdx = -1;
    let prevLetterChar = '';
    let prevHasDiacritic = false;

    function markReceiver() {
      if (prevLetterIdx >= 0) receivers[prevLetterIdx] = true;
    }

    for (let i = 0; i < chars.length; i++) {
      const ch = chars[i];

      function canTrigger(sym, prevLower) {
        switch (sym) {
          case '`': return 'srnmaeiouywx'.includes(prevLower);
          case '4': return 'aeiouyw'.includes(prevLower);
          case '~': return 'iyw'.includes(prevLower);
          case '^': return 'aeiouwy'.includes(prevLower);
          case ':': return 'aeiouy'.includes(prevLower);
          case 'V': return 'srn'.includes(prevLower);
          case 'J': return 'aeou'.includes(prevLower);
          case 'Q': return prevLower === 't' || prevLower === 'd';
          case '3': return prevLower === 'a' || prevLower === 'e' || prevLower === 'o';
          case '7': return /\p{L}/u.test(prevLower);
          default:  return false;
        }
      }

      const isInterpunct = (s) => s === '7' || s === '.';
      const stackBlocked = (sym) => !stack && prevHasDiacritic && !isInterpunct(sym);
      const prevLower = prevLetterChar.toLowerCase();

      if (/[0-9]/.test(ch)) {
        if (prevLetterIdx >= 0 && canTrigger(ch, prevLower) && !stackBlocked(ch)) {
          triggers[i] = true;
          if (!isInterpunct(ch)) {
            markReceiver();
            prevHasDiacritic = true;
          }
        }
      } else if (ch === '`' || ch === '~' || ch === '^' || ch === ':') {
        if (prevLetterIdx >= 0 && canTrigger(ch, prevLower) && !stackBlocked(ch)) {
          triggers[i] = true;
          markReceiver();
          prevHasDiacritic = true;
        }
      } else if (ch === 'V' || ch === 'J' || ch === 'Q') {
        if (prevLetterIdx >= 0 && /\p{L}/u.test(prevLetterChar) && canTrigger(ch, prevLower) && !stackBlocked(ch)) {
          triggers[i] = true;
          markReceiver();
          prevHasDiacritic = true;
        } else {
          prevLetterIdx = i;
          prevLetterChar = ch;
          prevHasDiacritic = false;
        }
      } else if (ch === '.') {
        const nextCh = chars[i + 1];
        if (prevLetterIdx >= 0 && /\p{L}/u.test(prevLetterChar) && nextCh && /\p{L}/u.test(nextCh)) {
          triggers[i] = true;
        }
      } else if (/\p{L}/u.test(ch)) {
        prevLetterIdx = i;
        prevLetterChar = ch;
        prevHasDiacritic = false;
      } else {
        prevLetterIdx = -1;
        prevLetterChar = '';
        prevHasDiacritic = false;
      }
    }
    return { triggers, receivers };
  }

  function convert(text, strict, stack) {
    const chars = Array.from(text);
    const result = [];
    const baseLetters = [];

    function pushResult(entry, base) {
      result.push(entry);
      baseLetters.push(base !== undefined ? base : entry);
    }
    function replaceLast(entry, base) {
      result[result.length - 1] = entry;
      if (base !== undefined) baseLetters[baseLetters.length - 1] = base;
    }

    function symbolToNumber(sym, prevLower) {
      switch (sym) {
        case '`': return '1';
        case '~': return 'iyw'.includes(prevLower) ? '2' : null;
        case '^': return 'aeiouwy'.includes(prevLower) ? 'c' : null;
        case ':': return 'aeiouy'.includes(prevLower) ? 'd' : null;
        case 'V': return 'srn'.includes(prevLower) ? '5' : null;
        case 'J': return 'aeou'.includes(prevLower) ? '2' : null;
        case 'Q': return (prevLower === 't' || prevLower === 'd') ? '9' : null;
        default:  return null;
      }
    }

    for (let i = 0; i < chars.length; i++) {
      const ch = chars[i];
      let numericTrigger = null;

      if (result.length > 0) {
        const prevBaseForCheck = baseLetters[baseLetters.length - 1].charAt(0);
        const prevLowerForCheck = prevBaseForCheck.toLowerCase();

        if (/[0-9]/.test(ch)) {
          if (ch === '3' || ch === '4' || ch === '7') {
            numericTrigger = ch;
          } else {
            pushResult(ch);
            continue;
          }
        } else if (ch === '`' || ch === '~' || ch === '^' || ch === ':') {
          numericTrigger = symbolToNumber(ch, prevLowerForCheck);
          if (numericTrigger === null) {
            // `:` that isn't a valid trigger is a literal colon.
            if (ch === ':') pushResult(ch);
            continue;
          }
        } else if (ch === 'V' || ch === 'J' || ch === 'Q') {
          const lastBase = baseLetters[baseLetters.length - 1].charAt(0);
          if (/\p{L}/u.test(lastBase)) {
            numericTrigger = symbolToNumber(ch, prevLowerForCheck);
            if (numericTrigger === null) { pushResult(ch); continue; }
          } else {
            pushResult(ch);
            continue;
          }
        } else if (ch === '.') {
          const nextCh = chars[i + 1];
          if (/\p{L}/u.test(prevBaseForCheck) && nextCh && /\p{L}/u.test(nextCh)) {
            pushResult('·');
          } else {
            pushResult(ch);
          }
          continue;
        }
      } else if (/[0-9]/.test(ch)) {
        if (ch === '3' || ch === '4' || ch === '7') { continue; }
        pushResult(ch);
        continue;
      } else if (ch === '`' || ch === '~' || ch === '^') {
        continue;
      } else if (ch === ':') {
        pushResult(ch);
        continue;
      }

      if (numericTrigger !== null) {
        const num = numericTrigger;
        const prev = result[result.length - 1];
        const prevBase = baseLetters[baseLetters.length - 1].charAt(0);
        const prevLower = prevBase.toLowerCase();
        const isUpper = prevBase !== prevLower;

        if (!stack && prev !== prevBase) { continue; }

        if (num === '7') {
          if (/\p{L}/u.test(prevBase)) { pushResult('·'); }
          continue;
        }

        const rule = RULES[`${num}:${prevLower}`];
        if (!rule) continue;
        if (strict && !rule.precomposed) continue;

        if (rule.replacement) {
          const newVal = isUpper ? rule.upperReplacement : rule.replacement;
          replaceLast(newVal, newVal);
        } else {
          // When any diacritic lands on the second i of an ii digraph,
          // make the first i dotless automatically.
          if (prevLower === 'i' && result.length >= 2) {
            const beforePrevBase = baseLetters[baseLetters.length - 2].charAt(0);
            if (beforePrevBase.toLowerCase() === 'i') {
              const dotless = beforePrevBase !== beforePrevBase.toLowerCase() ? 'I' : 'ı';
              result[result.length - 2] = dotless;
              baseLetters[baseLetters.length - 2] = dotless;
              result[result.length - 1] = (prev + rule.mark).normalize('NFC');
              continue;
            }
          }
          const composed = (prev + rule.mark).normalize('NFC');
          if (strict && Array.from(composed).length > 1) { continue; }
          result[result.length - 1] = composed;
        }
      } else {
        pushResult(ch);
      }
    }

    // Post-process: if a diacritic ended up on the first i of an ii pair
    // (e.g. from pasted text), move it to the second and make first dotless.
    let out = result.join('');
    out = out
      .replace(/íi/g, 'ıí').replace(/Íi/g, 'Íı')
      .replace(/ìi/g, 'ıì').replace(/Ìi/g, 'Ìı')
      .replace(/îi/g, 'ıî').replace(/Îi/g, 'Îı')
      .replace(/ïi/g, 'ıï').replace(/Ïi/g, 'Ïı')
      .replace(/ĩi/g, 'ıĩ').replace(/Ĩi/g, 'Iĩ')
      .replace(/ĩI/g, 'ıĨ').replace(/ĨI/g, 'IĨ');
    return out;
  }

  // Accept either positional (text, strict, stack) or an options object as the
  // second argument, so callers can write convert(text, { strict, stack }).
  function convertPublic(text, a, b) {
    if (a && typeof a === 'object') return convert(text, !!a.strict, !!a.stack);
    return convert(text, !!a, !!b);
  }

  window.Diacritics = { convert: convertPublic, computeTriggerMask };
})();
