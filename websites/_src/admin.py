# -*- coding: utf-8 -*-
"""صفحات پنل مدیریت عصرجدید — طراحی ساده و شکیل"""
from data import *
from layouts import icon, cat_name, sprite

STATUS_CLASS = {"pending": "warn", "processing": "info", "shipping": "info", "done": "ok", "canceled": "danger"}


def kpis():
    return '<div class="admin-kpis">' + "".join(
        f'''<article class="kpi">
      <div class="kpi-top"><span class="kpi-ico">{icon(c['icon'])}</span>
        <span class="kpi-delta {'up' if c['up'] else 'down'}">{icon("trend-up" if c['up'] else "trend-down")} {c['delta']}</span></div>
      <span class="kpi-title">{c['title']}</span>
      <div class="kpi-value">{c['value']}<small>{c['unit']}</small></div>
    </article>''' for c in ADMIN["dashboard_cards"]) + "</div>"


def line_chart():
    """نمودار فروش — SVG که با جاوااسکریپت از data-* رسم می‌شود"""
    points = ",".join(str(b["value"]) for b in ADMIN["sales_chart"])
    labels = "،".join(b["label"] for b in ADMIN["sales_chart"])
    return f'''<div class="chart-wrap">
  <svg class="chart-svg js-line-chart" data-points="{points}" data-labels="{labels}" data-unit="میلیون تومان"
       viewBox="0 0 720 250" role="img" aria-label="نمودار فروش ماهانه"></svg>
  <div class="chart-legend"><span><i></i> فروش ماهانه (میلیون تومان)</span><span><i class="alt"></i> میانگین دوره</span></div>
</div>'''


def donut_chart():
    values = ",".join(str(r["pct"]) for r in ADMIN["reports"])
    colors = ",".join(r["color"] for r in ADMIN["reports"])
    legend = "".join(f'<li><span class="dot" style="--c:{r["color"]}"></span><span>{r["label"]}</span>'
                     f'<strong>{fa_num(r["pct"])}٪</strong></li>' for r in ADMIN["reports"])
    return f'''<div class="donut-simple">
  <div class="donut-wrap-s">
    <svg class="donut-svg js-donut" data-values="{values}" data-colors="{colors}" viewBox="0 0 120 120" role="img" aria-label="سهم گروه محصولات">
      <circle cx="60" cy="60" r="46" stroke="var(--line)"></circle>
    </svg>
    <span class="donut-hole"><strong>۱۰۰٪</strong><small>کل فروش</small></span>
  </div>
  <ul class="donut-legend">{legend}</ul>
</div>'''


def dashboard(t):
    orders = "".join(f'''<tr>
      <td><a class="link" href="orders.html">{o['code']}</a></td><td>{o['customer']}</td><td>{o['date']}</td>
      <td>{money(o['total'])}</td>
      <td><span class="status status-{o['key']}">{o['status']}</span></td></tr>''' for o in ADMIN["orders"][:5])
    tops = "".join(f'''<li><span class="rank-num">{fa_num(i + 1)}</span>
      <span class="li-main"><p>{p['name']}</p><small>{fa_num(p['sold'])} فروش</small></span>
      <span class="mini-bar"><b style="width:{p['share']}%"></b></span>
      <span class="li-value">{money(p['revenue'])}</span></li>''' for i, p in enumerate(ADMIN["top_products"][:4]))
    acts = "".join(f'''<li><span class="li-ico">{icon(a['icon'])}</span>
      <span class="li-main"><p>{a['text']}</p><small>{a['time']}</small></span></li>''' for a in ADMIN["activities"][:4])
    stock = "".join(f'''<li><span class="li-main"><p>{n}</p></span>
      <span class="mini-bar"><b style="width:{w}%;{ 'background:var(--warn)' if w < 30 else '' }"></b></span>
      <small>{v}</small></li>''' for n, w, v in [
        ("نانوسنگ نمای تراورتن کرم", 88, "۲٬۴۰۰ مترمربع"),
        ("آجرنما نسوز تراکوتا", 96, "۵٬۲۰۰ مترمربع"),
        ("صفحه کوارتز سفید برفی", 52, "۱٬۲۴۰ مترمربع"),
        ("سینک کورین یکپارچه", 18, "۱۴۵ عدد"),
    ])
    return f'''
<div class="adm-page-head">
  <div class="adm-page-title"><h2>خلاصه وضعیت فروشگاه</h2><p>آخرین به‌روزرسانی: امروز ۱۴۰۴/۰۷/۰۲ – ۰۹:۱۵</p></div>
  <div class="adm-page-actions">
    <a class="btn btn-outline btn-sm" href="orders.html">{icon("chart")} گزارش کامل</a>
    <a class="btn btn-primary btn-sm" href="product-form.html">{icon("plus")} محصول جدید</a>
  </div>
</div>
{kpis()}
<div class="adm-grid-2-1">
  <div class="adm-card">
    <div class="adm-card-head">
      <div><h3>فروش ماهانه</h3><p>مجموع فروش هشت ماه گذشته</p></div>
      <div class="adm-card-tools"><button class="chip-btn active" type="button">۱۴۰۴</button><button class="chip-btn" type="button">۱۴۰۳</button></div>
    </div>
    {line_chart()}
  </div>
  <div class="adm-card">
    <div class="adm-card-head"><div><h3>سهم گروه محصولات</h3><p>سه ماه گذشته</p></div></div>
    {donut_chart()}
  </div>
</div>
<div class="adm-card">
  <div class="adm-card-head">
    <div><h3>سفارش‌های اخیر</h3><p>پنج سفارش آخر فروشگاه</p></div>
    <a class="adm-link" href="orders.html">همه سفارش‌ها {icon("arrow-left")}</a>
  </div>
  <div class="table-wrap"><table class="adm-table">
    <thead><tr><th>کد سفارش</th><th>مشتری</th><th>تاریخ</th><th>مبلغ</th><th>وضعیت</th></tr></thead>
    <tbody>{orders}</tbody></table></div>
</div>
<div class="adm-grid-2">
  <div class="adm-card">
    <div class="adm-card-head"><div><h3>پرفروش‌ترین محصولات</h3></div>
      <a class="adm-link" href="products.html">مدیریت {icon("arrow-left")}</a></div>
    <ul class="adm-list rank-list">{tops}</ul>
  </div>
  <div class="adm-card">
    <div class="adm-card-head"><div><h3>آخرین رویدادها</h3></div></div>
    <ul class="adm-list">{acts}</ul>
  </div>
</div>
<div class="adm-grid-2">
  <div class="adm-card">
    <div class="adm-card-head"><div><h3>وضعیت انبار</h3><p>محصولات نیازمند توجه</p></div>
      <a class="adm-link" href="products.html">انبار {icon("arrow-left")}</a></div>
    <ul class="adm-list stock-list">{stock}</ul>
  </div>
  <div class="adm-card">
    <h3>دسترسی سریع</h3>
    <div class="adm-quick">
      <a href="product-form.html">{icon("plus")} افزودن محصول جدید</a>
      <a href="orders.html">{icon("cart")} بررسی سفارش‌های در انتظار</a>
      <a href="comments.html">{icon("message")} تأیید دیدگاه‌های جدید</a>
      <a href="settings.html">{icon("settings")} تنظیمات فروشگاه</a>
    </div>
    <div class="report-tiles" style="margin-top:16px">
      <a href="orders.html">{icon("chart")}<strong>گزارش فروش</strong><small>خروجی Excel</small></a>
      <a href="customers.html">{icon("users")}<strong>مشتریان</strong><small>۱٬۲۴۸ نفر</small></a>
    </div>
  </div>
</div>'''


def products(t):
    rows = ""
    for s in STONES:
        cls = "ok" if s["stock"] > 500 else ("warn" if s["stock"] > 100 else "danger")
        rows += f'''<tr>
      <td class="check-cell"><input type="checkbox" aria-label="انتخاب"></td>
      <td class="adm-prod"><img src="../assets/images/{s['image']}" alt="{s['name']}">
        <div><a class="link" href="product-form.html">{s['name']}</a><small>کد {s['code']}</small></div></td>
      <td>{cat_name(s['cat'])}</td>
      <td>{fa_num(s['price'])}</td>
      <td><span class="stock-pill {cls}">{fa_num(s['stock'])} {s['unit']}</span></td>
      <td>{'<span class="status status-ok">منتشرشده</span>' if s['featured'] else '<span class="status status-info">عادی</span>'}</td>
      <td class="row-actions">
        <a class="icon-btn sm" href="product-form.html" title="ویرایش">{icon("edit")}</a>
        <button class="icon-btn sm danger js-confirm" type="button" data-name="{s['name']}" title="حذف">{icon("trash")}</button>
      </td></tr>'''
    return f'''
<div class="adm-page-head">
  <div class="adm-filters">
    <div class="adm-searchbox">{icon("search")}<input type="search" placeholder="جستجوی نام یا کد محصول…" class="js-admin-search" aria-label="جستجو"></div>
    <select class="adm-select" aria-label="دسته‌بندی"><option>همه دسته‌ها</option>{''.join(f'<option>{c["name"]}</option>' for c in CATEGORIES)}</select>
  </div>
  <div class="adm-page-actions">
    <button class="btn btn-outline btn-sm" type="button">{icon("download")} خروجی Excel</button>
    <a class="btn btn-primary btn-sm" href="product-form.html">{icon("plus")} افزودن محصول</a>
  </div>
</div>
<div class="adm-card">
  <div class="adm-card-head">
    <div><h3>لیست محصولات</h3><p>{fa_num(len(STONES))} محصول از ۱۶۱ محصول</p></div>
    <div class="adm-bulk"><span>عملیات گروهی:</span>
      <button class="btn btn-ghost btn-sm" type="button">انتشار</button>
      <button class="btn btn-ghost btn-sm" type="button">حذف</button></div>
  </div>
  <div class="table-wrap"><table class="adm-table">
    <thead><tr><th class="check-cell"><input type="checkbox" class="js-check-all" aria-label="انتخاب همه"></th>
      <th>محصول</th><th>دسته‌بندی</th><th>قیمت (تومان)</th><th>موجودی</th><th>وضعیت</th><th></th></tr></thead>
    <tbody>{rows}</tbody></table></div>
  <div class="adm-pagination"><span>نمایش ۱ تا ۱۲ از ۱۶۱ محصول</span>
    <div class="pager"><button class="chip-btn active" type="button">۱</button>
      <button class="chip-btn" type="button">۲</button><button class="chip-btn" type="button">۳</button>
      <button class="chip-btn" type="button">{fa_num(14)}</button></div></div>
</div>'''


def product_form(t):
    return f'''
<form class="adm-form js-adm-form" novalidate>
  <div class="adm-page-head">
    <div class="adm-page-title"><h2>افزودن محصول جدید</h2><p>فیلدهای ستاره‌دار الزامی هستند.</p></div>
    <div class="adm-page-actions">
      <a class="btn btn-ghost btn-sm" href="products.html">انصراف</a>
      <button class="btn btn-outline btn-sm" type="button">{icon("save")} پیش‌نویس</button>
      <button class="btn btn-primary btn-sm" type="submit">{icon("check")} انتشار</button>
    </div>
  </div>
  <div class="adm-form-layout">
    <div class="adm-form-main">
      <div class="adm-card">
        <h3>اطلاعات پایه</h3>
        <div class="adm-form-grid">
          <div class="field"><label>نام محصول <span class="req">*</span></label><input type="text" class="js-slug-src" placeholder="مثلاً: نانوسنگ نمای تراورتن کرم" required></div>
          <div class="field"><label>کد محصول <span class="req">*</span></label><input type="text" placeholder="NS-311" required></div>
          <div class="field"><label>نشانی صفحه (Slug)</label><input type="text" class="js-slug-out" placeholder="nanosang-tavartun-krem"></div>
          <div class="field"><label>دسته‌بندی <span class="req">*</span></label><select required><option value="">انتخاب کنید…</option>{''.join(f'<option>{c["name"]}</option>' for c in CATEGORIES)}</select></div>
          <div class="field full"><label>توضیح کوتاه</label><textarea rows="2" placeholder="حداکثر ۱۴۰ کاراکتر، نمایش در کارت محصول"></textarea></div>
          <div class="field full"><label>توضیحات کامل</label><textarea rows="6" placeholder="ویژگی‌ها، کاربردها و نکات فنی…"></textarea></div>
        </div>
      </div>
      <div class="adm-card">
        <h3>قیمت و موجودی</h3>
        <div class="adm-form-grid">
          <div class="field"><label>قیمت واحد (تومان) <span class="req">*</span></label><input type="text" placeholder="۶۸۰٬۰۰۰" required></div>
          <div class="field"><label>قیمت پیش از تخفیف</label><input type="text" placeholder="۷۸۰٬۰۰۰"></div>
          <div class="field"><label>واحد فروش</label><select><option>مترمربع</option><option>متر طول</option><option>عدد</option></select></div>
          <div class="field"><label>موجودی انبار <span class="req">*</span></label><input type="text" placeholder="۲۴۰۰" required></div>
          <div class="field"><label>حد هشدار موجودی</label><input type="text" placeholder="۲۰۰"></div>
          <div class="field"><label>وضعیت انتشار</label><select><option>منتشرشده</option><option>پیش‌نویس</option><option>ناموجود</option></select></div>
        </div>
      </div>
      <div class="adm-card">
        <div class="adm-card-head"><div><h3>مشخصات فنی</h3><p>ابعاد، ضخامت، وزن و سایر مشخصه‌ها</p></div>
          <button class="btn btn-ghost btn-sm" type="button">{icon("plus")} افزودن مشخصه</button></div>
        <div class="adm-form-grid">
          <div class="field"><label>ابعاد صفحه</label><input type="text" placeholder="۶۰ × ۱۲۰ سانتی‌متر"></div>
          <div class="field"><label>ضخامت</label><input type="text" placeholder="۲ سانتی‌متر"></div>
          <div class="field"><label>وزن</label><input type="text" placeholder="۴۵ کیلوگرم بر مترمربع"></div>
          <div class="field"><label>رنگ</label><input type="text" placeholder="کرم"></div>
        </div>
        <div class="table-wrap"><table class="adm-table adm-table-input">
          <thead><tr><th>عنوان مشخصه</th><th>مقدار</th><th class="check-cell"></th></tr></thead>
          <tbody>
            <tr><td><input type="text" value="جذب آب"></td><td><input type="text" value="کمتر از ۱٪"></td><td class="check-cell"><button class="icon-btn sm danger" type="button">{icon("trash")}</button></td></tr>
            <tr><td><input type="text" value="مقاومت فشاری"></td><td><input type="text" value="بیش از ۴۵ مگاپاسکال"></td><td class="check-cell"><button class="icon-btn sm danger" type="button">{icon("trash")}</button></td></tr>
          </tbody></table></div>
      </div>
      <div class="adm-card">
        <h3>سئو</h3>
        <div class="field"><label>عنوان متا</label><input type="text" placeholder="نانوسنگ تراورتن کرم | عصرجدید"></div>
        <div class="field"><label>توضیحات متا</label><textarea rows="2" placeholder="توضیح ۱۵۰ کاراکتری برای نتایج جستجو"></textarea></div>
        <div class="field"><label>کلمات کلیدی</label><input type="text" placeholder="نانوسنگ، تراورتن مصنوعی، نمای ساختمان"></div>
      </div>
    </div>
    <aside class="adm-form-side">
      <div class="adm-card">
        <h3>تصویر شاخص</h3>
        <div class="upload-box js-upload">
          <img src="../assets/images/p-2.jpg" alt="پیش‌نمایش تصویر">
          <div class="upload-hint">{icon("upload")}<span>تصویر جدید را رها کنید یا کلیک کنید</span><small>JPG یا PNG، حداکثر ۲ مگابایت</small></div>
          <input type="file" hidden>
        </div>
        <button class="btn btn-ghost btn-sm btn-block" type="button" style="margin-top:10px">{icon("trash")} حذف تصویر</button>
      </div>
      <div class="adm-card">
        <h3>گالری تصاویر</h3>
        <div class="upload-grid">
          <div class="ug-item js-upload"><img src="../assets/images/cat-1.jpg" alt="گالری"><input type="file" hidden></div>
          <div class="ug-item js-upload"><img src="../assets/images/hero-1.jpg" alt="گالری"><input type="file" hidden></div>
          <div class="ug-item ug-add js-upload">{icon("plus")}<input type="file" hidden></div>
        </div>
      </div>
      <div class="adm-card">
        <h3>تنظیمات نمایش</h3>
        <div class="field"><label>برچسب نمایشی</label><input type="text" placeholder="پرفروش / جدید / ٪۱۳ تخفیف"></div>
        <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>نمایش در محصولات منتخب صفحه اصلی</span></label>
        <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>امکان خرید آنلاین</span></label>
        <label class="switch-row"><input type="checkbox"><span class="switch"></span><span>نمایش در لیست مقایسه</span></label>
      </div>
    </aside>
  </div>
</form>'''


def categories(t):
    rows = ""
    for i, c in enumerate(CATEGORIES):
        rows += f'''<tr>
      <td class="adm-prod"><img src="../assets/images/{c['image']}" alt="{c['name']}">
        <div><strong>{c['name']}</strong><small>{c['slug']}</small></div></td>
      <td>{c['desc'][:58]}…</td>
      <td>{fa_num(c['count'])}</td>
      <td><span class="status status-ok">فعال</span></td>
      <td class="row-actions">
        <button class="icon-btn sm" type="button" title="ویرایش">{icon("edit")}</button>
        <button class="icon-btn sm danger js-confirm" type="button" data-name="{c['name']}" title="حذف">{icon("trash")}</button>
      </td></tr>'''
    return f'''
<div class="adm-page-head">
  <div class="adm-filters">
    <div class="adm-searchbox">{icon("search")}<input type="search" placeholder="جستجوی دسته‌بندی…" class="js-admin-search" aria-label="جستجو"></div>
  </div>
  <div class="adm-page-actions">
    <button class="btn btn-primary btn-sm js-modal-btn" type="button" data-modal="category">{icon("plus")} افزودن دسته‌بندی</button>
  </div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>گروه‌های محصول</h3><p>{fa_num(len(CATEGORIES))} دسته‌بندی فعال</p></div></div>
  <div class="table-wrap"><table class="adm-table">
    <thead><tr><th>دسته‌بندی</th><th>توضیح</th><th>تعداد محصول</th><th>وضعیت</th><th></th></tr></thead>
    <tbody>{rows}</tbody></table></div>
</div>'''


def orders(t):
    rows = ""
    for o in ADMIN["orders"]:
        rows += f'''<tr>
      <td class="check-cell"><input type="checkbox" aria-label="انتخاب"></td>
      <td><a class="link" href="#">{o['code']}</a></td>
      <td>{o['customer']}</td><td>{o['date']}</td>
      <td>{fa_num(o['items'])} قلم</td><td>{money(o['total'])}</td>
      <td><span class="status status-{o['key']}">{o['status']}</span></td>
      <td class="row-actions">
        <button class="icon-btn sm js-modal-btn" type="button" data-modal="order" title="جزئیات">{icon("eye")}</button>
        <button class="icon-btn sm" type="button" title="چاپ فاکتور">{icon("print")}</button>
        <button class="icon-btn sm danger js-confirm" type="button" data-name="{o['code']}" title="لغو">{icon("x-circle")}</button>
      </td></tr>'''
    small = [
        ("در انتظار پرداخت", "۹ سفارش", "cart", "var(--warn)"),
        ("در حال آماده‌سازی و ارسال", "۱۴ سفارش", "truck", "var(--info)"),
        ("تحویل‌شده در این ماه", "۲۱ سفارش", "check-circle", "var(--ok)"),
    ]
    kpi = '<div class="admin-kpis" style="grid-template-columns:repeat(3,1fr)">' + "".join(
        f'''<article class="kpi"><div class="kpi-top"><span class="kpi-ico" style="color:{color}">{icon(ic)}</span></div>
        <span class="kpi-title">{title}</span><div class="kpi-value" style="font-size:1.2rem">{value}</div></article>'''
        for title, value, ic, color in small) + "</div>"
    return f'''
{kpi}
<div class="adm-page-head">
  <div class="adm-filters">
    <div class="adm-searchbox">{icon("search")}<input type="search" placeholder="کد سفارش یا نام مشتری…" class="js-admin-search" aria-label="جستجو"></div>
    <select class="adm-select"><option>همه وضعیت‌ها</option><option>در انتظار پرداخت</option><option>در حال آماده‌سازی</option><option>در حال ارسال</option><option>تحویل‌شده</option><option>لغوشده</option></select>
    <input class="adm-select" type="text" placeholder="از تاریخ ۱۴۰۴/۰۴/۰۱" style="min-width:170px">
  </div>
  <div class="adm-page-actions"><button class="btn btn-outline btn-sm" type="button">{icon("download")} خروجی گزارش</button></div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>سفارش‌ها</h3><p>{fa_num(len(ADMIN['orders']))} سفارش در این فهرست</p></div></div>
  <div class="table-wrap"><table class="adm-table">
    <thead><tr><th class="check-cell"><input type="checkbox" class="js-check-all" aria-label="انتخاب همه"></th><th>کد سفارش</th><th>مشتری</th><th>تاریخ</th><th>اقلام</th><th>مبلغ (تومان)</th><th>وضعیت</th><th></th></tr></thead>
    <tbody>{rows}</tbody></table></div>
  <div class="adm-pagination"><span>نمایش ۱ تا ۶ از ۳۷ سفارش</span>
    <div class="pager"><button class="chip-btn active" type="button">۱</button><button class="chip-btn" type="button">۲</button>
      <button class="chip-btn" type="button">۳</button></div></div>
</div>'''


def comments(t):
    cards = ""
    for c in ADMIN["comments"]:
        st = {"در انتظار تأیید": ("warn", "در انتظار تأیید"), "تأیید شده": ("ok", "تأییدشده"), "رد شده": ("danger", "ردشده")}[c["status"]]
        cards += f'''<article class="adm-card" style="padding:18px">
      <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
        <span class="avatar">{c['name'][:1]}</span>
        <div style="flex:1;min-width:180px">
          <strong style="font-size:.9rem">{c['name']}</strong>
          <div class="adm-card-head" style="margin:0"><p style="margin:0">روی «{c['product']}» — {c['date']}</p></div>
        </div>
        <span class="status status-{st[0]}">{st[1]}</span>
      </div>
      <p style="margin:12px 0 0;color:var(--ink-2);font-size:.88rem">{c['text']}</p>
      <div style="display:flex;gap:8px;margin-top:14px;flex-wrap:wrap">
        <button class="btn btn-outline btn-sm" type="button">{icon("check")} تأیید</button>
        <button class="btn btn-ghost btn-sm js-modal-btn" type="button" data-modal="reply">{icon("message")} پاسخ</button>
        <button class="btn btn-ghost btn-sm danger js-confirm" type="button" data-name="دیدگاه {c['name']}">حذف</button>
      </div>
    </article>'''
    return f'''
<div class="adm-page-head">
  <div class="adm-filters">
    <div class="adm-searchbox">{icon("search")}<input type="search" placeholder="جستجو در متن دیدگاه‌ها…" class="js-admin-search" aria-label="جستجو"></div>
    <div class="pager"><button class="chip-btn active" type="button">همه</button><button class="chip-btn" type="button">در انتظار تأیید</button><button class="chip-btn" type="button">تأییدشده</button></div>
  </div>
  <div class="adm-page-actions"><button class="btn btn-primary btn-sm" type="button">{icon("check")} تأیید موارد انتخاب‌شده</button></div>
</div>
<div class="adm-grid-2" style="gap:18px">{cards}</div>
<div class="adm-card">
  <h3>قواعد تأیید دیدگاه</h3>
  <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>تأیید خودکار دیدگاه مشتریان دارای سابقه خرید</span></label>
  <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>فیلتر خودکار کلمات نامناسب</span></label>
  <label class="switch-row"><input type="checkbox"><span class="switch"></span><span>اجازه ثبت دیدگاه برای کاربران مهمان</span></label>
</div>'''


def customers(t):
    rows = ""
    for u in ADMIN["users"]:
        rows += f'''<tr>
      <td class="check-cell"><input type="checkbox" aria-label="انتخاب"></td>
      <td class="adm-prod"><span class="avatar">{u['name'][:1]}</span>
        <div><strong style="font-size:.87rem">{u['name']}</strong><small>{u['email'] or '—'}</small></div></td>
      <td>{u['phone']}</td><td>{u['role']}</td><td>{fa_num(u['orders'])} سفارش</td><td>{u['joined']}</td>
      <td>{'<span class="status status-ok">فعال</span>' if u['status'] else '<span class="status status-danger">غیرفعال</span>'}</td>
      <td class="row-actions">
        <button class="icon-btn sm" type="button" title="ویرایش">{icon("edit")}</button>
        <button class="icon-btn sm" type="button" title="تغییر نقش">{icon("lock")}</button>
        <button class="icon-btn sm danger js-confirm" type="button" data-name="{u['name']}" title="غیرفعال">{icon("trash")}</button>
      </td></tr>'''
    return f'''
<div class="adm-page-head">
  <div class="adm-filters">
    <div class="adm-searchbox">{icon("search")}<input type="search" placeholder="نام، ایمیل یا شماره همراه…" class="js-admin-search" aria-label="جستجو"></div>
    <select class="adm-select"><option>همه نقش‌ها</option>{''.join(f'<option>{r["name"]}</option>' for r in ADMIN['roles'])}</select>
  </div>
  <div class="adm-page-actions">
    <button class="btn btn-outline btn-sm" type="button">{icon("download")} خروجی</button>
    <button class="btn btn-primary btn-sm js-modal-btn" type="button" data-modal="customer">{icon("plus")} کاربر جدید</button>
  </div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>کاربران و مشتریان</h3><p>۱٬۲۴۸ کاربر ثبت‌شده</p></div></div>
  <div class="table-wrap"><table class="adm-table">
    <thead><tr><th class="check-cell"><input type="checkbox" class="js-check-all" aria-label="انتخاب همه"></th><th>کاربر</th><th>شماره همراه</th><th>نقش</th><th>سفارش‌ها</th><th>تاریخ عضویت</th><th>وضعیت</th><th></th></tr></thead>
    <tbody>{rows}</tbody></table></div>
</div>'''


def roles(t):
    rows = "".join(f'''<tr>
      <td><strong>{r['name']}</strong></td>
      <td>{fa_num(r['users'])} کاربر</td>
      <td>{r['perms']}</td>
      <td>{r['create']}</td>
      <td class="row-actions">
        <button class="icon-btn sm" type="button" title="ویرایش">{icon("edit")}</button>
        <button class="icon-btn sm danger js-confirm" type="button" data-name="نقش {r['name']}" title="حذف">{icon("trash")}</button>
      </td></tr>''' for r in ADMIN["roles"])
    perms = [("مدیریت محصولات", True), ("مدیریت سفارش‌ها", True), ("مدیریت مشتریان", True), ("مدیریت دیدگاه‌ها", True),
             ("گزارش‌های مالی", True), ("تنظیمات سایت", False), ("مدیریت نقش‌ها", False)]
    perm_rows = "".join(f'''<tr><td>{name}</td>
      <td><label class="switch-inline"><input type="checkbox" {'checked' if ok else ''}><span class="switch"></span></label></td>
      <td><label class="switch-inline"><input type="checkbox" {'checked' if ok else ''}><span class="switch"></span></label></td></tr>''' for name, ok in perms)
    return f'''
<div class="adm-page-head">
  <div class="adm-page-title"><h2>نقش‌ها و سطوح دسترسی</h2><p>تعیین دسترسی هر گروه کاربری در پنل مدیریت</p></div>
  <div class="adm-page-actions"><button class="btn btn-primary btn-sm js-modal-btn" type="button" data-modal="role">{icon("plus")} نقش جدید</button></div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>نقش‌های تعریف‌شده</h3></div></div>
  <div class="table-wrap"><table class="adm-table">
    <thead><tr><th>نام نقش</th><th>تعداد کاربر</th><th>دسترسی‌ها</th><th>تاریخ ایجاد</th><th></th></tr></thead>
    <tbody>{rows}</tbody></table></div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>ماتریس دسترسی</h3><p>مقایسه دو نقش پرکاربرد</p></div></div>
  <div class="table-wrap"><table class="adm-table">
    <thead><tr><th>بخش</th><th>مدیر فروش</th><th>پشتیبانی</th></tr></thead>
    <tbody>{perm_rows}</tbody></table></div>
</div>'''


def profile(t):
    return f'''
<div class="adm-page-head">
  <div class="adm-page-title"><h2>پروفایل مدیر</h2><p>اطلاعات حساب و امنیت ورود به پنل</p></div>
  <div class="adm-page-actions"><button class="btn btn-primary btn-sm" type="button" form="profileForm" formnovalidate>{icon("save")} ذخیره تغییرات</button></div>
</div>
<div class="adm-grid-1-2">
  <div class="adm-card adm-profile-card">
    <span class="avatar avatar-xl">س‌ر</span>
    <h3>مهندس سعید رضایی</h3>
    <span class="status status-ok">مدیر سیستم</span>
    <ul class="kv-list">
      <li><span>نام کاربری</span><strong>saeed.rezaei</strong></li>
      <li><span>شماره همراه</span><strong>۰۹۱۵۹۸۶۱۲۱۶</strong></li>
      <li><span>ایمیل</span><strong>saeed@asrjadid.com</strong></li>
      <li><span>آخرین ورود</span><strong>امروز ۰۸:۴۲</strong></li>
    </ul>
    <button class="btn btn-ghost btn-sm btn-block" type="button" style="margin-top:12px">{icon("upload")} تغییر تصویر پروفایل</button>
  </div>
  <div class="adm-form-main">
    <form class="adm-card adm-form js-adm-form" id="profileForm" novalidate>
      <h3>اطلاعات فردی</h3>
      <div class="adm-form-grid">
        <div class="field"><label>نام</label><input type="text" value="سعید"></div>
        <div class="field"><label>نام خانوادگی</label><input type="text" value="رضایی"></div>
        <div class="field"><label>شماره همراه</label><input type="tel" value="۰۹۱۵۹۸۶۱۲۱۶"></div>
        <div class="field"><label>ایمیل</label><input type="email" value="saeed@asrjadid.com"></div>
      </div>
      <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>دریافت ایمیل گزارش فروش روزانه</span></label>
      <button class="btn btn-outline btn-sm" type="submit" style="align-self:flex-start">{icon("save")} ذخیره اطلاعات</button>
    </form>
    <form class="adm-card adm-form js-adm-form" novalidate>
      <h3>تغییر رمز عبور</h3>
      <div class="adm-form-grid">
        <div class="field"><label>رمز فعلی</label><input type="password"></div>
        <div class="field"><label>رمز جدید</label><input type="password"></div>
        <div class="field full"><label>تکرار رمز جدید</label><input type="password"></div>
      </div>
      <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>ورود دومرحله‌ای با پیامک</span></label>
      <button class="btn btn-outline btn-sm" type="submit" style="align-self:flex-start">{icon("lock")} تغییر رمز</button>
    </form>
  </div>
</div>'''


def settings(t):
    return f'''
<div class="adm-page-head">
  <div class="adm-page-title"><h2>تنظیمات فروشگاه</h2><p>اطلاعات تماس، ارسال، پرداخت و سئو</p></div>
  <div class="adm-page-actions"><button class="btn btn-primary btn-sm" type="submit" form="settingsForm">{icon("save")} ذخیره تنظیمات</button></div>
</div>
<form class="adm-form js-adm-form" id="settingsForm" novalidate>
  <div class="adm-tabs js-adm-tabs">
    <div class="tabs-head">
      <a class="tab-btn active" href="#st-general" data-tab="st-general">عمومی</a>
      <a class="tab-btn" href="#st-contact" data-tab="st-contact">اطلاعات تماس</a>
      <a class="tab-btn" href="#st-ship" data-tab="st-ship">ارسال و حمل</a>
      <a class="tab-btn" href="#st-pay" data-tab="st-pay">پرداخت و مالیات</a>
      <a class="tab-btn" href="#st-seo" data-tab="st-seo">سئو و پشتیبان</a>
    </div>
    <div class="tabs-body">
      <div class="tab-panel active" id="st-general">
        <div class="adm-card">
          <h3>اطلاعات عمومی</h3>
          <div class="adm-form-grid">
            <div class="field"><label>نام فروشگاه</label><input type="text" value="عصرجدید"></div>
            <div class="field"><label>شعار سایت</label><input type="text" value="طراحی امروز، استحکام فردا"></div>
            <div class="field"><label>واحد پول</label><select><option>تومان</option><option>ریال</option></select></div>
            <div class="field"><label>تقویم نمایش</label><select><option>شمسی</option><option>میلادی</option></select></div>
          </div>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>فعال بودن فروشگاه و ثبت سفارش</span></label>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>نمایش قیمت برای کاربران مهمان</span></label>
        </div>
      </div>
      <div class="tab-panel" id="st-contact">
        <div class="adm-card">
          <h3>اطلاعات تماس</h3>
          <div class="adm-form-grid">
            <div class="field"><label>تلفن ثابت</label><input type="text" value="{SITE['phone']}"></div>
            <div class="field"><label>همراه / واتس‌اپ</label><input type="text" value="{SITE['mobile']}"></div>
            <div class="field"><label>ایمیل فروش</label><input type="email" value="{SITE['sales_email']}"></div>
            <div class="field"><label>ایمیل پشتیبانی</label><input type="email" value="{SITE['email']}"></div>
            <div class="field full"><label>نشانی کارخانه</label><textarea rows="2">{SITE['address']}</textarea></div>
            <div class="field full"><label>ساعات کاری</label><input type="text" value="{SITE['hours']}"></div>
          </div>
        </div>
      </div>
      <div class="tab-panel" id="st-ship">
        <div class="adm-card">
          <h3>روش‌های ارسال</h3>
          <div class="table-wrap"><table class="adm-table adm-table-input">
            <thead><tr><th>روش ارسال</th><th>هزینه پایه (تومان)</th><th>ارسال رایگان از</th><th>فعال</th></tr></thead>
            <tbody>
              <tr><td><input type="text" value="باربری تخصصی"></td><td><input type="text" value="۱٬۸۵۰٬۰۰۰"></td><td><input type="text" value="۵۰ مترمربع"></td>
                <td><label class="switch-inline"><input type="checkbox" checked><span class="switch"></span></label></td></tr>
              <tr><td><input type="text" value="پست پیشتاز"></td><td><input type="text" value="۳۸۰٬۰۰۰"></td><td><input type="text" value="تا ۳۰ کیلوگرم"></td>
                <td><label class="switch-inline"><input type="checkbox" checked><span class="switch"></span></label></td></tr>
              <tr><td><input type="text" value="تحویل حضوری"></td><td><input type="text" value="۰"></td><td><input type="text" value="—"></td>
                <td><label class="switch-inline"><input type="checkbox" checked><span class="switch"></span></label></td></tr>
            </tbody></table></div>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>بیمه خودکار محموله</span></label>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>ارسال پیامک کد رهگیری به مشتری</span></label>
        </div>
      </div>
      <div class="tab-panel" id="st-pay">
        <div class="adm-card">
          <h3>درگاه پرداخت</h3>
          <div class="adm-form-grid">
            <div class="field"><label>درگاه اصلی</label><select><option>زرین‌پال</option><option>درگاه پارسیان</option><option>سامان</option></select></div>
            <div class="field"><label>شماره پذیرنده</label><input type="text" value="۸۸۴۵۶۲۲"></div>
            <div class="field"><label>مالیات ارزش افزوده (٪)</label><input type="text" value="۹"></div>
            <div class="field"><label>پیش‌پرداخت سفارش (٪)</label><input type="text" value="۳۰"></div>
          </div>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>صدور خودکار فاکتور رسمی</span></label>
          <label class="switch-row"><input type="checkbox"><span class="switch"></span><span>فعال بودن پرداخت کارت به کارت</span></label>
        </div>
      </div>
      <div class="tab-panel" id="st-seo">
        <div class="adm-card">
          <h3>سئو</h3>
          <div class="field"><label>عنوان پیش‌فرض صفحات</label><input type="text" value="عصرجدید | سنگ مصنوعی، نانوسنگ، کوارتز و کورین"></div>
          <div class="field"><label>توضیحات متا پیش‌فرض</label><textarea rows="2">عصرجدید، تولیدکننده سنگ مصنوعی نما، پنل سه‌بعدی، صفحات کوارتز و کورین با ۱۹ سال سابقه و ضمانت کتبی ۱۸ ماهه.</textarea></div>
          <div class="adm-form-grid">
            <div class="field"><label>کد Google Analytics</label><input type="text" placeholder="G-XXXXXXX"></div>
            <div class="field"><label>متا تگ Search Console</label><input type="text" placeholder="google-site-verification=…"></div>
          </div>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>ساخت خودکار نقشه سایت XML</span></label>
        </div>
        <div class="adm-card">
          <h3>پشتیبان‌گیری</h3>
          <ul class="kv-list">
            <li><span>آخرین نسخه پشتیبان</span><strong>امروز ۰۳:۰۰ (خودکار)</strong></li>
            <li><span>حجم کل داده</span><strong>۲٫۴ گیگابایت</strong></li>
          </ul>
          <div class="adm-inline-actions">
            <button class="btn btn-outline btn-sm" type="button">{icon("download")} دانلود پشتیبان</button>
            <button class="btn btn-outline btn-sm" type="button">{icon("refresh")} پشتیبان‌گیری فوری</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</form>'''


def admin_login(t):
    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ورود به پنل مدیریت | عصرجدید</title>
<link rel="icon" type="image/svg+xml" href="../assets/images/favicon.svg">
<link rel="stylesheet" href="../assets/css/admin.css">
</head>
<body class="admin admin-login-page admin-theme-{t}">
{sprite()}
<div class="adm-login">
  <div class="adm-login-brand">
    <span class="brand-mark">{icon("diamond")}</span>
    <h1>پنل مدیریت عصرجدید</h1>
    <p>برای ورود، اطلاعات حساب مدیریتی خود را وارد کنید.</p>
  </div>
  <div class="notice-bar notice-demo">{icon("alert")}<p>نسخه نمایشی: نام کاربری <strong>admin</strong> و رمز <strong>admin123</strong></p></div>
  <form class="adm-form js-adm-login" novalidate data-demo-user="admin" data-demo-pass="admin123">
    <div class="field"><label>نام کاربری یا ایمیل</label>
      <div class="input-icon">{icon("user")}<input type="text" placeholder="admin" required></div></div>
    <div class="field"><label>رمز عبور</label>
      <div class="input-icon">{icon("lock")}<input type="password" placeholder="••••••••" required>
        <button class="input-btn js-pass-toggle" type="button" aria-label="نمایش رمز">{icon("eye")}</button></div></div>
    <div class="adm-login-row">
      <label class="check-row"><input type="checkbox" checked><span>مرا به خاطر بسپار</span></label>
      <a href="../forgot-password.html" class="link">فراموشی رمز</a>
    </div>
    <button class="btn btn-primary btn-lg btn-block" type="submit">{icon("logout")} ورود به پنل</button>
  </form>
  <div class="adm-login-foot">
    <a href="../index.html">{icon("home")} بازگشت به سایت</a>
    <span>پشتیبانی فنی: ۰۹۱۵-۹۸۶-۱۲۱۶</span>
  </div>
</div>
<div class="toast-wrap" id="toastWrap"></div>
<script src="../assets/js/admin.js"></script>
</body>
</html>
'''
