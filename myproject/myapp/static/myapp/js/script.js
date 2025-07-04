console.log('script.js загружен');

/* ─────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {

  /* ==== 1.  Анимация появления (.reveal) ==== */
  const revealObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-active');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  document.querySelectorAll('.reveal')
          .forEach(el => revealObserver.observe(el));
  window.revealObserver = revealObserver;           // удобно дебажить
  console.log('Reveal-observer запущен ✅');

  /* ==== 2.  Переключатель темы ==== */
  const body        = document.body;
  const btnTheme    = document.getElementById('themeToggle');
  const iconTheme   = document.getElementById('themeIcon');

  // ставим сохранённую тему
  const saved = localStorage.getItem('theme') || 'dark';
  if (saved === 'light') {
    body.classList.add('theme-light');
    iconTheme.classList.replace('fa-moon', 'fa-sun');
  }

  btnTheme.addEventListener('click', () => {
    const light = body.classList.toggle('theme-light');
    localStorage.setItem('theme', light ? 'light' : 'dark');
    iconTheme.classList.toggle('fa-moon', !light);
    iconTheme.classList.toggle('fa-sun',  light);
  });

  /* ==== 3.  Бургер-меню ==== */
  const burgerBtn  = document.getElementById('burgerBtn');
  const burgerIcon = document.getElementById('burgerIcon');
  const navLinks   = document.querySelector('.nav-links');

  if (burgerBtn && navLinks) {
    burgerBtn.addEventListener('click', () => {
      const opened = navLinks.classList.toggle('nav-open');
      burgerIcon.classList.toggle('fa-xmark', opened);
      burgerIcon.classList.toggle('fa-bars',  !opened);
      burgerBtn.classList.toggle('open', opened);
      themeToggle.classList.toggle('open', opened);
    });

    /* закрываем меню после клика */
    navLinks.querySelectorAll('a').forEach(link =>
      link.addEventListener('click', () => {
        navLinks.classList.remove('nav-open');
        burgerIcon.classList.add('fa-bars');
        burgerIcon.classList.remove('fa-xmark');
        burgerBtn.classList.remove('open');
      })
    );
  }

  /* ==== 4.  Lazy-loading fallback ==== */
  const lazyImgs = Array.from(document.querySelectorAll('img[loading="lazy"]'));
  if (!('loading' in HTMLImageElement.prototype) && 'IntersectionObserver' in window) {

    const imgObserver = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          obs.unobserve(img);
        }
      });
    }, { rootMargin: '200px' });

    lazyImgs.forEach(img => {
      img.dataset.src = img.src;
      img.removeAttribute('src');
      imgObserver.observe(img);
    });
  }
  /* ==== 5.  Скрываем loader после полной загрузки ==== */
  window.addEventListener('load', () => {
    const loader = document.getElementById('loader');
    if (loader) loader.classList.add('hidden');
  });
});


