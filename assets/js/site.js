/* Marsicalluminio – interazioni condivise */
(() => {
  const doc = document.documentElement;
  doc.classList.remove('no-js');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(pointer: fine)').matches;

  /* Navbar: vetro smerigliato allo scroll + barra contatti mobile */
  const nav = document.querySelector('.site-nav');
  const bar = document.querySelector('.mobile-bar');
  const onScroll = () => {
    const y = window.scrollY;
    nav && nav.classList.toggle('is-scrolled', y > 24);
    bar && bar.classList.toggle('is-visible', y > window.innerHeight * 0.6);
  };
  onScroll();
  addEventListener('scroll', onScroll, { passive: true });

  /* Menu mobile */
  const menuBtn = document.querySelector('.menu-btn');
  const setMenu = open => {
    document.body.classList.toggle('menu-open', open);
    menuBtn && menuBtn.setAttribute('aria-expanded', String(open));
  };
  menuBtn && menuBtn.addEventListener('click', () => setMenu(!document.body.classList.contains('menu-open')));
  document.querySelectorAll('.nav-links a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });

  /* Comparsa progressiva degli elementi */
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduced) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(el => io.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('is-in'));
  }

  /* Contatori numerici */
  const counters = document.querySelectorAll('[data-count]');
  const fmt = (v, dec) => v.toFixed(dec).replace('.', ',');
  const runCounter = el => {
    const end = parseFloat(el.dataset.count);
    const dec = (el.dataset.count.split('.')[1] || '').length;
    if (reduced) { el.textContent = fmt(end, dec); return; }
    const from = parseFloat(el.dataset.from || 0);
    const t0 = performance.now(), dur = 1600;
    const tick = t => {
      const p = Math.min(1, (t - t0) / dur);
      const e = 1 - Math.pow(1 - p, 4);
      el.textContent = fmt(from + (end - from) * e, dec);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if ('IntersectionObserver' in window) {
    const co = new IntersectionObserver(entries => entries.forEach(en => {
      if (en.isIntersecting) { runCounter(en.target); co.unobserve(en.target); }
    }), { threshold: 0.6 });
    counters.forEach(c => co.observe(c));
  } else counters.forEach(runCounter);

  /* Voce di menu attiva in base alla sezione visibile */
  const links = [...document.querySelectorAll('.nav-links a[href^="#"]')];
  const sections = links.map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if (sections.length && 'IntersectionObserver' in window) {
    const so = new IntersectionObserver(entries => entries.forEach(en => {
      if (!en.isIntersecting) return;
      links.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + en.target.id));
    }), { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(s => so.observe(s));
  }

  if (!fine || reduced) return;

  /* Luce che segue il cursore su pulsanti e card */
  document.querySelectorAll('.btn-primary, .spot').forEach(el => {
    el.addEventListener('pointermove', e => {
      const r = el.getBoundingClientRect();
      el.style.setProperty('--x', (e.clientX - r.left) + 'px');
      el.style.setProperty('--y', (e.clientY - r.top) + 'px');
    });
  });

  /* Inclinazione 3D */
  document.querySelectorAll('[data-tilt]').forEach(el => {
    const max = parseFloat(el.dataset.tilt) || 8;
    let raf;
    el.addEventListener('pointermove', e => {
      const r = el.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - .5;
      const py = (e.clientY - r.top) / r.height - .5;
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        el.style.setProperty('--rx', (-py * max).toFixed(2) + 'deg');
        el.style.setProperty('--ry', (px * max).toFixed(2) + 'deg');
        el.style.setProperty('--gx', ((px + .5) * 100).toFixed(1) + '%');
        el.style.setProperty('--gy', ((py + .5) * 100).toFixed(1) + '%');
      });
    });
    el.addEventListener('pointerleave', () => {
      el.style.setProperty('--rx', '0deg');
      el.style.setProperty('--ry', '0deg');
    });
  });
})();
