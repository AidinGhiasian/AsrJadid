/* ==========================================================================
   عصرجدید — اسکریپت پنل مدیریت (بدون کتابخانه خارجی)
   ========================================================================== */
(function () {
  'use strict';

  const $ = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.prototype.slice.call((c || document).querySelectorAll(s));
  const faDigits = '۰۱۲۳۴۵۶۷۸۹';
  const toFa = (v) => String(v).replace(/\d/g, (d) => faDigits[+d]);

  function toast(msg, type) {
    const wrap = $('#toastWrap');
    if (!wrap) return;
    const el = document.createElement('div');
    el.className = 'toast ' + (type || 'ok');
    el.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' +
      (type === 'err' ? '<circle cx="12" cy="12" r="9"/><path d="m9 9 6 6M15 9l-6 6"/>' : '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>') +
      '</svg><span>' + msg + '</span>';
    wrap.appendChild(el);
    setTimeout(() => { el.style.opacity = '0'; el.style.transform = 'translateY(10px)'; }, 2600);
    setTimeout(() => el.remove(), 3000);
  }

  /* ---------------- sidebar ---------------- */
  const side = $('#admSide');
  $$('.js-adm-side').forEach((b) => b.addEventListener('click', () => side && side.classList.toggle('open')));
  $$('.js-adm-side-close').forEach((b) => b.addEventListener('click', () => side && side.classList.remove('open')));
  document.addEventListener('click', (e) => {
    if (side && side.classList.contains('open') && !side.contains(e.target) && !e.target.closest('.js-adm-side')) {
      side.classList.remove('open');
    }
  });

  /* ---------------- dark mode ---------------- */
  const themeBtn = $('.js-theme-toggle');
  if (themeBtn) {
    try { if (localStorage.getItem('asr_admin_dark') === '1') document.body.classList.add('dark'); } catch (e) {}
    themeBtn.addEventListener('click', () => {
      document.body.classList.toggle('dark');
      const dark = document.body.classList.contains('dark');
      try { localStorage.setItem('asr_admin_dark', dark ? '1' : '0'); } catch (e) {}
      toast(dark ? 'حالت تیره فعال شد' : 'حالت روشن فعال شد');
    });
  }

  /* ---------------- tables: search & bulk ---------------- */
  function filterTables(q) {
    q = (q || '').trim().toLowerCase();
    $$('.adm-table tbody tr').forEach((tr) => {
      if (!q) { tr.style.display = ''; return; }
      tr.style.display = tr.textContent.toLowerCase().indexOf(q) > -1 ? '' : 'none';
    });
  }
  const headerSearch = $('.js-admin-search');
  if (headerSearch) headerSearch.addEventListener('input', () => filterTables(headerSearch.value));
  $$('.js-admin-search').forEach((inp) => {
    if (inp === headerSearch) return;
    inp.addEventListener('input', () => filterTables(inp.value));
  });

  $$('.js-check-all').forEach((cb) => cb.addEventListener('change', () => {
    const table = cb.closest('table');
    $$('tbody input[type=checkbox]', table).forEach((i) => { i.checked = cb.checked; });
  }));

  /* ---------------- admin tabs ---------------- */
  $$('.js-adm-tabs').forEach((box) => {
    const heads = $$('.tab-btn', box);
    heads.forEach((h) => h.addEventListener('click', (e) => {
      const href = h.getAttribute('href') || '';
      if (href.charAt(0) === '#') e.preventDefault();
      heads.forEach((x) => x.classList.remove('active'));
      h.classList.add('active');
      const id = h.getAttribute('data-tab');
      $$('.tab-panel', box).forEach((p) => p.classList.toggle('active', p.id === id));
    }));
  });

  /* ---------------- modal ---------------- */
  function openModal(html) {
    const m = $('#admModal');
    if (!m) return;
    $('#admModalBody').innerHTML = html;
    m.hidden = false;
    document.body.style.overflow = 'hidden';
  }
  function closeModal() {
    const m = $('#admModal');
    if (!m) return;
    m.hidden = true;
    document.body.style.overflow = '';
    const t = $('#admModalBody');
    if (t) t.innerHTML = '';
  }
  $$('.js-modal-close').forEach((b) => b.addEventListener('click', closeModal));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });

  const MODALS = {
    order: '<h3>جزئیات سفارش</h3>' +
      '<ul class="kv-list">' +
      '<li><span>کد سفارش</span><strong>AJ-14040701-311</strong></li>' +
      '<li><span>مشتری</span><strong>شرکت آبان سازه</strong></li>' +
      '<li><span>تاریخ ثبت</span><strong>۱۴۰۴/۰۷/۰۱ – ۱۰:۲۴</strong></li>' +
      '<li><span>مبلغ کل</span><strong>۶۲٬۳۰۰٬۰۰۰ تومان</strong></li>' +
      '<li><span>شیوه ارسال</span><strong>باربری تخصصی – بارنامه ۹۸۴۵۱-۲۲۳</strong></li>' +
      '<li><span>وضعیت پرداخت</span><strong>در انتظار پرداخت (پیش‌فاکتور صادر شده)</strong></li></ul>' +
      '<div class="modal-actions"><button class="btn btn-outline" type="button">چاپ فاکتور</button>' +
      '<button class="btn btn-primary" type="button">تأیید پرداخت و شروع آماده‌سازی</button></div>',
    category: '<h3>افزودن دسته‌بندی جدید</h3><form class="adm-form" novalidate>' +
      '<div class="field"><label>نام دسته‌بندی</label><input type="text" placeholder="مثلاً: صفحات کوارتز"></div>' +
      '<div class="field"><label>نشانی صفحه (Slug)</label><input type="text" placeholder="quartz"></div>' +
      '<div class="field"><label>توضیح کوتاه</label><textarea rows="3"></textarea></div>' +
      '<div class="modal-actions"><button class="btn btn-outline js-modal-close" type="button">انصراف</button>' +
      '<button class="btn btn-primary" type="submit">ذخیره دسته‌بندی</button></div></form>',
    customer: '<h3>افزودن کاربر جدید</h3><form class="adm-form" novalidate>' +
      '<div class="field"><label>نام و نام خانوادگی</label><input type="text" required></div>' +
      '<div class="field"><label>شماره همراه</label><input type="tel" required></div>' +
      '<div class="field"><label>نقش کاربری</label><select><option>مشتری</option><option>مشتری سازمانی</option><option>مدیر فروش</option><option>پشتیبانی</option><option>مدیر سیستم</option></select></div>' +
      '<label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>ارسال پیامک خوش‌آمدگویی و اطلاعات ورود</span></label>' +
      '<div class="modal-actions"><button class="btn btn-outline js-modal-close" type="button">انصراف</button>' +
      '<button class="btn btn-primary" type="submit">ایجاد کاربر</button></div></form>',
    reply: '<h3>پاسخ به دیدگاه</h3><form class="adm-form" novalidate>' +
      '<div class="field"><label>دیدگاه</label><input type="text" value="سارا ح. — نانوسنگ نمای تراورتن کرم" readonly></div>' +
      '<div class="field"><label>متن پاسخ</label><textarea rows="4" placeholder="پاسخ کارشناس عصرجدید…"></textarea></div>' +
      '<label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>ثبت به‌عنوان پاسخ رسمی کارشناس</span></label>' +
      '<div class="modal-actions"><button class="btn btn-ghost js-modal-close" type="button">انصراف</button>' +
      '<button class="btn btn-primary" type="submit">ارسال پاسخ</button></div></form>',
    role: '<h3>ایجاد نقش جدید</h3><form class="adm-form" novalidate>' +
      '<div class="field"><label>نام نقش</label><input type="text" placeholder="مثلاً: کارشناس فروش شهرستان"></div>' +
      '<div class="field"><label>توضیح</label><input type="text" placeholder="شرح مختصر وظایف این نقش"></div>' +
      [['مدیریت محصولات', true], ['مدیریت سفارش‌ها', true], ['مدیریت مشتریان', false], ['گزارش‌های مالی', false], ['تنظیمات سایت', false]]
        .map(([n, c]) => '<label class="switch-row"><input type="checkbox" ' + (c ? 'checked' : '') + '><span class="switch"></span><span>' + n + '</span></label>').join('') +
      '<div class="modal-actions"><button class="btn btn-outline js-modal-close" type="button">انصراف</button>' +
      '<button class="btn btn-primary" type="submit">ذخیره نقش</button></div></form>'
  };

  $$('.js-modal-btn').forEach((btn) => btn.addEventListener('click', (e) => {
    const kind = btn.getAttribute('data-modal');
    if (!kind) return;
    e.preventDefault();
    openModal(MODALS[kind] || '<h3>اطلاعات</h3><p class="muted">این بخش در نسخه نهایی به داده واقعی متصل می‌شود.</p>');
  }));

  /* confirm delete */
  $$('.js-confirm').forEach((btn) => btn.addEventListener('click', () => {
    const name = btn.getAttribute('data-name') || 'این مورد';
    openModal('<h3>تأیید حذف</h3><p>آیا از حذف <strong>' + name + '</strong> مطمئن هستید؟ این عملیات قابل بازگشت نیست.</p>' +
      '<div class="modal-actions"><button class="btn btn-outline" type="button" id="cmNo">انصراف</button>' +
      '<button class="btn btn-primary" type="button" id="cmYes" style="background:var(--c-danger)">حذف کن</button></div>');
    const yes = $('#cmYes');
    if (yes) yes.addEventListener('click', () => {
      closeModal();
      const row = btn.closest('tr');
      if (row) { row.style.transition = 'opacity .3s'; row.style.opacity = '0'; setTimeout(() => row.remove(), 300); }
      toast('«' + name + '» حذف شد', 'warn');
    });
    const no = $('#cmNo');
    if (no) no.addEventListener('click', closeModal);
  }));

  /* ---------------- uploads ---------------- */
  $$('.js-upload').forEach((box) => {
    const input = $('input[type=file]', box) || box.parentNode.querySelector('input[type=file]');
    box.addEventListener('click', () => input && input.click());
    box.addEventListener('dragover', (e) => { e.preventDefault(); box.classList.add('drag'); });
    box.addEventListener('dragleave', () => box.classList.remove('drag'));
    const preview = (file) => {
      if (!file || file.type.indexOf('image') !== 0) return;
      const img = $('img', box);
      const url = URL.createObjectURL(file);
      if (img) img.src = url;
      else {
        const im = document.createElement('img');
        im.src = url; im.alt = 'پیش‌نمایش';
        box.insertBefore(im, box.firstChild);
      }
      toast('تصویر «' + file.name + '» بارگذاری شد');
    };
    box.addEventListener('drop', (e) => { e.preventDefault(); box.classList.remove('drag'); preview(e.dataTransfer.files[0]); });
    if (input) input.addEventListener('change', () => preview(input.files[0]));
  });

  /* ---------------- slug ---------------- */
  const map = { 'ا': 'a', 'آ': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ث': 's', 'ج': 'j', 'چ': 'ch', 'ح': 'h', 'خ': 'kh', 'د': 'd', 'ذ': 'z', 'ر': 'r', 'ز': 'z', 'ژ': 'zh', 'س': 's', 'ش': 'sh', 'ص': 's', 'ض': 'z', 'ط': 't', 'ظ': 'z', 'ع': 'a', 'غ': 'gh', 'ف': 'f', 'ق': 'gh', 'ک': 'k', 'ك': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n', 'و': 'v', 'ه': 'h', 'ی': 'y', 'ي': 'y', ' ': '-', '‌': '-' };
  const slugSrc = $('.js-slug-src'), slugOut = $('.js-slug-out');
  if (slugSrc && slugOut) slugSrc.addEventListener('input', () => {
    slugOut.value = slugSrc.value.split('').map((ch) => map[ch] !== undefined ? map[ch] : ch)
      .join('').toLowerCase().replace(/[^a-z0-9-]/g, '').replace(/-+/g, '-');
  });

  /* ---------------- KPI counters ---------------- */
  const toEnDigits = (v) => String(v)
    .replace(/[۰-۹]/g, (d) => String('۰۱۲۳۴۵۶۷۸۹'.indexOf(d)))
    .replace(/[٠-٩]/g, (d) => String('٠١٢٣٤٥٦٧٨٩'.indexOf(d)));
  $$('.kpi-value').forEach((el) => {
    const node = el.childNodes[0];
    if (!node) return;
    const raw = toEnDigits((node.textContent || '').trim()).replace(/[٬،,\s]/g, '');
    const num = parseFloat(raw.replace(/[^\d.]/g, ''));
    if (!isFinite(num) || num < 1) return;
    const suffix = raw.replace(/[\d.,٫]/g, '');
    let cur = 0;
    const step = Math.max(1, Math.round(num / 40));
    const t = setInterval(() => {
      cur += step;
      if (cur >= num) { cur = num; clearInterval(t); }
      node.textContent = toFa(Math.round(cur).toLocaleString('en-US').replace(/,/g, '٫')) + suffix;
    }, 26);
  });

  /* ---------------- SVG line chart ---------------- */
  const lineSvg = $('.js-line-chart');
  if (lineSvg) {
    const pts = (lineSvg.getAttribute('data-points') || '').split(',').map(Number).filter((n) => !isNaN(n));
    const labels = (lineSvg.getAttribute('data-labels') || '').split('،');
    const unit = lineSvg.getAttribute('data-unit') || '';
    const W = 720, H = 250, padX = 40, padY = 28;
    const max = Math.max.apply(null, pts) * 1.15;
    const min = 0;
    const stepX = (W - padX * 2) / (pts.length - 1);
    const y = (v) => H - padY - ((v - min) / (max - min)) * (H - padY * 2);
    const coords = pts.map((v, i) => [padX + i * stepX, y(v)]);
    const line = coords.map((c, i) => (i ? 'L' : 'M') + c[0].toFixed(1) + ' ' + c[1].toFixed(1)).join(' ');
    const area = line + ' L' + coords[coords.length - 1][0].toFixed(1) + ' ' + (H - padY) + ' L' + coords[0][0].toFixed(1) + ' ' + (H - padY) + ' Z';
    const avg = pts.reduce((a, b) => a + b, 0) / pts.length;
    let html = '<defs><linearGradient id="chartFill" x1="0" y1="0" x2="0" y2="1">' +
      '<stop offset="0%" stop-color="var(--brand)" stop-opacity=".22"/>' +
      '<stop offset="100%" stop-color="var(--brand)" stop-opacity="0"/></linearGradient></defs>';
    for (let g = 0; g <= 4; g++) {
      const gy = padY + ((H - padY * 2) / 4) * g;
      const val = Math.round(max - (max / 4) * g);
      html += '<line class="grid-line" x1="' + padX + '" y1="' + gy + '" x2="' + (W - padX) + '" y2="' + gy + '"/>' +
        '<text class="axis-label" x="' + (padX - 8) + '" y="' + (gy + 4) + '" text-anchor="end">' + toFa(val) + '</text>';
    }
    html += '<line class="grid-line" style="stroke-dasharray:4 4" x1="' + padX + '" y1="' + y(avg).toFixed(1) + '" x2="' + (W - padX) + '" y2="' + y(avg).toFixed(1) + '"/>';
    html += '<path class="area" d="' + area + '"/><path class="line" d="' + line + '"/>';
    coords.forEach((c, i) => {
      html += '<circle class="dot" cx="' + c[0].toFixed(1) + '" cy="' + c[1].toFixed(1) + '" r="4"><title>' +
        (labels[i] || '') + ': ' + toFa(pts[i]) + ' ' + unit + '</title></circle>';
      html += '<text class="axis-label" x="' + c[0].toFixed(1) + '" y="' + (H - 8) + '" text-anchor="middle">' + (labels[i] || '') + '</text>';
    });
    lineSvg.innerHTML = html;
  }

  /* ---------------- SVG donut ---------------- */
  const donut = $('.js-donut');
  if (donut) {
    const vals = (donut.getAttribute('data-values') || '').split(',').map(Number).filter((n) => !isNaN(n));
    const cols = (donut.getAttribute('data-colors') || '').split(',');
    const r = 46, C = 2 * Math.PI * r;
    let total = vals.reduce((a, b) => a + b, 0) || 1;
    let offset = 0, html = '<circle cx="60" cy="60" r="' + r + '" stroke="var(--line)" stroke-linecap="butt" transform="rotate(-90 60 60)"></circle>';
    vals.forEach((v, i) => {
      const len = (v / total) * C;
      html += '<circle cx="60" cy="60" r="' + r + '" stroke="' + (cols[i] || 'var(--brand)') + '"' +
        ' stroke-dasharray="' + Math.max(0, len - 3).toFixed(1) + ' ' + (C - Math.max(0, len - 3)).toFixed(1) + '"' +
        ' stroke-dashoffset="' + (-offset).toFixed(1) + '" stroke-linecap="butt" transform="rotate(-90 60 60)"><title>' +
        toFa(v) + '٪</title></circle>';
      offset += len;
    });
    donut.innerHTML = html;
  }

  /* ---------------- bar chart (fallback) ---------------- */
  const bars = $$('.bar-chart .bar-col i');
  if (bars.length) bars.forEach((b, i) => {
    const h = b.style.height;
    b.style.height = '0';
    setTimeout(() => { b.style.height = h; }, 120 + i * 70);
  });

})();
