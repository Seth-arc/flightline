(() => {
  const S = window.Settle;
  const theme = document.getElementById('theme-button');
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  function applyTheme(dark) {
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    theme.setAttribute('aria-pressed', String(dark));
  }
  let saved;
  try { saved = localStorage.getItem('flightline-theme'); } catch { /* Storage can be unavailable in private contexts. */ }
  applyTheme(saved === 'dark' || (saved !== 'light' && systemTheme.matches));
  theme.hidden = false;
  theme.addEventListener('click', () => {
    const dark = theme.getAttribute('aria-pressed') !== 'true';
    applyTheme(dark);
    saved = dark ? 'dark' : 'light';
    try { localStorage.setItem('flightline-theme', saved); } catch { /* The current-session choice still applies. */ }
  });
  systemTheme.addEventListener('change', event => { if (!saved) applyTheme(event.matches); });

  const group = document.querySelector('.st-seg');
  const indicator = group.querySelector('.st-seg-indicator');
  const options = [...group.querySelectorAll('.st-seg-option')];
  const panels = [...document.querySelectorAll('.workflow-panel')];
  group.hidden = false;
  let x = 0, width = 0;
  const paint = () => {
    indicator.style.transform = `translateX(${x}px)`;
    indicator.style.width = `${Math.max(0, width)}px`;
  };
  // The shared indicator explains selection continuity between sibling scenarios.
  const sx = S?.spring({ preset: 'snappy', precision: 0.05, paint: false, onUpdate: v => { x = v; paint(); } });
  const sw = S?.spring({ preset: 'snappy', precision: 0.05, paint: false, onUpdate: v => { width = v; paint(); } });
  function select(button, animate = true, focus = false) {
    options.forEach(option => {
      const active = option === button;
      option.setAttribute('aria-checked', String(active));
      option.tabIndex = active ? 0 : -1;
    });
    panels.forEach(panel => { panel.hidden = panel.id !== button.dataset.panel; });
    if (focus) button.focus();
    if (sx && sw) {
      sx[animate ? 'to' : 'jump'](button.offsetLeft);
      sw[animate ? 'to' : 'jump'](button.offsetWidth);
    } else { x = button.offsetLeft; width = button.offsetWidth; paint(); }
  }
  options.forEach((option, i) => {
    option.addEventListener('click', () => select(option));
    option.addEventListener('keydown', event => {
      let index;
      if (['ArrowRight', 'ArrowDown'].includes(event.key)) index = (i + 1) % options.length;
      if (['ArrowLeft', 'ArrowUp'].includes(event.key)) index = (i - 1 + options.length) % options.length;
      if (event.key === 'Home') index = 0;
      if (event.key === 'End') index = options.length - 1;
      if (index !== undefined) { event.preventDefault(); select(options[index], true, true); }
    });
  });
  const align = () => select(options.find(option => option.getAttribute('aria-checked') === 'true'), false);
  select(options[0], false);
  window.addEventListener('resize', align);
  if (document.fonts) document.fonts.ready.then(align);

  const copy = document.getElementById('copy-prompt');
  const prompt = document.getElementById('prompt-text');
  const status = document.getElementById('copy-status');
  copy.hidden = false;
  copy.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(prompt.textContent.trim());
      status.textContent = 'Prompt copied. Paste it into a new agent session.';
    } catch {
      const range = document.createRange();
      range.selectNodeContents(prompt);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = 'Clipboard unavailable. The prompt is selected; use your browser’s Copy command.';
    }
  });
  // Press feedback confirms direct manipulation; the page stays still at rest.
  document.querySelectorAll('.st-btn, .st-seg-option').forEach(button => S?.press(button));
})();
