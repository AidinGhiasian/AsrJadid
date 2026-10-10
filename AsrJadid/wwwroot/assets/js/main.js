/* ==========================================================================
   عصرجدید — اسکریپت اصلی سایت (بدون کتابخانه خارجی)
   ========================================================================== */
(function () {
  'use strict';

  /* ---------------- helpers ---------------- */
  const $ = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.prototype.slice.call((c || document).querySelectorAll(s));
  const faDigits = '۰۱۲۳۴۵۶۷۸۹';
  const toFa = (v) => String(v).replace(/\d/g, (d) => faDigits[+d]);
  const toEn = (v) => String(v).replace(/[۰-۹]/g, (d) => faDigits.indexOf(d));

  function toast(msg, type) {
    const wrap = $('#toastWrap');
    if (!wrap) return;
    const el = document.createElement('div');
    el.className = 'toast ' + (type || 'ok');
    el.innerHTML =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' +
      (type === 'err'
        ? '<circle cx="12" cy="12" r="9"/><path d="m9 9 6 6M15 9l-6 6"/>'
        : '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>') +
      '</svg><span>' + msg + '</span>';
    wrap.appendChild(el);
    setTimeout(() => { el.style.opacity = '0'; el.style.transform = 'translateY(10px)'; }, 2600);
    setTimeout(() => el.remove(), 3000);
  }
  window.asrToast = toast;

  function openModal(html) {
    const m = $('#quickModal');
    if (!m) return;
    $('#quickBody').innerHTML = html;
    m.hidden = false;
    document.body.style.overflow = 'hidden';
  }
  function closeModal() {
    const m = $('#quickModal');
    if (!m) return;
    m.hidden = true;
    document.body.style.overflow = '';
  }

  /* ---------------- header ---------------- */
  const header = $('.js-header');
  const onScroll = () => {
    if (header) header.classList.toggle('scrolled', window.scrollY > 12);
    const top = $('.js-top');
    if (top) top.classList.toggle('show', window.scrollY > 420);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const nav = $('#mainNav');
  function closeNav() {
    if (nav) nav.classList.remove('open');
    $$('.has-mega').forEach((i) => i.classList.remove('mega-open'));
  }
  $$('.js-nav-toggle').forEach((b) =>
    b.addEventListener('click', () => {
      if (!nav) return;
      const open = nav.classList.toggle('open');
      document.body.style.overflow = open ? 'hidden' : '';
      b.innerHTML = open
        ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>'
        : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>';
    }));
  document.addEventListener('click', (e) => {
    if (nav && nav.classList.contains('open') && !nav.contains(e.target) && !e.target.closest('.js-nav-toggle')) {
      closeNav();
      document.body.style.overflow = '';
    }
  });

  /* منوی «گروه محصولات» در موبایل: لمس اول زیرمنو را باز می‌کند، لمس دوم وارد صفحه می‌شود */
  $$('.has-mega > .nav-link').forEach((link) => {
    link.addEventListener('click', (e) => {
      const item = link.parentElement;
      if (window.matchMedia('(max-width:960px)').matches && !item.classList.contains('mega-open')) {
        e.preventDefault();
        item.classList.add('mega-open');
      }
    });
  });

  /* search overlay */
  const so = $('#searchOverlay');
  $$('.js-search-open').forEach((b) => b.addEventListener('click', () => {
    if (!so) return;
    so.hidden = false;
    const inp = $('input', so);
    if (inp) setTimeout(() => inp.focus(), 60);
  }));
  $$('.js-search-close').forEach((b) => b.addEventListener('click', () => { if (so) so.hidden = true; }));
  if (so) so.addEventListener('click', (e) => { if (e.target === so) so.hidden = true; });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (so) so.hidden = true;
      closeModal();
    }
  });
  $$('.js-search-open, .js-search-close').length; // no-op
  const searchForm = so ? $('.search-form', so) : null;
  if (searchForm) searchForm.addEventListener('submit', (e) => {
    // جستجو به صفحه واقعی سرچ (Razor) هدایت می‌شود
    const input = $('input[name=q], input[type=search], input[type=text]', searchForm);
    const q = input ? input.value.trim() : '';
    if (!q) { e.preventDefault(); if (input) input.focus(); return; }
    searchForm.setAttribute('action', '/Search');
    searchForm.setAttribute('method', 'get');
    if (input) input.setAttribute('name', 'q');
  });

  /* ---------------- modal / lightbox ---------------- */
  $$('.js-modal-close').forEach((b) => b.addEventListener('click', closeModal));

  $$('.js-modal-btn').forEach((btn) => btn.addEventListener('click', (e) => {
    e.preventDefault();
    const kind = btn.getAttribute('data-modal');
    if (kind === 'video') {
      openModal('<h3>ویدیو معرفی عصرجدید</h3><div class="video-box" style="margin-top:12px">' +
        '<img src="assets/images/hero-1.jpg" alt="ویدیو"><span class="vb-overlay"></span>' +
        '<button class="video-play" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="m10 8.5 6 3.5-6 3.5v-7Z"/></svg></button></div>' +
        '<p class="muted" style="margin-top:10px">برای دریافت ویدیو کوتاه خط تولید و کاتالوگ طرح‌ها، از صفحه تماس با ما درخواست دهید.</p>');
    } else if (kind === 'review') {
      openModal('<h3>ثبت دیدگاه جدید</h3><form class="form js-form" data-ok-message="دیدگاه شما ثبت شد و پس از تأیید کارشناس منتشر می‌شود." novalidate>' +
        '<div class="field"><label>نام و نام خانوادگی</label><input type="text" required></div>' +
        '<div class="field"><label>امتیاز شما</label><select><option>۵ ستاره – عالی</option><option>۴ ستاره – خوب</option><option>۳ ستاره – متوسط</option><option>۲ ستاره – ضعیف</option><option>۱ ستاره – بد</option></select></div>' +
        '<div class="field"><label>متن دیدگاه</label><textarea rows="4" required></textarea></div>' +
        '<div class="form-actions"><button class="btn btn-primary" type="submit">ارسال دیدگاه</button></div></form>');
    } else {
      openModal('<h3>اطلاعات تکمیلی</h3><p class="muted">برای دریافت جزئیات فنی، نمونه‌سازی و قیمت نهایی با کارشناسان ما تماس بگیرید.</p>' +
        '<div class="modal-actions"><a class="btn btn-primary" href="/Contact">تماس با کارشناس</a>' +
        '<a class="btn btn-outline" href="/PriceList">لیست قیمت</a></div>');
    }
  }));

  $$('.js-lightbox').forEach((a) => a.addEventListener('click', (e) => {
    e.preventDefault();
    const img = a.getAttribute('href');
    const cap = a.querySelector('.g-overlay strong');
    const box = document.createElement('div');
    box.className = 'lightbox js-lb';
    box.innerHTML = '<button class="lightbox-close" type="button" aria-label="بستن">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg></button>' +
      '<img src="' + img + '" alt="">' +
      (cap ? '<div class="lightbox-cap">' + cap.textContent + '</div>' : '');
    document.body.appendChild(box);
    document.body.style.overflow = 'hidden';
    const kill = () => { box.remove(); document.body.style.overflow = ''; };
    box.addEventListener('click', (ev) => { if (ev.target === box || ev.target.closest('.lightbox-close')) kill(); });
    document.addEventListener('keydown', function esc(ev) {
      if (ev.key === 'Escape') { kill(); document.removeEventListener('keydown', esc); }
    });
  }));

  /* ---------------- hero slider ---------------- */
  const slider = $('.js-slider');
  if (slider) {
    const slides = $$('.slide', slider);
    const dots = $('.js-slide-dots', slider);
    let idx = 0, timer = null;
    if (dots) {
      slides.forEach((_, i) => {
        const d = document.createElement('button');
        d.type = 'button';
        d.setAttribute('aria-label', 'اسلاید ' + toFa(i + 1));
        d.addEventListener('click', () => go(i));
        dots.appendChild(d);
      });
    }
    function go(i) {
      idx = (i + slides.length) % slides.length;
      slides.forEach((s, k) => s.classList.toggle('active', k === idx));
      if (dots) $$('button', dots).forEach((d, k) => d.classList.toggle('active', k === idx));
    }
    function play() { timer = setInterval(() => go(idx + 1), 6500); }
    function stop() { clearInterval(timer); }
    const prev = $('.js-slide-prev', slider), next = $('.js-slide-next', slider);
    if (prev) prev.addEventListener('click', () => { go(idx - 1); stop(); play(); });
    if (next) next.addEventListener('click', () => { go(idx + 1); stop(); play(); });
    go(0); play();
    slider.addEventListener('mouseenter', stop);
    slider.addEventListener('mouseleave', play);
  }

  /* ---------------- tabs ---------------- */
  $$('.js-tabs').forEach((box) => {
    const heads = $$('.tab-btn', box);
    heads.forEach((h) => h.addEventListener('click', (e) => {
      const isAnchor = h.getAttribute('href') && h.getAttribute('href').charAt(0) === '#';
      if (isAnchor) e.preventDefault();
      heads.forEach((x) => x.classList.remove('active'));
      h.classList.add('active');
      const id = h.getAttribute('data-tab');
      $$('.tab-panel', box).forEach((p) => p.classList.toggle('active', p.id === id));
    }));
  });

  /* ---------------- accordion ---------------- */
  $$('.js-acc').forEach((btn) => btn.addEventListener('click', () => {
    const item = btn.closest('.acc-item');
    const open = item.classList.contains('open');
    const group = item.closest('.accordion');
    if (group) $$('.acc-item', group).forEach((i) => { i.classList.remove('open'); const h = $('.js-acc', i); if (h) h.setAttribute('aria-expanded', 'false'); });
    item.classList.toggle('open', !open);
    btn.setAttribute('aria-expanded', String(!open));
  }));

  /* ---------------- quantity ---------------- */
  $$('[data-qty]').forEach((q) => {
    const input = $('input', q);
    const minus = $('.js-minus', q), plus = $('.js-plus', q);
    if (plus) plus.addEventListener('click', () => { input.value = toFa(Math.max(1, (+toEn(input.value) || 1) + 1)); });
    if (minus) minus.addEventListener('click', () => { input.value = toFa(Math.max(1, (+toEn(input.value) || 1) - 1)); });
  });

  /* ---------------- cart & wishlist (localStorage) ---------------- */
  const store = {
    get(key, def) { try { return JSON.parse(localStorage.getItem('asr_' + key)) || def; } catch (e) { return def; } },
    set(key, val) { try { localStorage.setItem('asr_' + key, JSON.stringify(val)); } catch (e) {} }
  };
  function paintCounts() {
    const cart = store.get('cart', []);
    const wish = store.get('wish', []);
    const cn = cart.reduce((s, i) => s + i.qty, 0);
    $$('.js-cart-count').forEach((el) => { el.textContent = toFa(cn); el.hidden = cn === 0; });
    $$('.js-wish-count').forEach((el) => { el.textContent = toFa(wish.length); el.hidden = wish.length === 0; });
  }
  paintCounts();

  $$('.js-add').forEach((btn) => btn.addEventListener('click', () => {
    const card = btn.closest('[data-id]');
    const id = btn.getAttribute('data-id') || (card && card.getAttribute('data-id'));
    const qtyInput = card ? $('[data-qty] input', card) : null;
    const pageQty = $('.pd-buy [data-qty] input');
    const qty = +toEn((qtyInput || pageQty || {}).value || 1) || 1;
    const cart = store.get('cart', []);
    const found = cart.filter((i) => String(i.id) === String(id))[0];
    if (found) found.qty += qty; else cart.push({ id: +id, qty: qty });
    store.set('cart', cart);
    paintCounts();
    toast('محصول به سبد خرید اضافه شد (' + toFa(qty) + ' واحد)');
    btn.classList.add('added');
    setTimeout(() => btn.classList.remove('added'), 1200);
  }));

  $$('.js-wish').forEach((btn) => btn.addEventListener('click', (e) => {
    e.preventDefault();
    const id = +btn.getAttribute('data-id');
    let wish = store.get('wish', []);
    if (wish.indexOf(id) > -1) { wish = wish.filter((x) => x !== id); toast('از علاقه‌مندی‌ها حذف شد', 'warn'); }
    else { wish.push(id); toast('به علاقه‌مندی‌ها اضافه شد'); }
    store.set('wish', wish);
    paintCounts();
  }));

  $$('.js-compare').forEach((btn) => btn.addEventListener('click', (e) => {
    e.preventDefault();
    const id = +btn.getAttribute('data-id');
    let cmp = store.get('compare', []);
    if (cmp.indexOf(id) === -1 && cmp.length < 4) { cmp.push(id); store.set('compare', cmp); toast('به لیست مقایسه اضافه شد'); }
    else if (cmp.indexOf(id) > -1) { cmp = cmp.filter((x) => x !== id); store.set('compare', cmp); toast('از مقایسه حذف شد', 'warn'); }
    else toast('حداکثر ۴ محصول قابل مقایسه است', 'warn');
  }));

  /* quick view */
  $$('.js-quick').forEach((btn) => btn.addEventListener('click', (e) => {
    e.preventDefault();
    const card = btn.closest('.product-card');
    if (!card) return;
    const img = $('.card-media img', card);
    const name = $('.card-title', card) ? $('.card-title', card).textContent.trim() : '';
    const text = $('.card-text', card) ? $('.card-text', card).textContent.trim() : '';
    const price = $('.price', card) ? $('.price', card).querySelector('.amount').textContent : '';
    openModal('<div style="display:flex;gap:18px;flex-wrap:wrap">' +
      '<img src="' + (img ? img.getAttribute('src') : '') + '" alt="" style="width:280px;border-radius:14px;object-fit:cover">' +
      '<div style="flex:1;min-width:220px"><h3>' + name + '</h3><p class="muted">' + text + '</p>' +
      '<div class="price big"><span class="amount">' + price + '</span><span class="cur">تومان</span></div>' +
      '<div class="form-actions" style="margin-top:14px"><a class="btn btn-primary" href="product.html">مشاهده کامل محصول</a>' +
      '<a class="btn btn-outline" href="contact.html">استعلام قیمت پروژه</a></div></div></div>');
  }));

  /* ---------------- product gallery thumbs ---------------- */
  $$('.js-thumb').forEach((t) => t.addEventListener('click', () => {
    const main = $('#pdMain');
    if (!main) return;
    main.src = t.getAttribute('data-src');
    $$('.js-thumb').forEach((x) => x.classList.remove('active'));
    t.classList.add('active');
  }));

  /* ---------------- products filters ---------------- */
  const grid = $('.js-products');
  if (grid) {
    const cards = $$('.product-card', grid);
    const countEl = $('.js-result-count');
    const empty = $('#noResult');
    const activeBox = $('.js-active-filters');
    const state = { cats: [], from: 0, to: Infinity, sort: 'default', color: null, stock: false };

    function apply() {
      let shown = 0;
      cards.forEach((c) => {
        const cat = c.getAttribute('data-cat');
        const price = +c.getAttribute('data-price');
        let ok = true;
        if (state.cats.length && state.cats.indexOf(cat) === -1) ok = false;
        if (price < state.from || price > state.to) ok = false;
        if (state.color && (c.getAttribute('data-color') || '').indexOf(state.color) === -1) ok = false;
        if (state.stock && c.getAttribute('data-stock') !== '1') ok = false;
        c.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      /* sort */
      if (state.sort !== 'default') {
        const arr = cards.slice().sort((a, b) => {
          const pa = +a.getAttribute('data-price'), pb = +b.getAttribute('data-price');
          if (state.sort === 'cheap') return pa - pb;
          if (state.sort === 'expensive') return pb - pa;
          if (state.sort === 'new') return +b.getAttribute('data-id') - +a.getAttribute('data-id');
          if (state.sort === 'popular') return +b.getAttribute('data-price') - +a.getAttribute('data-price');
          return 0;
        });
        arr.forEach((c) => grid.appendChild(c));
      }
      if (countEl) countEl.textContent = toFa(shown) + ' محصول';
      if (empty) empty.hidden = shown !== 0;
      paintChips();
    }
    function paintChips() {
      if (!activeBox) return;
      activeBox.innerHTML = '';
      state.cats.forEach((c) => {
        const label = ($$('.js-filter-cat').filter((i) => i.value === c)[0] || {}).parentNode;
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'chip-btn';
        chip.innerHTML = (label ? label.textContent.trim().split('(')[0] : c) +
          ' <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>';
        chip.addEventListener('click', () => {
          state.cats = state.cats.filter((x) => x !== c);
          const box = $$('.js-filter-cat').filter((i) => i.value === c)[0];
          if (box) box.checked = false;
          apply();
        });
        activeBox.appendChild(chip);
      });
      if (state.from > 0 || state.to !== Infinity) {
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'chip-btn';
        chip.textContent = 'قیمت: ' + toFa((state.from || 0).toLocaleString('en-US').replace(/,/g, '٫')) + ' تا ' +
          (state.to === Infinity ? 'بی‌نهایت' : toFa(state.to.toLocaleString('en-US').replace(/,/g, '٫')));
        chip.addEventListener('click', () => { state.from = 0; state.to = Infinity; apply(); });
        activeBox.appendChild(chip);
      }
    }
    /* فیلتر رنگ: چیپ‌های رنگ به کارت‌های محصول وصل می‌شوند */
    $$('.color-chip').forEach((chip) => chip.addEventListener('click', () => {
      const c = (chip.getAttribute('data-color') || chip.textContent || '').trim();
      state.color = state.color === c ? null : c;
      $$('.color-chip').forEach((x) => x.classList.toggle('active', ((x.getAttribute('data-color') || x.textContent || '').trim() === state.color)));
      apply();
    }));

    $$('.js-filter-stock').forEach((cb) => cb.addEventListener('change', () => {
      state.stock = cb.checked;
      apply();
    }));

    $$('.js-filter-cat').forEach((cb) => cb.addEventListener('change', () => {
      state.cats = $$('.js-filter-cat').filter((i) => i.checked).map((i) => i.value);
      apply();
    }));
    const applyPrice = () => {
      const f = $('#priceFrom'), t = $('#priceTo');
      state.from = f && toEn(f.value).replace(/[^\d]/g, '') ? +toEn(f.value).replace(/[^\d]/g, '') : 0;
      state.to = t && toEn(t.value).replace(/[^\d]/g, '') ? +toEn(t.value).replace(/[^\d]/g, '') : Infinity;
      apply();
    };
    const apBtn = $('.js-apply-price');
    if (apBtn) apBtn.addEventListener('click', applyPrice);
    $$('.js-range').forEach((b) => b.addEventListener('click', () => {
      const f = $('#priceFrom'), t = $('#priceTo');
      if (f) f.value = toFa((+b.getAttribute('data-from')).toLocaleString('en-US'));
      if (t) t.value = toFa((+b.getAttribute('data-to')).toLocaleString('en-US'));
      applyPrice();
    }));
    const sortSel = $('.js-sort');
    if (sortSel) sortSel.addEventListener('change', () => { state.sort = sortSel.value; apply(); });
    $$('.js-clear-filters').forEach((b) => b.addEventListener('click', () => {
      $$('.js-filter-cat').forEach((i) => { i.checked = false; });
      $$('.js-filter-stock').forEach((i) => { i.checked = false; });
      state.stock = false;
      const f = $('#priceFrom'), t = $('#priceTo');
      if (f) f.value = ''; if (t) t.value = '';
      state.cats = []; state.from = 0; state.to = Infinity; state.color = null;
      $$('.color-chip').forEach((x) => x.classList.remove('active'));
      if (sortSel) { sortSel.value = 'default'; state.sort = 'default'; }
      apply();
      toast('فیلترها حذف شد');
    }));
    $$('.js-view').forEach((b) => b.addEventListener('click', () => {
      $$('.js-view').forEach((x) => x.classList.remove('active'));
      b.classList.add('active');
      grid.classList.toggle('view-list', b.getAttribute('data-view') === 'list');
    }));
    $$('.js-side-toggle').forEach((b) => b.addEventListener('click', () => {
      const card = b.closest('.side-card');
      if (card) card.classList.toggle('collapsed');
    }));
    apply();
  }

  /* ---------------- gallery filter ---------------- */
  const gFilter = $('.js-gallery-filter');
  if (gFilter) {
    const items = $$('#galleryGrid .g-item');
    $$('.chip-btn', gFilter).forEach((b) => b.addEventListener('click', () => {
      $$('.chip-btn', gFilter).forEach((x) => x.classList.remove('active'));
      b.classList.add('active');
      const f = b.getAttribute('data-filter');
      items.forEach((it) => { it.style.display = (f === 'all' || it.getAttribute('data-cat') === f) ? '' : 'none'; });
    }));
  }

  /* ---------------- blog filter ---------------- */
  const blogFilter = $('.js-blog');
  if (blogFilter) {
    const posts = $$('.blog-card', blogFilter);
    $$('[data-bfilter]').forEach((b) => b.addEventListener('click', () => {
      $$('[data-bfilter]').forEach((x) => x.classList.remove('active'));
      b.classList.add('active');
      const f = b.getAttribute('data-bfilter');
      posts.forEach((p) => { p.style.display = (f === 'all' || p.getAttribute('data-cat') === f) ? '' : 'none'; });
    }));
  }

  /* ---------------- price table filter ---------------- */
  const priceTable = $('#priceTable');
  if (priceTable) {
    const rows = $$('tbody tr', priceTable);
    $$('[data-pfilter]').forEach((b) => b.addEventListener('click', () => {
      $$('[data-pfilter]').forEach((x) => x.classList.remove('active'));
      b.classList.add('active');
      const f = b.getAttribute('data-pfilter');
      rows.forEach((r) => { r.style.display = (f === 'all' || r.getAttribute('data-cat') === f) ? '' : 'none'; });
    }));
  }

  /* ---------------- cost calculator ---------------- */
  const calc = $('.js-calc');
  if (calc) {
    const len = $('.js-calc-len'), hei = $('.js-calc-hei'), prod = $('.js-calc-prod'), waste = $('.js-calc-waste');
    const area = $('.js-calc-area'), areaW = $('.js-calc-area-w'), total = $('.js-calc-total');
    const run = () => {
      if (!len || !hei) return;
      const a = (parseFloat(toEn(len.value)) || 0) * (parseFloat(toEn(hei.value)) || 0);
      const w = 1 + (parseFloat(waste.value) || 0) / 100;
      const price = parseFloat(prod.value) || 0;
      const aw = a * w;
      if (area) area.textContent = toFa(a.toFixed(0)) + ' مترمربع';
      if (areaW) areaW.textContent = toFa(aw.toFixed(0)) + ' مترمربع';
      if (total) total.textContent = toFa(Math.round(aw * price).toLocaleString('en-US').replace(/,/g, '٫')) + ' تومان';
    };
    [len, hei, prod, waste].forEach((el) => el && el.addEventListener('input', run));
    [prod, waste].forEach((el) => el && el.addEventListener('change', run));
    run();
  }

  /* ---------------- file drop ---------------- */
  $$('.js-file-drop').forEach((box) => {
    const input = $('input[type=file]', box);
    box.addEventListener('click', () => input && input.click());
    box.addEventListener('dragover', (e) => { e.preventDefault(); box.classList.add('drag'); });
    box.addEventListener('dragleave', () => box.classList.remove('drag'));
    box.addEventListener('drop', (e) => {
      e.preventDefault(); box.classList.remove('drag');
      if (e.dataTransfer.files.length) {
        box.classList.add('has-file');
        box.querySelector('span').textContent = 'فایل انتخاب شد: ' + e.dataTransfer.files[0].name;
      }
    });
    if (input) input.addEventListener('change', () => {
      if (input.files.length) {
        box.classList.add('has-file');
        const s = box.querySelector('span');
        if (s) s.textContent = 'فایل انتخاب شد: ' + input.files[0].name;
      }
    });
  });

  /* ---------------- counters ---------------- */
  const counters = $$('.js-count');
  if (counters.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        const el = en.target, target = +el.getAttribute('data-to') || 0;
        let cur = 0;
        const step = Math.max(1, Math.round(target / 60));
        const t = setInterval(() => {
          cur += step;
          if (cur >= target) { cur = target; clearInterval(t); }
          el.textContent = toFa(cur.toLocaleString('en-US').replace(/,/g, '٫'));
        }, 24);
        io.unobserve(el);
      });
    }, { threshold: .4 });
    counters.forEach((c) => io.observe(c));
  }

  /* ---------------- password toggle / OTP / timer ---------------- */
  $$('.js-pass-toggle').forEach((b) => b.addEventListener('click', () => {
    const input = b.parentNode.querySelector('input');
    if (!input) return;
    input.type = input.type === 'password' ? 'text' : 'password';
  }));
  const otp = $('.js-otp');
  if (otp) {
    const inputs = $$('input', otp);
    inputs.forEach((inp, i) => {
      inp.addEventListener('input', () => { if (inp.value && inputs[i + 1]) inputs[i + 1].focus(); });
      inp.addEventListener('keydown', (e) => { if (e.key === 'Backspace' && !inp.value && inputs[i - 1]) inputs[i - 1].focus(); });
    });
  }
  const timerEl = $('.js-timer');
  if (timerEl) {
    let left = 90;
    setInterval(() => {
      if (left <= 0) return;
      left--;
      const m = Math.floor(left / 60), s = left % 60;
      timerEl.textContent = toFa((m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s);
    }, 1000);
    const resend = $('.js-resend');
    if (resend) resend.addEventListener('click', () => { left = 90; toast('کد تأیید مجدداً ارسال شد'); });
  }

  /* ---------------- forms: اعتبارسنجی و بازخورد سراسری ---------------- */
  document.addEventListener('submit', (e) => {
    const form = e.target && e.target.closest ? e.target.closest('form.js-form') : null;
    if (!form) return;
    e.preventDefault();
    let bad = null;
    $$('input[required], textarea[required], select[required]', form).forEach((f) => {
      const empty = !f.value || !String(f.value).trim();
      f.classList.toggle('error', empty);
      if (empty && !bad) bad = f;
    });
    if (bad) {
      toast('لطفاً فیلدهای الزامی را تکمیل کنید', 'err');
      bad.focus();
      return;
    }
    toast(form.getAttribute('data-ok-message') || 'درخواست شما ثبت شد. کارشناسان ما به‌زودی با شما تماس می‌گیرند.');
    form.reset();
    $$('.file-drop', form).forEach((b) => { b.classList.remove('has-file'); });
  });

  /* ---------------- خبرنامه: ارسال واقعی به سرور ---------------- */
  $$('form.js-newsletter').forEach((form) => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = $('input[type=email], input[name=email]', form);
      const email = (emailInput ? emailInput.value : '').trim();
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
        toast('ایمیل معتبر وارد کنید', 'err');
        if (emailInput) emailInput.focus();
        return;
      }
      const btn = $('button[type=submit]', form);
      if (btn) btn.disabled = true;
      fetch(form.getAttribute('action') || '/Contact?handler=Newsletter', {
        method: 'POST',
        body: new FormData(form),
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
      })
        .then((r) => r.json())
        .then((d) => {
          toast((d && d.message) || 'ایمیل شما در خبرنامه ثبت شد');
          if (d && d.ok) form.reset();
        })
        .catch(() => toast('ارتباط با سرور برقرار نشد؛ دوباره تلاش کنید', 'err'))
        .finally(() => { if (btn) btn.disabled = false; });
    });
  });

  /* ---------------- فرم استخدام: انتخاب موقعیت از فهرست ---------------- */
  $$('[data-job]').forEach((a) => a.addEventListener('click', () => {
    const sel = $('#jobPosition');
    if (sel) sel.value = a.getAttribute('data-job') || sel.value;
  }));

  /* ---------------- misc ---------------- */
  $$('.js-top').forEach((b) => b.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' })));
  $$('.js-print').forEach((b) => b.addEventListener('click', () => window.print()));
  /* ---------------- share buttons (تلگرام/واتس‌اپ/لینکدین/کپی) ---------------- */
  const pageUrl = encodeURIComponent(window.location.href);
  const pageTitle = encodeURIComponent(document.title);
  const shareTargets = {
    telegram: 'https://t.me/share/url?url=' + pageUrl + '&text=' + pageTitle,
    whatsapp: 'https://wa.me/?text=' + pageTitle + '%20' + pageUrl,
    linkedin: 'https://www.linkedin.com/sharing/share-offsite/?url=' + pageUrl
  };
  $$('[data-share]').forEach((el) => {
    el.addEventListener('click', (e) => {
      const kind = el.getAttribute('data-share');
      if (kind === 'copy' || !shareTargets[kind]) {
        e.preventDefault();
        if (navigator.clipboard) {
          navigator.clipboard.writeText(window.location.href);
          toast('نشانی صفحه کپی شد');
        } else {
          window.prompt('نشانی صفحه را کپی کنید:', window.location.href);
        }
        return;
      }
      e.preventDefault();
      window.open(shareTargets[kind], '_blank', 'noopener,width=640,height=560');
    });
  });

  /* ---------------- detail hooks (quantity stepper + sticky buy) ---------------- */
  const qtyBox = $('.pd-buy [data-qty]');
  if (qtyBox && !qtyBox.closest('[data-qty]').querySelector('.qty-btn')) {
    const input = $('input', qtyBox);
    if (input) {
      const step = (delta) => { input.value = toFa(Math.max(1, (+toEn(input.value) || 1) + delta)); };
      const minus = document.createElement('button');
      minus.type = 'button';
      minus.className = 'qty-btn js-minus';
      minus.setAttribute('aria-label', 'کاهش');
      minus.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M5 12h14"/></svg>';
      const plus = document.createElement('button');
      plus.type = 'button';
      plus.className = 'qty-btn js-plus';
      plus.setAttribute('aria-label', 'افزایش');
      plus.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>';
      minus.addEventListener('click', () => step(-1));
      plus.addEventListener('click', () => step(1));
      input.parentNode.insertBefore(minus, input);
      input.parentNode.insertBefore(plus, input.nextSibling);
    }
  }

  const pinned = $('.pd-info .pd-head');
  if (pinned && window.matchMedia('(min-width: 961px)').matches) {
    pinned.style.position = 'sticky';
    pinned.style.top = '96px';
    pinned.style.zIndex = '3';
    pinned.style.background = 'var(--c-card)';
  }
})();
