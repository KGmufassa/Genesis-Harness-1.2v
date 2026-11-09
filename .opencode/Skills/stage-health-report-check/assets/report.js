const patches = [...document.querySelectorAll('details.patch')];
const input = document.getElementById('patch-search');
const status = document.getElementById('search-status');
const filter = () => {
  const query = input.value.trim().toLowerCase();
  let matches = 0;
  for (const patch of patches) {
    const match = !query || patch.textContent.toLowerCase().includes(query);
    patch.hidden = !match;
    if (match) matches++;
    if (query && match) patch.open = true;
  }
  status.textContent = query ? `${matches} of ${patches.length} patches match. Overview sections remain visible.` : `Showing all ${patches.length} patches · Filter patches or browse the section navigation.`;
};
input.addEventListener('input', filter);
document.getElementById('expand').addEventListener('click', () => patches.filter(p => !p.hidden).forEach(p => p.open = true));
document.getElementById('collapse').addEventListener('click', () => patches.forEach(p => p.open = false));
document.getElementById('print').addEventListener('click', () => window.print());
function revealHash() {
  const target = document.getElementById(location.hash.slice(1));
  if (target?.matches('details.patch')) {
    if (target.hidden) { input.value = ''; filter(); }
    target.open = true;
    target.scrollIntoView({block:'start'});
  }
}
window.addEventListener('hashchange', revealHash);
document.querySelectorAll('.sidebar a[href^="#patch-"]').forEach(link => link.addEventListener('click', () => {
  const target = document.getElementById(link.hash.slice(1));
  if (target?.matches('details.patch')) {
    if (target.hidden) { input.value = ''; filter(); }
    target.open = true;
  }
}));
let printState = [];
window.addEventListener('beforeprint', () => { printState = patches.map(p => p.open); patches.forEach(p => p.open = true); });
window.addEventListener('afterprint', () => { patches.forEach((p,i) => p.open = printState[i]); });
revealHash();
