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

  /* ---------------- slug + counters + charts ---------------- */
  const map = { 'ا': 'a', 'آ': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ث': 's', 'ج': 'j', 'چ': 'ch', 'ح': 'h', 'خ': 'kh', 'د': 'd', 'ذ': 'z', 'ر': 'r', 'ز': 'z', 'ژ': 'zh', 'س': 's', 'ش': 'sh', 'ص': 's', 'ض': 'z', 'ط': 't', 'ظ': 'z', 'ع': 'a', 'غ': 'gh', 'ف': 'f', 'ق': 'gh', 'ک': 'k', 'ك': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n', 'و': 'v', 'ه': 'h', 'ی': 'y', 'ي': 'y', ' ': '-', '‌': '-' };
  const slugSrc = $('.js-slug-src'), slugOut = $('.js-slug-out');
  if (slugSrc && slugOut) slugSrc.addEventListener('input', () => {
    slugOut.value = slugSrc.value.split('').map((ch) => map[ch] !== undefined ? map[ch] : ch)
      .join('').toLowerCase().replace(/[^a-z0-9-]/g, '').replace(/-+/g, '-');
  });

  $$('.adm-stat .as-value').forEach((el) => {
    const raw = el.textContent.trim();
    const num = parseFloat(raw.replace(/[^\d.]/g, ''));
    if (!isFinite(num) || num <= 0) return;
    el.style.opacity = '0';
    let cur = 0;
    const step = Math.max(1, Math.round(num / 40));
    const t = setInterval(() => {
      cur += step;
      if (cur >= num) { cur = num; clearInterval(t); }
      el.style.opacity = '1';
      el.innerHTML = toFa(Math.round(cur).toLocaleString('en-US').replace(/,/g, '٫')) +
        (raw.replace(/[\d.,٫]/g, '').trim() ? ' <small>' + raw.replace(/[\d.,٫]/g, '').trim() + '</small>' : '');
    }, 26);
  });

  const bars = $$('.bar-chart .bar-col i');
  if (bars.length) bars.forEach((b, i) => {
    const h = b.style.height;
    b.style.height = '0';
    setTimeout(() => { b.style.height = h; }, 120 + i * 70);
  });

  /* ---------------- demo actions ---------------- */
  const loginForm = $('.js-adm-login');
  if (loginForm) loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const user = ($('input[type=text]', loginForm).value || '').trim();
    const pass = $('input[type=password]', loginForm).value;
    if (user.toLowerCase() !== (loginForm.getAttribute('data-demo-user') || 'admin') || pass !== (loginForm.getAttribute('data-demo-pass') || 'admin123')) {
      toast('نام کاربری یا رمز عبور نادرست است', 'err');
      return;
    }
    toast('خوش آمدید! در حال انتقال به داشبورد…');
    setTimeout(() => { window.location.href = 'dashboard.html'; }, 900);
  });

  $$('.js-adm-form').forEach((form) => form.addEventListener('submit', (e) => {
    e.preventDefault();
    let bad = null;
    $$('[required]', form).forEach((f) => {
      const empty = !String(f.value || '').trim();
      f.classList.toggle('error', empty);
      if (empty && !bad) bad = f;
    });
    if (bad) { toast('فیلدهای الزامی را تکمیل کنید', 'err'); bad.focus(); return; }
    toast('تغییرات با موفقیت ذخیره شد');
  }));

  $$('[type=button]').forEach((b) => {
    const t = (b.textContent || '').trim();
    if (/خروجی|دانلود|Excel|چاپ/.test(t) && !b.classList.contains('js-print')) {
      b.addEventListener('click', () => toast('فایل خروجی آماده دانلود شد (نسخه نمایشی)'));
    }
    if (/اعمال فیلتر|فیلتر/.test(t)) b.addEventListener('click', () => toast('فیلتر اعمال شد'));
    if (/پشتیبان|بازگردانی/.test(t)) b.addEventListener('click', () => toast('عملیات پشتیبان‌گیری در صف اجرا قرار گرفت'));
  });
})();
