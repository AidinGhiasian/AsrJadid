/* ==========================================================================
   عصرجدید — اسکریپت صفحات سبد خرید، علاقه‌مندی‌ها، مقایسه، تسویه و سفارش‌ها
   داده‌های سبد/علاقه‌مندی/مقایسه در مرورگر (localStorage) نگهداری می‌شود و
   اطلاعات کامل محصولات از سرویس واقعی سرور (/Api/Basket) خوانده می‌شود.
   ========================================================================== */
(function () {
  'use strict';

  const $ = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.prototype.slice.call((c || document).querySelectorAll(s));
  const faDigits = '۰۱۲۳۴۵۶۷۸۹';
  const toFa = (v) => String(v).replace(/\d/g, (d) => faDigits[+d]);
  const toEn = (v) => String(v).replace(/[۰-۹]/g, (d) => faDigits.indexOf(d));
  const TAX_RATE = 0.09;
  const SHIPPING = 1850000;
  const FREE_LIMIT = 50000000;

  /* ---------------- storage ---------------- */
  const store = {
    get(key, def) { try { return JSON.parse(localStorage.getItem('asr_' + key)) || def; } catch (e) { return def; } },
    set(key, val) { try { localStorage.setItem('asr_' + key, JSON.stringify(val)); } catch (e) {} }
  };

  function toast(msg, type) {
    if (typeof window.asrToast === 'function') { window.asrToast(msg, type); return; }
    window.alert(msg);
  }

  function money(n) {
    return toFa(Math.round(n).toLocaleString('en-US'));
  }

  function paintCounts() {
    const cart = store.get('cart', []);
    const wish = store.get('wish', []);
    const compare = store.get('compare', []);
    const cn = cart.reduce((s, i) => s + (+i.qty || 0), 0);

    $$('.js-cart-count').forEach((el) => { el.textContent = toFa(cn); el.hidden = cn === 0; });
    $$('.js-wish-count').forEach((el) => { el.textContent = toFa(wish.length); el.hidden = wish.length === 0; });
    $$('.js-compare-count').forEach((el) => { el.textContent = toFa(compare.length); el.hidden = compare.length === 0; });
    return { cart: cart, wish: wish, compare: compare, cartCount: cn };
  }

  function setCart(cart) { store.set('cart', cart); paintCounts(); }
  function findInCart(cart, id) { return cart.filter((i) => String(i.id) === String(id))[0]; }

  function addToCart(id, qty) {
    const cart = store.get('cart', []);
    const found = findInCart(cart, id);
    if (found) found.qty = (+found.qty || 0) + (qty || 1);
    else cart.push({ id: +id, qty: qty || 1 });
    setCart(cart);
  }

  /* ---------------- server data ---------------- */
  function fetchItems(ids) {
    if (!ids.length) return Promise.resolve([]);
    const url = '/Api/Basket?handler=Items&ids=' + ids.map((i) => toEn(i)).join(',');
    return fetch(url, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
      .then((r) => (r.ok ? r.json() : []))
      .catch(() => []);
  }

  function cardHtml(p) {
    const instock = p.stock > 0;
    return '<article class="card product-card" data-cat="' + (p.categorySlug || '') + '" data-price="' + p.price + '" data-id="' + p.id + '">' +
      '<div class="card-media"><a href="' + p.url + '" class="media-link" aria-label="' + p.name + '">' +
      '<img src="' + p.image + '" alt="' + p.name + '" loading="lazy"></a>' +
      (instock ? '' : '<span class="badge badge-dark">ناموجود</span>') +
      '<div class="card-actions">' +
      '<button class="icon-btn js-compare" type="button" title="افزودن به مقایسه" data-act="compare" data-id="' + p.id + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M7 4v16m0 0-3-3m3 3 3-3M17 20V4m0 0-3 3m3-3 3 3"/></svg></button>' +
      '<button class="icon-btn js-quick" type="button" title="نمایش سریع" data-act="quick" data-id="' + p.id + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6Z"/><circle cx="12" cy="12" r="2.5"/></svg></button>' +
      '</div></div>' +
      '<div class="card-body"><div class="card-meta"><a href="/Category/' + (p.categorySlug || '') + '" class="cat-link">' + (p.category || 'عصرجدید') + '</a>' +
      '<span class="code">کد ' + toFa(p.code) + '</span></div>' +
      '<h3 class="card-title"><a href="' + p.url + '">' + p.name + '</a></h3>' +
      '<p class="card-text">' + (p.color ? 'رنگ: ' + p.color : '') + (p.size ? ' • ابعاد: ' + p.size + ' سانتی‌متر' : '') + '</p>' +
      '<div class="card-rate"><span class="card-stock' + (instock ? '' : ' out') + '">' + (instock ? 'موجود در انبار' : 'ناموجود') + '</span></div></div>' +
      '<div class="card-foot"><div class="price"><strong>' + money(p.price) + '</strong><small>تومان / مترمربع</small></div>' +
      '<button class="btn btn-primary card-buy" type="button" data-act="add" data-id="' + p.id + '"' + (instock ? '' : ' disabled') + '>افزودن به سبد</button>' +
      '</div></article>';
  }

  function quickHtml(p) {
    return '<div style="display:flex;gap:18px;flex-wrap:wrap">' +
      '<img src="' + p.image + '" alt="" style="width:280px;border-radius:14px;object-fit:cover">' +
      '<div style="flex:1;min-width:220px"><h3>' + p.name + '</h3>' +
      '<p class="muted">' + (p.category || '') + ' • رنگ ' + (p.color || '-') + ' • ابعاد ' + (p.size || '-') + ' سانتی‌متر</p>' +
      '<div class="price big"><span class="amount">' + money(p.price) + '</span><span class="cur">تومان</span></div>' +
      '<div class="form-actions" style="margin-top:14px"><a class="btn btn-primary" href="' + p.url + '">مشاهده کامل محصول</a>' +
      '<button class="btn btn-outline" type="button" data-act="add" data-id="' + p.id + '">افزودن به سبد</button></div></div></div>';
  }

  function openQuick(p) {
    const m = $('#quickModal');
    if (!m || !$('#quickBody')) { window.location.href = p.url; return; }
    $('#quickBody').innerHTML = quickHtml(p);
    m.hidden = false;
    document.body.style.overflow = 'hidden';
  }

  /* ---------------- global delegated actions ---------------- */
  document.addEventListener('click', function (e) {
    const btn = e.target.closest('[data-act]');
    const quick = $('#quickModal');

    if (quick && !quick.hidden && (e.target === quick || e.target.closest('.js-modal-close'))) {
      quick.hidden = true;
      document.body.style.overflow = '';
      return;
    }

    if (!btn) return;
    const act = btn.getAttribute('data-act');
    const id = btn.getAttribute('data-id');

    if (act === 'add') {
      e.preventDefault();
      const qtyBox = btn.closest('[data-id]');
      const input = qtyBox ? $('[data-qty] input', qtyBox) : null;
      const qty = input ? (+toEn(input.value) || 1) : 1;
      addToCart(id, qty);
      toast('محصول به سبد خرید اضافه شد (' + toFa(qty) + ' واحد)');
      btn.classList.add('added');
      setTimeout(() => btn.classList.remove('added'), 1200);
      refresh();
    }

    if (act === 'del') {
      e.preventDefault();
      const cart = store.get('cart', []).filter((i) => String(i.id) !== String(id));
      setCart(cart);
      toast('کالا از سبد خرید حذف شد', 'warn');
      refresh();
    }

    if (act === 'inc' || act === 'dec') {
      e.preventDefault();
      const cart = store.get('cart', []);
      const item = findInCart(cart, id);
      if (item) {
        item.qty = Math.max(1, (+item.qty || 1) + (act === 'inc' ? 1 : -1));
        setCart(cart);
        refresh();
      }
    }

    if (act === 'wish-del') {
      e.preventDefault();
      const wish = store.get('wish', []).filter((x) => String(x) !== String(id));
      store.set('wish', wish);
      paintCounts();
      toast('از علاقه‌مندی‌ها حذف شد', 'warn');
      refresh();
    }

    if (act === 'compare') {
      e.preventDefault();
      let cmp = store.get('compare', []);
      if (cmp.map(String).indexOf(String(id)) > -1) cmp = cmp.filter((x) => String(x) !== String(id));
      else if (cmp.length < 4) cmp.push(+id);
      else { toast('حداکثر ۴ محصول قابل مقایسه است', 'warn'); return; }
      store.set('compare', cmp);
      paintCounts();
      toast('لیست مقایسه به‌روزرسانی شد');
      refresh();
    }

    if (act === 'compare-del') {
      e.preventDefault();
      const cmp = store.get('compare', []).filter((x) => String(x) !== String(id));
      store.set('compare', cmp);
      paintCounts();
      refresh();
    }

    if (act === 'quick') {
      e.preventDefault();
      const holder = btn.closest('[data-product]');
      const data = holder ? JSON.parse(holder.getAttribute('data-product')) : null;
      if (data) openQuick(data);
      else window.location.href = '/Product/' + id;
    }

    if (act === 'order-del') {
      e.preventDefault();
      const code = btn.getAttribute('data-code');
      const orders = store.get('orders', []).filter((o) => o.code !== code);
      store.set('orders', orders);
      toast('سفارش از فهرست حذف شد', 'warn');
      refresh();
    }
  });

  /* ---------------- page: cart ---------------- */
  function renderCart() {
    const body = $('#cartBody');
    if (!body) return;

    const cart = store.get('cart', []);
    const ids = cart.map((i) => i.id);

    fetchItems(ids).then(function (items) {
      const alive = cart.filter((c) => items.some((p) => String(p.id) === String(c.id)));

      if (alive.length !== cart.length) setCart(alive);

      if (!items.length) {
        const empty = $('#cartEmpty');
        if (empty) empty.hidden = false;
        const wrap = $('#cartWrap');
        if (wrap) wrap.hidden = true;
        const sub = $('#cartCount');
        if (sub) sub.textContent = 'سبد خرید شما خالی است.';
        paintCounts();
        return;
      }

      let html = '';
      let subtotal = 0;
      let units = 0;

      items.forEach(function (p) {
        const qty = (+(findInCart(alive, p.id) || {}).qty) || 1;
        const row = p.price * qty;
        subtotal += row;
        units += qty;
        html += '<tr>' +
          '<td class="ci-prod"><a href="' + p.url + '" class="ci-media"><img src="' + p.image + '" alt="' + p.name + '"></a>' +
          '<div class="ci-info"><a href="' + p.url + '" class="ci-name">' + p.name + '</a>' +
          '<span class="ci-meta">کد ' + toFa(p.code) + ' • دسته: ' + (p.category || '-') + '</span>' +
          '<span class="ci-meta">' + (p.size || '') + ' سانتی‌متر • رنگ ' + (p.color || '-') + '</span></div></td>' +
          '<td data-label="قیمت واحد">' + money(p.price) + ' تومان</td>' +
          '<td data-label="تعداد"><div class="qty" data-qty>' +
          '<button type="button" class="qty-btn" data-act="dec" data-id="' + p.id + '" aria-label="کاهش"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><path d="M5 12h14"/></svg></button>' +
          '<input type="text" value="' + toFa(qty) + '" aria-label="تعداد" readonly>' +
          '<button type="button" class="qty-btn" data-act="inc" data-id="' + p.id + '" aria-label="افزایش"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg></button>' +
          '</div></td>' +
          '<td data-label="جمع">' + money(row) + ' تومان</td>' +
          '<td><button class="icon-btn sm danger" type="button" data-act="del" data-id="' + p.id + '" aria-label="حذف"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/></svg></button></td>' +
          '</tr>';
      });

      body.innerHTML = html;

      const tax = Math.round(subtotal * TAX_RATE);
      const shipping = subtotal >= FREE_LIMIT ? 0 : SHIPPING;
      const total = subtotal + tax + shipping;

      const setText = (sel, val) => { const el = $(sel); if (el) el.textContent = money(val) + ' تومان'; };
      setText('[data-cart="subtotal"]', subtotal);
      setText('[data-cart="tax"]', tax);
      setText('[data-cart="shipping"]', shipping);
      setText('[data-cart="total"]', total);

      const sub = $('#cartCount');
      if (sub) sub.textContent = toFa(units) + ' قلم کالا در سبد خرید شما';

      const empty = $('#cartEmpty');
      if (empty) empty.hidden = true;
      const wrap = $('#cartWrap');
      if (wrap) wrap.hidden = false;

      // پیشنهاد محصولات
      const grid = $('#cartSuggest');
      if (grid) {
        fetch('/Api/Basket?handler=Suggest&ids=' + ids.join(','))
          .then((r) => (r.ok ? r.json() : []))
          .then((sug) => { if (sug.length) grid.innerHTML = sug.map(cardHtml).join(''); })
          .catch(() => {});
      }
    });
  }

  /* ---------------- page: wishlist ---------------- */
  function renderWishlist() {
    const grid = $('#wishGrid');
    if (!grid) return;

    const wish = store.get('wish', []);

    fetchItems(wish).then(function (items) {
      if (!items.length) {
        grid.innerHTML = '<div class="empty-state"><h3>لیست علاقه‌مندی‌ها خالی است</h3>' +
          '<p class="muted">با زدن آیکن قلب روی هر محصول، آن را برای بررسی بعدی ذخیره کنید.</p>' +
          '<a class="btn btn-primary" href="/Products">مشاهده محصولات</a></div>';
        paintCounts();
        return;
      }

      grid.innerHTML = items.map(function (p) {
        const instock = p.stock > 0;
        return '<article class="card product-card" data-cat="' + (p.categorySlug || '') + '" data-price="' + p.price + '" data-id="' + p.id + '" data-product=\'' + JSON.stringify(p).replace(/'/g, '&#39;') + '\'>' +
          '<div class="card-media"><a href="' + p.url + '" class="media-link"><img src="' + p.image + '" alt="' + p.name + '" loading="lazy"></a>' +
          (instock ? '' : '<span class="badge badge-dark">ناموجود</span>') +
          '<div class="card-actions">' +
          '<button class="icon-btn js-wish" type="button" title="حذف از علاقه‌مندی‌ها" data-act="wish-del" data-id="' + p.id + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20s-7-4.4-7-9.5A4.5 4.5 0 0 1 12 7a4.5 4.5 0 0 1 7 3.5C19 15.6 12 20 12 20Z"/></svg></button>' +
          '<button class="icon-btn js-compare" type="button" title="افزودن به مقایسه" data-act="compare" data-id="' + p.id + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M7 4v16m0 0-3-3m3 3 3-3M17 20V4m0 0-3 3m3-3 3 3"/></svg></button>' +
          '<button class="icon-btn js-quick" type="button" title="نمایش سریع" data-act="quick" data-id="' + p.id + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6Z"/><circle cx="12" cy="12" r="2.5"/></svg></button>' +
          '</div></div>' +
          '<div class="card-body"><div class="card-meta"><a href="/Category/' + (p.categorySlug || '') + '" class="cat-link">' + (p.category || 'عصرجدید') + '</a>' +
          '<span class="code">کد ' + toFa(p.code) + '</span></div>' +
          '<h3 class="card-title"><a href="' + p.url + '">' + p.name + '</a></h3>' +
          '<div class="card-rate"><span class="card-stock' + (instock ? '' : ' out') + '">' + (instock ? 'موجود در انبار' : 'ناموجود') + '</span></div></div>' +
          '<div class="card-foot"><div class="price"><strong>' + money(p.price) + '</strong><small>تومان / مترمربع</small></div>' +
          '<button class="btn btn-primary card-buy" type="button" data-act="add" data-id="' + p.id + '"' + (instock ? '' : ' disabled') + '>افزودن به سبد</button>' +
          '</div></article>';
      }).join('');

      const count = $('#wishCount');
      if (count) count.textContent = toFa(items.length) + ' محصول در علاقه‌مندی‌های شما';
      paintCounts();
    });
  }

  /* ---------------- page: compare ---------------- */
  function renderCompare() {
    const table = $('#compareTable');
    if (!table) return;

    const cmp = store.get('compare', []);
    const empty = $('#compareEmpty');

    fetchItems(cmp).then(function (items) {
      if (!items.length) {
        if (empty) empty.hidden = false;
        table.hidden = true;
        paintCounts();
        return;
      }

      const row = (title, fn) => '<tr><th>' + title + '</th>' + items.map((p) => '<td>' + fn(p) + '</td>').join('') + '</tr>';

      table.hidden = false;
      if (empty) empty.hidden = true;

      table.innerHTML =
        '<thead><tr><th></th>' + items.map((p) =>
          '<td><a href="' + p.url + '" class="ci-media"><img src="' + p.image + '" alt="' + p.name + '" style="width:110px;border-radius:10px"></a>' +
          '<strong style="display:block;margin-top:8px">' + p.name + '</strong>' +
          '<button class="icon-btn sm danger" type="button" data-act="compare-del" data-id="' + p.id + '" aria-label="حذف" style="margin-top:8px"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/></svg></button></td>').join('') + '</tr></thead><tbody>' +
        row('قیمت', (p) => money(p.price) + ' تومان') +
        row('دسته‌بندی', (p) => '<a class="link" href="/Category/' + (p.categorySlug || '') + '">' + (p.category || '-') + '</a>') +
        row('ابعاد (سانتی‌متر)', (p) => p.size || '-') +
        row('وزن (کیلوگرم)', (p) => p.weight || '-') +
        row('رنگ', (p) => p.color || '-') +
        row('موجودی', (p) => p.stock > 0 ? 'موجود (' + toFa(p.stock) + ')' : 'ناموجود') +
        row('کد کالا', (p) => toFa(p.code)) +
        row('', (p) => '<button class="btn btn-primary btn-sm" type="button" data-act="add" data-id="' + p.id + '"' + (p.stock > 0 ? '' : ' disabled') + '>افزودن به سبد</button>') +
        '</tbody>';

      paintCounts();
    });
  }

  /* ---------------- page: checkout ---------------- */
  function orderCode() {
    const d = new Date();
    const pad = (n) => String(n).padStart(2, '0');
    return 'ASR-' + String(d.getFullYear()).slice(2) + pad(d.getMonth() + 1) + pad(d.getDate()) + '-' + String(d.getTime()).slice(-4);
  }

  function renderCheckout() {
    const list = $('#coList');
    if (!list) return;

    const cart = store.get('cart', []);

    fetchItems(cart.map((i) => i.id)).then(function (items) {
      if (!items.length) {
        const empty = $('#coEmpty');
        if (empty) empty.hidden = false;
        const form = $('#coForm');
        if (form) form.hidden = true;
        list.innerHTML = '';
        return;
      }

      let subtotal = 0;
      list.innerHTML = items.map(function (p) {
        const qty = (+(findInCart(cart, p.id) || {}).qty) || 1;
        subtotal += p.price * qty;
        return '<li><span>' + p.name + ' × ' + toFa(qty) + '</span><strong>' + money(p.price * qty) + ' تومان</strong></li>';
      }).join('');

      const tax = Math.round(subtotal * TAX_RATE);
      const shipping = subtotal >= FREE_LIMIT ? 0 : SHIPPING;
      const setText = (sel, val) => { const el = $(sel); if (el) el.textContent = money(val) + ' تومان'; };
      setText('[data-cart="subtotal"]', subtotal);
      setText('[data-cart="tax"]', tax);
      setText('[data-cart="shipping"]', shipping);
      setText('[data-cart="total"]', subtotal + tax + shipping);

      const code = orderCode();
      const codeInput = $('#TrackingCode');
      if (codeInput) codeInput.value = code;

      const form = $('#coForm');
      if (form) {
        form.addEventListener('submit', function () {
          const orders = store.get('orders', []);
          orders.unshift({
            code: code,
            date: new Date().toISOString(),
            total: subtotal + tax + shipping,
            totalText: money(subtotal + tax + shipping),
            status: 'در حال بررسی',
            items: items.map((p) => ({
              id: p.id, name: p.name, image: p.image, url: p.url,
              price: p.price, priceText: money(p.price),
              qty: (+(findInCart(cart, p.id) || {}).qty) || 1,
              size: p.size, color: p.color
            }))
          });
          store.set('orders', orders.slice(0, 30));
          setCart([]);
        });
      }
    });
  }

  /* ---------------- page: orders list ---------------- */
  function renderOrders() {
    const box = $('#ordersBox');
    if (!box) return;

    const orders = store.get('orders', []);

    if (!orders.length) {
      box.innerHTML = '<div class="empty-state"><h3>هنوز سفارشی ثبت نکرده‌اید</h3>' +
        '<p class="muted">پس از ثبت سفارش، وضعیت آن در همین صفحه قابل پیگیری است.</p>' +
        '<a class="btn btn-primary" href="/Products">شروع خرید</a></div>';
      return;
    }

    box.innerHTML = '<div class="table-wrap card"><table class="table"><thead><tr>' +
      '<th>کد سفارش</th><th>تاریخ</th><th>تعداد اقلام</th><th>مبلغ</th><th>وضعیت</th><th></th></tr></thead><tbody>' +
      orders.map(function (o) {
        const date = o.date ? new Date(o.date).toLocaleDateString('fa-IR') : '-';
        return '<tr><td>' + o.code + '</td><td>' + date + '</td><td>' + toFa((o.items || []).length) + ' قلم</td>' +
          '<td>' + (o.totalText || money(o.total || 0)) + ' تومان</td>' +
          '<td><span class="status status-processing">' + (o.status || 'در حال بررسی') + '</span></td>' +
          '<td><a class="btn btn-outline btn-sm" href="/Order?code=' + o.code + '">جزئیات</a> ' +
          '<button class="icon-btn sm danger" type="button" data-act="order-del" data-code="' + o.code + '" aria-label="حذف"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/></svg></button></td></tr>';
      }).join('') + '</tbody></table></div>';
  }

  /* ---------------- page: single order ---------------- */
  function renderOrder() {
    const box = $('#orderBox');
    if (!box) return;

    const code = box.getAttribute('data-code');
    const orders = store.get('orders', []);
    const order = code ? orders.filter((o) => o.code === code)[0] : orders[0];

    if (!order) {
      box.innerHTML = '<div class="empty-state"><h3>سفارش یافت نشد</h3>' +
        '<p class="muted">کد سفارش را کنترل کنید یا از صفحه سفارش‌ها یک سفارش را انتخاب کنید.</p>' +
        '<a class="btn btn-primary" href="/Orders">فهرست سفارش‌های من</a></div>';
      return;
    }

    const date = order.date ? new Date(order.date).toLocaleDateString('fa-IR') : '-';

    box.innerHTML =
      '<div class="grid grid-2"><div class="card"><h3>اطلاعات سفارش</h3>' +
      '<ul class="sum-list"><li><span>کد سفارش</span><strong>' + order.code + '</strong></li>' +
      '<li><span>تاریخ ثبت</span><strong>' + date + '</strong></li>' +
      '<li><span>وضعیت</span><strong>' + (order.status || 'در حال بررسی') + '</strong></li>' +
      '<li><span>تعداد اقلام</span><strong>' + toFa((order.items || []).length) + ' قلم</strong></li></ul>' +
      '<div class="sum-total"><span>مبلغ کل</span><strong>' + (order.totalText || money(order.total || 0)) + ' تومان</strong></div></div>' +
      '<div class="card"><h3>اقلام سفارش</h3><ul class="sum-list">' +
      (order.items || []).map((i) =>
        '<li><span><a class="link" href="' + i.url + '">' + i.name + '</a> × ' + toFa(i.qty) + '</span><strong>' + (i.priceText || money(i.price)) + ' تومان</strong></li>').join('') +
      '</ul><p class="muted" style="margin-top:10px">این سفارش در همین مرورگر ذخیره شده است؛ برای پیگیری رسمی با پشتیبانی تماس بگیرید: ۰۹۱۵۹۸۶۱۲۱۶</p>' +
      '<div class="form-actions"><a class="btn btn-primary" href="/Contact">پیگیری با پشتیبانی</a>' +
      '<a class="btn btn-outline" href="/Orders">سفارش‌های من</a></div></div></div>';
  }

  /* ---------------- page: dashboard ---------------- */
  function renderDashboard() {
    const box = $('#dbRecent');
    if (!box) return;

    const orders = store.get('orders', []);
    const wish = store.get('wish', []);
    const setText = (sel, val) => { const el = $(sel); if (el) el.textContent = toFa(val); };
    setText('#dbOrdersCount', orders.length);
    setText('#dbWishCount', wish.length);

    if (!orders.length) {
      box.innerHTML = '<div class="empty-state"><p class="muted">هنوز سفارشی ثبت نشده است.</p><a class="btn btn-primary btn-sm" href="/Products">مشاهده محصولات</a></div>';
      return;
    }

    box.innerHTML = '<div class="table-wrap"><table class="table table-compact"><thead><tr><th>کد</th><th>تاریخ</th><th>مبلغ</th><th>وضعیت</th><th></th></tr></thead><tbody>' +
      orders.slice(0, 5).map((o) =>
        '<tr><td>' + o.code + '</td><td>' + (o.date ? new Date(o.date).toLocaleDateString('fa-IR') : '-') + '</td>' +
        '<td>' + (o.totalText || money(o.total || 0)) + '</td>' +
        '<td><span class="status status-processing">' + (o.status || 'در حال بررسی') + '</span></td>' +
        '<td><a class="icon-btn sm" href="/Order?code=' + o.code + '" title="جزئیات"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6Z"/><circle cx="12" cy="12" r="2.5"/></svg></a></td></tr>').join('') +
      '</tbody></table></div>';
  }

  /* ---------------- bootstrap ---------------- */
  function refresh() {
    paintCounts();
    renderCart();
    renderWishlist();
    renderCompare();
    renderOrders();
    renderOrder();
    renderDashboard();
  }

  let booted = false;
  function boot() {
    if (booted) return;
    booted = true;
    refresh();
    renderCheckout();
  }

  document.addEventListener('DOMContentLoaded', boot);
  if (document.readyState !== 'loading') boot();

  window.AsrBasket = { store: store, paintCounts: paintCounts, addToCart: addToCart, money: money, toFa: toFa };
})();
