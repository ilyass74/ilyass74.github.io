/** Progressive enhancement. All technical narratives are pre-rendered HTML. */
const menuButton = document.querySelector('[data-menu-button]');
const menu = document.querySelector('#navigation');
menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  menu?.classList.toggle('is-open', open);
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && menuButton?.getAttribute('aria-expanded') === 'true') {
    menuButton.setAttribute('aria-expanded', 'false');
    menu?.classList.remove('is-open');
    menuButton.focus();
  }
});
const explorer = document.querySelector('[data-explorer]');
if (explorer) {
  const search = explorer.querySelector('input[type=search]');
  const filters = [...explorer.querySelectorAll('[data-category]')];
  const entries = [...explorer.querySelectorAll('[data-project]')];
  const status = explorer.querySelector('[data-result-count]');
  const empty = explorer.querySelector('[data-empty]');
  let category = 'All';
  const params = new URLSearchParams(location.search);
  search.value = params.get('q') || '';
  if (filters.some(button => button.dataset.category === params.get('discipline'))) category = params.get('discipline');
  const update = () => {
    const query = search.value.trim().toLowerCase();
    let count = 0;
    for (const entry of entries) {
      const matches = (category === 'All' || entry.dataset.discipline === category) && entry.dataset.search.includes(query);
      entry.hidden = !matches;
      if (matches) count++;
    }
    filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.category === category)));
    status.textContent = `${count} ${count === 1 ? 'project' : 'projects'} in view`;
    empty.hidden = count !== 0;
    const state = new URLSearchParams();
    if (query) state.set('q', search.value.trim());
    if (category !== 'All') state.set('discipline', category);
    history.replaceState(null, '', location.pathname + (state.size ? '?' + state : '') + location.hash);
  };
  search.addEventListener('input', update);
  filters.forEach(button => button.addEventListener('click', () => {category = button.dataset.category; update();}));
  explorer.querySelector('[data-reset]')?.addEventListener('click', () => {search.value = ''; category = 'All'; update(); search.focus();});
  update();
}
document.querySelectorAll('[data-architecture]').forEach(architecture => {
  const buttons = [...architecture.querySelectorAll('[data-node]')];
  const panels = [...architecture.querySelectorAll('[data-node-panel]')];
  buttons.forEach((button, index) => button.addEventListener('click', () => {
    buttons.forEach((item, i) => item.setAttribute('aria-expanded', String(i === index)));
    panels.forEach((panel, i) => panel.hidden = i !== index);
  }));
  panels.forEach((panel, i) => panel.hidden = i !== 0);
});
const contentsLinks = [...document.querySelectorAll('[data-contents] a')];
if ('IntersectionObserver' in window && contentsLinks.length) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) if (entry.isIntersecting) contentsLinks.forEach(link => link.setAttribute('aria-current', link.hash === '#' + entry.target.id ? 'location' : 'false'));
  }, {rootMargin: '-12% 0px -65% 0px'});
  contentsLinks.forEach(link => {const section = document.querySelector(link.hash); if (section) observer.observe(section);});
}
document.querySelector('[data-copy-email]')?.addEventListener('click', async () => {
  const status = document.querySelector('[data-copy-status]');
  try {await navigator.clipboard.writeText('chakirilyass16@gmail.com'); status.textContent = 'Email address copied.';}
  catch {status.textContent = 'Email: chakirilyass16@gmail.com';}
});
