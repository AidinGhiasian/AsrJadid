# -*- coding: utf-8 -*-
"""بدنه صفحات پنل مدیریت (مشترک بین دو پوسته)"""
from data import *
from layouts import icon, cat_name, product_card

STATUS_CLASS = {"pending": "warn", "processing": "info", "shipping": "info", "done": "ok", "canceled": "danger"}


def stat_cards():
    cards = "".join(f'''<div class="adm-stat">
      <span class="as-ico">{icon(c['icon'])}</span>
      <div class="as-body"><span class="as-title">{c['title']}</span>
        <strong class="as-value">{c['value']} <small>{c['unit']}</small></strong>
        <span class="as-delta {'up' if c['up'] else 'down'}">{icon("trend-up" if c['up'] else "trend-down")} {c['delta']} نسبت به ماه قبل</span></div>
    </div>''' for c in ADMIN["dashboard_cards"])
    return f'<div class="adm-stats">{cards}</div>'


def dashboard(t):
    bars = "".join(f'<div class="bar-col"><span class="bar-val">{fa_num(b["value"])}</span>'
                   f'<i style="height:{int(b["value"] / 80 * 100)}%"></i><small>{b["label"]}</small></div>'
                   for b in ADMIN["sales_chart"])
    tops = "".join(f'''<tr>
      <td>{fa_num(i + 1)}</td><td>{p['name']}</td><td>{fa_num(p['sold'])}</td>
      <td>{money(p['revenue'])}</td>
      <td><div class="mini-bar"><b style="width:{p['share']}%"></b></div></td></tr>''' for i, p in enumerate(ADMIN["top_products"]))
    acts = "".join(f'''<li><span class="act-ico">{icon(a['icon'])}</span>
      <div><p>{a['text']}</p><small>{a['time']}</small></div></li>''' for a in ADMIN["activities"])
    orders = "".join(f'''<tr>
      <td><a class="link" href="orders.html">{o['code']}</a></td><td>{o['customer']}</td><td>{o['date']}</td>
      <td>{money(o['total'])}</td>
      <td><span class="status status-{o['key']}">{o['status']}</span></td></tr>''' for o in ADMIN["orders"][:5])
    donut = "".join(f'<li><span class="dot" style="--c:{r["color"]}"></span><span>{r["label"]}</span><strong>{fa_num(r["pct"])}٪</strong></li>'
                    for r in ADMIN["reports"])
    donut_bg = ", ".join([f'{r["color"]} 0 {sum(x["pct"] for x in ADMIN["reports"][:i + 1])}%' for i, r in enumerate(ADMIN["reports"])])
    return f'''
{stat_cards()}
<div class="adm-grid-2-1">
  <div class="adm-card">
    <div class="adm-card-head"><div><h3>نمودار فروش ماهانه</h3><p>مجموع فروش به تفکیک ماه (میلیون تومان)</p></div>
      <div class="adm-card-tools"><button class="chip-btn active" type="button">۸ ماه</button><button class="chip-btn" type="button">سال ۱۴۰۴</button></div></div>
    <div class="bar-chart">{bars}</div>
  </div>
  <div class="adm-card">
    <div class="adm-card-head"><div><h3>سهم گروه محصولات</h3><p>از کل درآمد سه ماه گذشته</p></div></div>
    <div class="donut-wrap">
      <div class="donut" style="background:conic-gradient({donut_bg})"><span class="donut-hole"><strong>۱۰۰٪</strong><small>کل فروش</small></span></div>
      <ul class="donut-legend">{donut}</ul>
    </div>
  </div>
</div>
<div class="adm-grid-2-1">
  <div class="adm-card">
    <div class="adm-card-head"><div><h3>پرفروش‌ترین محصولات</h3><p>بر اساس تعداد فروش در ۹۰ روز گذشته</p></div>
      <a class="adm-link" href="products.html">مدیریت محصولات {icon("arrow-left")}</a></div>
    <div class="table-wrap"><table class="adm-table">
      <thead><tr><th>#</th><th>محصول</th><th>فروش</th><th>درآمد</th><th>سهم</th></tr></thead>
      <tbody>{tops}</tbody></table></div>
  </div>
  <div class="adm-card">
    <div class="adm-card-head"><div><h3>آخرین فعالیت‌ها</h3><p>رویدادهای اخیر پنل و فروشگاه</p></div></div>
    <ul class="activity">{acts}</ul>
  </div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>سفارش‌های اخیر</h3><p>آخرین سفارش‌های ثبت‌شده در فروشگاه</p></div>
    <a class="adm-link" href="orders.html">همه سفارش‌ها {icon("arrow-left")}</a></div>
  <div class="table-wrap"><table class="adm-table">
    <thead><tr><th>کد سفارش</th><th>مشتری</th><th>تاریخ</th><th>مبلغ</th><th>وضعیت</th></tr></thead>
    <tbody>{orders}</tbody></table></div>
</div>
<div class="adm-grid-3">
  <div class="adm-card adm-quick">
    <h3>افزودن سریع</h3>
    <a href="product-form.html">{icon("plus")} محصول جدید</a>
    <a href="categories.html">{icon("grid")} دسته‌بندی جدید</a>
    <a href="comments.html">{icon("message")} بررسی دیدگاه‌ها</a>
    <a href="settings.html">{icon("settings")} تنظیمات سایت</a>
  </div>
  <div class="adm-card">
    <h3>وضعیت انبار</h3>
    <ul class="stock-list">
      <li><span>نانوسنگ نمای تراورتن کرم</span><div class="mini-bar"><b style="width:88%"></b></div><small>۲۴۰۰ مترمربع</small></li>
      <li><span>آجرنما نسوز تراکوتا</span><div class="mini-bar"><b style="width:96%"></b></div><small>۵۲۰۰ مترمربع</small></li>
      <li><span>صفحه کوارتز سفید برفی</span><div class="mini-bar"><b style="width:52%"></b></div><small>۱۲۴۰ مترمربع</small></li>
      <li><span>سینک کورین یکپارچه</span><div class="mini-bar warn"><b style="width:18%"></b></div><small>۱۴۵ عدد — نیاز به تولید</small></li>
    </ul>
  </div>
  <div class="adm-card">
    <h3>میانبرهای گزارش</h3>
    <div class="report-tiles">
      <a href="orders.html">{icon("chart")}<strong>گزارش فروش</strong><small>خروجی Excel و PDF</small></a>
      <a href="customers.html">{icon("users")}<strong>مشتریان فعال</strong><small>۱٬۲۴۸ مشتری ثبت‌شده</small></a>
      <a href="comments.html">{icon("message")}<strong>دیدگاه‌های جدید</strong><small>۵ دیدگاه در انتظار تأیید</small></a>
      <a href="settings.html">{icon("settings")}<strong>تنظیمات فروشگاه</strong><small>ارسال، مالیات، درگاه</small></a>
    </div>
  </div>
</div>'''


def products(t):
    rows = ""
    for s in STONES:
        stock_cls = "ok" if s["stock"] > 500 else ("warn" if s["stock"] > 100 else "danger")
        rows += f'''<tr>
      <td class="check-cell"><input type="checkbox" aria-label="انتخاب"></td>
      <td class="adm-prod"><img src="../assets/images/{s['image']}" alt="{s['name']}">
        <div><a class="link" href="product-form.html">{s['name']}</a><small>کد {s['code']}</small></div></td>
      <td>{cat_name(s['cat'])}</td><td>{s['size']}</td>
      <td>{fa_num(s['price'])}</td>
      <td><span class="stock-pill {stock_cls}">{fa_num(s['stock'])} {s['unit']}</span></td>
      <td>{'<span class="status status-ok">منتشر شده</span>' if s['featured'] else '<span class="status status-info">پیش‌نویس/عادی</span>'}</td>
      <td class="row-actions">
        <a class="icon-btn sm" href="product-form.html" title="ویرایش">{icon("edit")}</a>
        <button class="icon-btn sm" type="button" title="نمایش در سایت">{icon("eye")}</button>
        <button class="icon-btn sm danger js-confirm" type="button" title="حذف" data-name="{s['name']}">{icon("trash")}</button>
      </td></tr>'''
    return f'''
<div class="adm-page-head">
  <div class="adm-filters">
    <div class="adm-searchbox">{icon("search")}<input type="search" placeholder="جستجوی نام یا کد محصول…" class="js-admin-search" aria-label="جستجو"></div>
    <select class="adm-select" aria-label="دسته‌بندی"><option>همه دسته‌بندی‌ها</option>{''.join(f'<option>{c["name"]}</option>' for c in CATEGORIES)}</select>
    <select class="adm-select" aria-label="وضعیت"><option>همه وضعیت‌ها</option><option>منتشر شده</option><option>پیش‌نویس</option><option>ناموجود</option></select>
    <button class="btn btn-outline sm" type="button">{icon("filter")} اعمال فیلتر</button>
  </div>
  <div class="adm-page-actions">
    <button class="btn btn-outline sm" type="button">{icon("download")} خروجی Excel</button>
    <a class="btn btn-primary sm" href="product-form.html">{icon("plus")} افزودن محصول</a>
  </div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>لیست محصولات</h3><p>{fa_num(len(STONES))} محصول نمایش داده شده از ۱۶۱ محصول</p></div>
    <div class="adm-bulk"><span>عملیات گروهی:</span>
      <button class="btn btn-ghost sm" type="button">انتشار</button>
      <button class="btn btn-ghost sm" type="button">پیش‌نویس</button>
      <button class="btn btn-ghost sm danger" type="button">حذف</button></div></div>
  <div class="table-wrap"><table class="adm-table adm-table-hover">
    <thead><tr><th class="check-cell"><input type="checkbox" class="js-check-all" aria-label="انتخاب همه"></th>
      <th>محصول</th><th>دسته‌بندی</th><th>ابعاد</th><th>قیمت (تومان)</th><th>موجودی</th><th>وضعیت</th><th>عملیات</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
  <div class="adm-pagination">
    <span>نمایش ۱ تا ۱۲ از ۱۶۱ محصول</span>
    <div class="pager"><button class="icon-btn sm" type="button">{icon("chev-right")}</button>
      <button class="chip-btn active" type="button">۱</button><button class="chip-btn" type="button">۲</button>
      <button class="chip-btn" type="button">۳</button><button class="icon-btn sm" type="button">{icon("chev-left")}</button></div>
  </div>
</div>'''


def product_form(t):
    return f'''
<form class="adm-form js-adm-form" novalidate>
  <div class="adm-page-head">
    <div class="adm-page-title"><h2>افزودن محصول جدید</h2><p>اطلاعات محصول را تکمیل کنید؛ فیلدهای ستاره‌دار الزامی هستند.</p></div>
    <div class="adm-page-actions">
      <a class="btn btn-ghost sm" href="products.html">{icon("x")} انصراف</a>
      <button class="btn btn-outline sm" type="button">{icon("save")} ذخیره پیش‌نویس</button>
      <button class="btn btn-primary sm" type="submit">{icon("check")} انتشار محصول</button>
    </div>
  </div>
  <div class="adm-form-layout">
    <div class="adm-form-main">
      <div class="adm-card">
        <div class="adm-card-head"><div><h3>اطلاعات پایه</h3><p>نام، کد و دسته‌بندی محصول</p></div></div>
        <div class="adm-form-grid">
          <div class="field"><label>نام محصول <span class="req">*</span></label><input type="text" class="js-slug-src" placeholder="مثلاً: نانوسنگ نمای تراورتن کرم" required></div>
          <div class="field"><label>کد محصول <span class="req">*</span></label><input type="text" placeholder="NS-311" required></div>
          <div class="field"><label>نشانی صفحه (Slug)</label><input type="text" class="js-slug-out" placeholder="nanosang-tavartun-krem"></div>
          <div class="field"><label>دسته‌بندی <span class="req">*</span></label><select required><option value="">انتخاب کنید…</option>{''.join(f'<option>{c["name"]}</option>' for c in CATEGORIES)}</select></div>
          <div class="field full"><label>توضیح کوتاه (نمایش در کارت محصول)</label>
            <textarea rows="2" placeholder="حداکثر ۱۴۰ کاراکتر…"></textarea></div>
          <div class="field full"><label>توضیحات کامل</label>
            <textarea rows="6" placeholder="ویژگی‌ها، کاربردها و نکات فنی محصول…"></textarea></div>
        </div>
      </div>
      <div class="adm-card">
        <div class="adm-card-head"><div><h3>قیمت و موجودی</h3><p>مبالغ به تومان وارد شود</p></div></div>
        <div class="adm-form-grid">
          <div class="field"><label>قیمت واحد <span class="req">*</span></label><input type="text" placeholder="۶۸۰۰۰۰" required></div>
          <div class="field"><label>قیمت قبل از تخفیف</label><input type="text" placeholder="۷۸۰۰۰۰"></div>
          <div class="field"><label>واحد فروش</label><select><option>مترمربع</option><option>متر طول</option><option>عدد</option><option>بسته</option></select></div>
          <div class="field"><label>موجودی انبار <span class="req">*</span></label><input type="text" placeholder="۲۴۰۰" required></div>
          <div class="field"><label>حد هشدار موجودی</label><input type="text" placeholder="۲۰۰"></div>
          <div class="field"><label>وضعیت انتشار</label><select><option>منتشر شده</option><option>پیش‌نویس</option><option>ناموجود</option></select></div>
        </div>
      </div>
      <div class="adm-card">
        <div class="adm-card-head"><div><h3>مشخصات فنی</h3><p>ابعاد، ضخامت، وزن و رنگ</p></div>
          <button class="btn btn-ghost sm" type="button">{icon("plus")} افزودن ردیف مشخصات</button></div>
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
            <tr><td><input type="text" value="کاربرد"></td><td><input type="text" value="نمای ساختمان، دیوار محوطه"></td><td class="check-cell"><button class="icon-btn sm danger" type="button">{icon("trash")}</button></td></tr>
          </tbody></table></div>
      </div>
      <div class="adm-card">
        <div class="adm-card-head"><div><h3>سئو و انتشار</h3><p>اطلاعات نمایش در موتورهای جستجو</p></div></div>
        <div class="adm-form-grid">
          <div class="field full"><label>عنوان متا (Title)</label><input type="text" placeholder="نانوسنگ تراورتن کرم | عصرجدید"></div>
          <div class="field full"><label>توضیحات متا (Description)</label><textarea rows="2" placeholder="توضیح ۱۵۰ کاراکتری برای نتایج جستجو…"></textarea></div>
          <div class="field full"><label>کلمات کلیدی</label><input type="text" placeholder="نانوسنگ، تراورتن مصنوعی، نمای ساختمان"></div>
        </div>
      </div>
    </div>
    <aside class="adm-form-side">
      <div class="adm-card">
        <div class="adm-card-head"><div><h3>تصویر شاخص</h3></div></div>
        <div class="upload-box js-upload">
          <img src="../assets/images/p-2.jpg" alt="پیش‌نمایش تصویر">
          <div class="upload-hint">{icon("upload")}<span>تصویر جدید را رها کنید یا کلیک کنید</span><small>JPG یا PNG، حداکثر ۲ مگابایت</small></div>
          <input type="file" hidden>
        </div>
        <button class="btn btn-ghost btn-block sm" type="button">{icon("trash")} حذف تصویر</button>
      </div>
      <div class="adm-card">
        <div class="adm-card-head"><div><h3>گالری تصاویر</h3></div></div>
        <div class="upload-grid">
          <div class="ug-item js-upload"><img src="../assets/images/cat-1.jpg" alt="تصویر گالری"><input type="file" hidden></div>
          <div class="ug-item js-upload"><img src="../assets/images/hero-1.jpg" alt="تصویر گالری"><input type="file" hidden></div>
          <div class="ug-item ug-add js-upload">{icon("plus")}<input type="file" hidden></div>
        </div>
      </div>
      <div class="adm-card">
        <div class="adm-card-head"><div><h3>برچسب‌ها و برجستگی</h3></div></div>
        <div class="field"><label>برچسب نمایشی</label><input type="text" placeholder="پرفروش / جدید / ٪۱۳ تخفیف"></div>
        <label class="check-row"><input type="checkbox" checked><span>نمایش در محصولات منتخب صفحه اصلی</span></label>
        <label class="check-row"><input type="checkbox"><span>فعال‌سازی مقایسه با محصولات مشابه</span></label>
        <label class="check-row"><input type="checkbox" checked><span>امکان خرید آنلاین</span></label>
      </div>
    </aside>
  </div>
</form>'''


def categories(t):
    rows = ""
    for i, c in enumerate(CATEGORIES):
        rows += f'''<tr>
      <td class="adm-prod"><img src="../assets/images/{c['image']}" alt="{c['name']}">
        <div><a class="link" href="product-form.html">{c['name']}</a><small>{c['slug']}</small></div></td>
      <td>{c['desc'][:64]}…</td>
      <td>{fa_num(c['count'])}</td>
      <td><span class="status status-ok">فعال</span></td>
      <td>{fa_num(i + 1)}</td>
      <td class="row-actions">
        <button class="icon-btn sm" type="button" title="ویرایش">{icon("edit")}</button>
        <button class="icon-btn sm danger js-confirm" type="button" title="حذف" data-name="{c['name']}">{icon("trash")}</button>
      </td></tr>'''
    return f'''
<div class="adm-page-head">
  <div class="adm-filters">
    <div class="adm-searchbox">{icon("search")}<input type="search" placeholder="جستجوی دسته‌بندی…" class="js-admin-search"></div>
    <select class="adm-select"><option>همه وضعیت‌ها</option><option>فعال</option><option>غیرفعال</option></select>
  </div>
  <div class="adm-page-actions">
    <a class="btn btn-primary sm js-modal-btn" href="#" data-modal="category">{icon("plus")} افزودن دسته‌بندی</a>
  </div>
</div>
<div class="adm-grid-1-2">
  <div class="adm-card">
    <div class="adm-card-head"><div><h3>دسته‌بندی جدید</h3><p>اطلاعات گروه محصول را وارد کنید</p></div></div>
    <form class="adm-form js-adm-form" novalidate>
      <div class="field"><label>نام دسته‌بندی <span class="req">*</span></label><input type="text" class="js-slug-src" placeholder="مثلاً: صفحات کوارتز" required></div>
      <div class="field"><label>نشانی صفحه (Slug)</label><input type="text" class="js-slug-out" placeholder="quartz"></div>
      <div class="field"><label>توضیح کوتاه</label><textarea rows="3" placeholder="توضیح نمایش در کارت دسته‌بندی…"></textarea></div>
      <div class="field"><label>تصویر دسته‌بندی</label>
        <div class="upload-box small js-upload">{icon("upload")}<span>انتخاب تصویر</span><input type="file" hidden></div></div>
      <label class="check-row"><input type="checkbox" checked><span>نمایش در منوی اصلی سایت</span></label>
      <button class="btn btn-primary btn-block" type="submit">{icon("save")} ذخیره دسته‌بندی</button>
    </form>
  </div>
  <div class="adm-card">
    <div class="adm-card-head"><div><h3>لیست دسته‌بندی‌ها</h3><p>{fa_num(len(CATEGORIES))} گروه محصول فعال</p></div></div>
    <div class="table-wrap"><table class="adm-table adm-table-hover">
      <thead><tr><th>دسته‌بندی</th><th>توضیح</th><th>تعداد محصول</th><th>وضعیت</th><th>ترتیب</th><th>عملیات</th></tr></thead>
      <tbody>{rows}</tbody></table></div>
  </div>
</div>'''


def orders(t):
    rows = ""
    for o in ADMIN["orders"]:
        rows += f'''<tr>
      <td class="check-cell"><input type="checkbox"></td>
      <td><a class="link" href="#">{o['code']}</a></td>
      <td>{o['customer']}</td><td>{o['date']}</td>
      <td>{fa_num(o['items'])} قلم</td><td>{money(o['total'])}</td>
      <td><span class="status status-{o['key']}">{o['status']}</span></td>
      <td class="row-actions">
        <button class="icon-btn sm js-modal-btn" type="button" data-modal="order" title="جزئیات">{icon("eye")}</button>
        <button class="icon-btn sm" type="button" title="چاپ فاکتور">{icon("print")}</button>
        <button class="icon-btn sm" type="button" title="تغییر وضعیت">{icon("refresh")}</button>
        <button class="icon-btn sm danger js-confirm" type="button" data-name="{o['code']}" title="لغو سفارش">{icon("x-circle")}</button>
      </td></tr>'''
    return f'''
{stat_cards()}
<div class="adm-page-head">
  <div class="adm-filters">
    <div class="adm-searchbox">{icon("search")}<input type="search" placeholder="جستجوی کد سفارش یا نام مشتری…" class="js-admin-search"></div>
    <select class="adm-select"><option>همه وضعیت‌ها</option><option>در انتظار پرداخت</option><option>در حال آماده‌سازی</option><option>در حال ارسال</option><option>تحویل شده</option><option>لغو شده</option></select>
    <input class="adm-select" type="text" placeholder="از تاریخ ۱۴۰۴/۰۴/۰۱">
    <button class="btn btn-outline sm" type="button">{icon("filter")} فیلتر</button>
  </div>
  <div class="adm-page-actions"><button class="btn btn-outline sm" type="button">{icon("download")} خروجی گزارش</button></div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>سفارش‌های فروشگاه</h3><p>{fa_num(len(ADMIN['orders']))} سفارش در این فهرست</p></div>
    <div class="adm-bulk"><span>تغییر وضعیت گروهی:</span>
      <button class="btn btn-ghost sm" type="button">آماده‌سازی</button>
      <button class="btn btn-ghost sm" type="button">ارسال</button>
      <button class="btn btn-ghost sm" type="button">تحویل</button></div></div>
  <div class="table-wrap"><table class="adm-table adm-table-hover">
    <thead><tr><th class="check-cell"><input type="checkbox" class="js-check-all"></th><th>کد سفارش</th><th>مشتری</th><th>تاریخ</th><th>اقلام</th><th>مبلغ کل (تومان)</th><th>وضعیت</th><th>عملیات</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
  <div class="adm-pagination"><span>نمایش ۱ تا ۶ از ۳۷ سفارش</span>
    <div class="pager"><button class="icon-btn sm" type="button">{icon("chev-right")}</button>
      <button class="chip-btn active" type="button">۱</button><button class="chip-btn" type="button">۲</button>
      <button class="chip-btn" type="button">۳</button><button class="icon-btn sm" type="button">{icon("chev-left")}</button></div></div>
</div>'''


def comments(t):
    rows = ""
    stat = {"در انتظار تأیید": "warn", "تأیید شده": "ok", "رد شده": "danger"}
    for c in ADMIN["comments"]:
        rows += f'''<tr>
      <td class="check-cell"><input type="checkbox"></td>
      <td><strong>{c['name']}</strong></td>
      <td><a class="link" href="#">{c['product']}</a></td>
      <td class="adm-comment-text">{c['text'][:110]}…</td>
      <td>{c['date']}</td>
      <td><span class="status status-{stat[c['status']]}">{c['status']}</span></td>
      <td class="row-actions">
        <button class="icon-btn sm" type="button" title="تأیید">{icon("check")}</button>
        <button class="icon-btn sm" type="button" title="پاسخ">{icon("message")}</button>
        <button class="icon-btn sm danger js-confirm" type="button" data-name="دیدگاه {c['name']}" title="حذف">{icon("trash")}</button>
      </td></tr>'''
    return f'''
<div class="adm-page-head">
  <div class="adm-filters">
    <div class="adm-searchbox">{icon("search")}<input type="search" placeholder="جستجو در متن دیدگاه‌ها…" class="js-admin-search"></div>
    <select class="adm-select"><option>همه وضعیت‌ها</option><option>در انتظار تأیید</option><option>تأیید شده</option><option>رد شده</option></select>
  </div>
  <div class="adm-page-actions"><button class="btn btn-primary sm" type="button">{icon("check")} تأیید موارد انتخاب‌شده</button></div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>دیدگاه‌های محصولات</h3><p>۵ دیدگاه ثبت‌شده، ۲ مورد در انتظار تأیید</p></div></div>
  <div class="table-wrap"><table class="adm-table adm-table-hover">
    <thead><tr><th class="check-cell"><input type="checkbox" class="js-check-all"></th><th>کاربر</th><th>محصول</th><th>متن دیدگاه</th><th>تاریخ</th><th>وضعیت</th><th>عملیات</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
</div>
<div class="adm-grid-2">
  <div class="adm-card">
    <h3>پاسخ سریع به دیدگاه</h3>
    <form class="adm-form js-adm-form" novalidate>
      <div class="field"><label>دیدگاه انتخاب‌شده</label><input type="text" value="سارا ح. — نانوسنگ نمای تراورتن کرم" readonly></div>
      <div class="field"><label>متن پاسخ</label><textarea rows="4" placeholder="پاسخ کارشناس عصرجدید…"></textarea></div>
      <label class="check-row"><input type="checkbox" checked><span>ثبت به‌عنوان پاسخ رسمی کارشناس (با نشان تأیید)</span></label>
      <button class="btn btn-primary" type="submit">{icon("message")} ارسال پاسخ</button>
    </form>
  </div>
  <div class="adm-card">
    <h3>قواعد تأیید دیدگاه</h3>
    <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>تأیید خودکار دیدگاه مشتریان دارای خرید</span></label>
    <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>فیلتر خودکار کلمات نامناسب</span></label>
    <label class="switch-row"><input type="checkbox"><span class="switch"></span><span>اجازه ثبت دیدگاه برای کاربران مهمان</span></label>
    <p class="muted">دیدگاه‌های در انتظار تأیید پس از ۷۲ ساعت به‌صورت خودکار بسته می‌شوند.</p>
  </div>
</div>'''


def customers(t):
    rows = ""
    for u in ADMIN["users"]:
        rows += f'''<tr>
      <td class="check-cell"><input type="checkbox"></td>
      <td class="adm-prod"><span class="avatar">{u['name'][:1]}</span>
        <div><a class="link" href="#">{u['name']}</a><small>{u['email'] or '—'}</small></div></td>
      <td>{u['phone']}</td><td>{u['role']}</td><td>{fa_num(u['orders'])} سفارش</td><td>{u['joined']}</td>
      <td>{'<span class="status status-ok">فعال</span>' if u['status'] else '<span class="status status-danger">غیرفعال</span>'}</td>
      <td class="row-actions">
        <button class="icon-btn sm" type="button" title="ویرایش">{icon("edit")}</button>
        <button class="icon-btn sm" type="button" title="تغییر نقش">{icon("lock")}</button>
        <button class="icon-btn sm danger js-confirm" type="button" data-name="{u['name']}" title="غیرفعال‌سازی">{icon("trash")}</button>
      </td></tr>'''
    return f'''
<div class="adm-page-head">
  <div class="adm-filters">
    <div class="adm-searchbox">{icon("search")}<input type="search" placeholder="جستجوی نام، ایمیل یا شماره…" class="js-admin-search"></div>
    <select class="adm-select"><option>همه نقش‌ها</option>{''.join(f'<option>{r["name"]}</option>' for r in ADMIN['roles'])}</select>
    <select class="adm-select"><option>همه وضعیت‌ها</option><option>فعال</option><option>غیرفعال</option></select>
  </div>
  <div class="adm-page-actions">
    <button class="btn btn-outline sm" type="button">{icon("download")} خروجی مشتریان</button>
    <button class="btn btn-primary sm js-modal-btn" type="button" data-modal="customer">{icon("plus")} افزودن کاربر</button>
  </div>
</div>
{stat_cards()}
<div class="adm-card">
  <div class="adm-card-head"><div><h3>کاربران و مشتریان</h3><p>۱٬۲۴۸ کاربر ثبت‌شده در فروشگاه</p></div></div>
  <div class="table-wrap"><table class="adm-table adm-table-hover">
    <thead><tr><th class="check-cell"><input type="checkbox" class="js-check-all"></th><th>کاربر</th><th>شماره همراه</th><th>نقش</th><th>سفارش‌ها</th><th>تاریخ عضویت</th><th>وضعیت</th><th>عملیات</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
</div>'''


def roles(t):
    rows = ""
    for r in ADMIN["roles"]:
        rows += f'''<tr>
      <td>{fa_num(r['id'])}</td>
      <td><strong>{r['name']}</strong></td>
      <td>{fa_num(r['users'])} کاربر</td>
      <td>{r['perms']}</td>
      <td>{r['create']}</td>
      <td class="row-actions">
        <button class="icon-btn sm" type="button" title="ویرایش">{icon("edit")}</button>
        <button class="icon-btn sm danger js-confirm" type="button" data-name="نقش {r['name']}" title="حذف">{icon("trash")}</button>
      </td></tr>'''
    perms = [("مدیریت محصولات", True), ("مدیریت سفارش‌ها", True), ("مدیریت مشتریان", True), ("مدیریت دیدگاه‌ها", True),
             ("مدیریت مقالات و گالری", True), ("گزارش‌های مالی", True), ("تنظیمات سایت", True), ("مدیریت نقش‌ها و دسترسی‌ها", False)]
    perm_rows = "".join(f'''<tr><td>{name}</td>
      <td><label class="switch-inline"><input type="checkbox" {'checked' if ok else ''}><span class="switch"></span></label></td>
      <td><label class="switch-inline"><input type="checkbox" {'checked' if ok else ''}><span class="switch"></span></label></td></tr>''' for name, ok in perms)
    return f'''
<div class="adm-page-head">
  <div class="adm-page-title"><h2>نقش‌ها و سطوح دسترسی</h2><p>تعیین سطح دسترسی هر گروه کاربری در پنل مدیریت</p></div>
  <div class="adm-page-actions"><button class="btn btn-primary sm js-modal-btn" type="button" data-modal="role">{icon("plus")} نقش جدید</button></div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>لیست نقش‌ها</h3></div></div>
  <div class="table-wrap"><table class="adm-table adm-table-hover">
    <thead><tr><th>#</th><th>نام نقش</th><th>تعداد کاربر</th><th>دسترسی‌ها</th><th>تاریخ ایجاد</th><th>عملیات</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
</div>
<div class="adm-card">
  <div class="adm-card-head"><div><h3>ماتریس دسترسی</h3><p>مقایسه دو نقش پرکاربرد: مدیر فروش و پشتیبانی</p></div></div>
  <div class="table-wrap"><table class="adm-table">
    <thead><tr><th>بخش</th><th>مدیر فروش</th><th>پشتیبانی</th></tr></thead>
    <tbody>{perm_rows}</tbody></table></div>
</div>'''


def profile(t):
    return f'''
<div class="adm-page-head">
  <div class="adm-page-title"><h2>پروفایل مدیر</h2><p>اطلاعات حساب کاربری و امنیت حساب مدیریتی</p></div>
  <div class="adm-page-actions"><button class="btn btn-primary sm" type="button">{icon("save")} ذخیره تغییرات</button></div>
</div>
<div class="adm-grid-1-2">
  <div class="adm-card adm-profile-card">
    <span class="avatar avatar-xl">س‌ر</span>
    <h3>مهندس سعید رضایی</h3>
    <span class="status status-ok">مدیر سیستم</span>
    <ul class="kv-list">
      <li><span>نام کاربری</span><strong>saeed.rezaei</strong></li>
      <li><span>شماره همراه</span><strong>۰۹۱۲۱۱۱۲۲۳۳</strong></li>
      <li><span>ایمیل</span><strong>saeed@asrjadid.com</strong></li>
      <li><span>آخرین ورود</span><strong>امروز – ۰۸:۴۲ از IP 217.218.4.11</strong></li>
      <li><span>دسترسی‌ها</span><strong>دسترسی کامل (۸ بخش)</strong></li>
    </ul>
    <button class="btn btn-outline btn-block" type="button">{icon("upload")} تغییر تصویر پروفایل</button>
  </div>
  <div class="stack-forms">
    <form class="adm-card adm-form js-adm-form" novalidate>
      <h3>اطلاعات فردی</h3>
      <div class="adm-form-grid">
        <div class="field"><label>نام</label><input type="text" value="سعید"></div>
        <div class="field"><label>نام خانوادگی</label><input type="text" value="رضایی"></div>
        <div class="field"><label>شماره همراه</label><input type="tel" value="۰۹۱۲۱۱۱۲۲۳۳"></div>
        <div class="field"><label>ایمیل</label><input type="email" value="saeed@asrjadid.com"></div>
      </div>
      <button class="btn btn-primary" type="submit">{icon("save")} ذخیره اطلاعات</button>
    </form>
    <form class="adm-card adm-form js-adm-form" novalidate>
      <h3>تغییر رمز عبور پنل</h3>
      <div class="adm-form-grid">
        <div class="field"><label>رمز فعلی</label><input type="password"></div>
        <div class="field"><label>رمز جدید</label><input type="password"></div>
        <div class="field full"><label>تکرار رمز جدید</label><input type="password"></div>
      </div>
      <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>ورود دومرحله‌ای با پیامک برای حساب مدیر</span></label>
      <button class="btn btn-outline" type="submit">{icon("lock")} تغییر رمز عبور</button>
    </form>
  </div>
</div>'''


def settings(t):
    return f'''
<div class="adm-page-head">
  <div class="adm-page-title"><h2>تنظیمات فروشگاه</h2><p>اطلاعات تماس، ارسال، پرداخت و تنظیمات عمومی سایت</p></div>
  <div class="adm-page-actions">
    <button class="btn btn-ghost sm" type="button">{icon("refresh")} بازگردانی پیش‌فرض</button>
    <button class="btn btn-primary sm" type="submit" form="settingsForm">{icon("save")} ذخیره تنظیمات</button>
  </div>
</div>
<form class="adm-form js-adm-form" id="settingsForm" novalidate>
  <div class="adm-tabs js-adm-tabs">
    <div class="tabs-head">
      <a class="tab-btn active" href="#st-general" data-tab="st-general">عمومی</a>
      <a class="tab-btn" href="#st-contact" data-tab="st-contact">اطلاعات تماس</a>
      <a class="tab-btn" href="#st-ship" data-tab="st-ship">ارسال و حمل</a>
      <a class="tab-btn" href="#st-pay" data-tab="st-pay">پرداخت و مالیات</a>
      <a class="tab-btn" href="#st-seo" data-tab="st-seo">سئو و اسکریپت‌ها</a>
    </div>
    <div class="tabs-body">
      <div class="tab-panel active" id="st-general">
        <div class="adm-card">
          <h3>اطلاعات عمومی سایت</h3>
          <div class="adm-form-grid">
            <div class="field"><label>نام فروشگاه</label><input type="text" value="عصرجدید"></div>
            <div class="field"><label>شعار سایت</label><input type="text" value="طراحی امروز، استحکام فردا"></div>
            <div class="field"><label>واحد پول</label><select><option>تومان</option><option>ریال</option></select></div>
            <div class="field"><label>نسخه نمایش تاریخ</label><select><option>شمسی (جلالی)</option><option>میلادی</option></select></div>
            <div class="field full"><label>معرفی کوتاه سایت (Footer)</label><textarea rows="3">{SITE['about_short'][:170]}…</textarea></div>
          </div>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>فعال بودن فروشگاه و امکان ثبت سفارش</span></label>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>نمایش قیمت به کاربران مهمان</span></label>
          <label class="switch-row"><input type="checkbox"><span class="switch"></span><span>حالت تعمیر سایت (بستن موقت فروشگاه)</span></label>
        </div>
      </div>
      <div class="tab-panel" id="st-contact">
        <div class="adm-card">
          <h3>اطلاعات تماس</h3>
          <div class="adm-form-grid">
            <div class="field"><label>تلفن ثابت</label><input type="text" value="{SITE['phone']}"></div>
            <div class="field"><label>تلفن همراه / واتس‌اپ</label><input type="text" value="{SITE['mobile']}"></div>
            <div class="field"><label>ایمیل فروش</label><input type="email" value="{SITE['sales_email']}"></div>
            <div class="field"><label>ایمیل پشتیبانی</label><input type="email" value="{SITE['email']}"></div>
            <div class="field full"><label>نشانی کارخانه</label><textarea rows="2">{SITE['address']}</textarea></div>
            <div class="field full"><label>ساعات کاری</label><input type="text" value="{SITE['hours']}"></div>
          </div>
        </div>
        <div class="adm-card">
          <h3>شبکه‌های اجتماعی</h3>
          <div class="adm-form-grid">
            <div class="field"><label>اینستاگرام</label><div class="input-icon">{icon("ig")}<input type="text" value="{SITE['instagram']}"></div></div>
            <div class="field"><label>تلگرام</label><div class="input-icon">{icon("tg")}<input type="text" value="{SITE['telegram']}"></div></div>
            <div class="field"><label>لینکدین</label><div class="input-icon">{icon("in")}<input type="text" value="{SITE['linkedin']}"></div></div>
            <div class="field"><label>واتس‌اپ</label><div class="input-icon">{icon("wa")}<input type="text" value="{SITE['whatsapp']}"></div></div>
          </div>
        </div>
      </div>
      <div class="tab-panel" id="st-ship">
        <div class="adm-card">
          <h3>روش‌های ارسال</h3>
          <div class="table-wrap"><table class="adm-table adm-table-input">
            <thead><tr><th>روش ارسال</th><th>هزینه پایه (تومان)</th><th>آستانه ارسال رایگان</th><th>فعال</th></tr></thead>
            <tbody>
              <tr><td><input type="text" value="باربری تخصصی"></td><td><input type="text" value="۱۸۵۰۰۰۰"></td><td><input type="text" value="۵۰ مترمربع"></td>
                <td><label class="switch-inline"><input type="checkbox" checked><span class="switch"></span></label></td></tr>
              <tr><td><input type="text" value="پست پیشتاز"></td><td><input type="text" value="۳۸۰۰۰۰"></td><td><input type="text" value="تا ۳۰ کیلوگرم"></td>
                <td><label class="switch-inline"><input type="checkbox" checked><span class="switch"></span></label></td></tr>
              <tr><td><input type="text" value="تحویل حضوری (کارخانه)"></td><td><input type="text" value="۰"></td><td><input type="text" value="—"></td>
                <td><label class="switch-inline"><input type="checkbox" checked><span class="switch"></span></label></td></tr>
            </tbody></table></div>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>بیمه خودکار محموله روی همه ارسال‌ها</span></label>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>ارسال پیامک کد رهگیری بارنامه به مشتری</span></label>
        </div>
      </div>
      <div class="tab-panel" id="st-pay">
        <div class="adm-card">
          <h3>درگاه پرداخت و مالیات</h3>
          <div class="adm-form-grid">
            <div class="field"><label>درگاه اصلی</label><select><option>زرین‌پال</option><option>درگاه پارسیان</option><option>سامان</option><option>آی‌دی‌پی</option></select></div>
            <div class="field"><label>شماره پذیرنده (Terminal)</label><input type="text" value="۸۸۴۵۶۲۲"></div>
            <div class="field"><label>درصد مالیات ارزش افزوده</label><input type="text" value="۹"></div>
            <div class="field"><label>درصد پیش‌پرداخت سفارش</label><input type="text" value="۳۰"></div>
          </div>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>صدور خودکار فاکتور رسمی پس از پرداخت موفق</span></label>
          <label class="switch-row"><input type="checkbox"><span class="switch"></span><span>فعال بودن پرداخت کارت به کارت (تأیید دستی)</span></label>
        </div>
        <div class="adm-card">
          <h3>تخفیف پلکانی پروژه‌ها</h3>
          <div class="table-wrap"><table class="adm-table adm-table-input">
            <thead><tr><th>از متراژ</th><th>تا متراژ</th><th>درصد تخفیف</th><th></th></tr></thead>
            <tbody>
              <tr><td><input type="text" value="۵۰"></td><td><input type="text" value="۲۰۰"></td><td><input type="text" value="۲"></td><td><button class="icon-btn sm danger" type="button">{icon("trash")}</button></td></tr>
              <tr><td><input type="text" value="۲۰۰"></td><td><input type="text" value="۵۰۰"></td><td><input type="text" value="۴"></td><td><button class="icon-btn sm danger" type="button">{icon("trash")}</button></td></tr>
              <tr><td><input type="text" value="۵۰۰"></td><td><input type="text" value="∞"></td><td><input type="text" value="۸"></td><td><button class="icon-btn sm danger" type="button">{icon("trash")}</button></td></tr>
            </tbody></table></div>
        </div>
      </div>
      <div class="tab-panel" id="st-seo">
        <div class="adm-card">
          <h3>تنظیمات سئو</h3>
          <div class="adm-form-grid">
            <div class="field full"><label>عنوان پیش‌فرض صفحات</label><input type="text" value="عصرجدید | سنگ مصنوعی، نانوسنگ، کوارتز و کورین"></div>
            <div class="field full"><label>توضیحات متا پیش‌فرض</label><textarea rows="2">عصرجدید، تولیدکننده سنگ مصنوعی نما، پنل سه‌بعدی، صفحات کوارتز و کورین با ۱۹ سال سابقه و ضمانت کتبی ۱۸ ماهه.</textarea></div>
            <div class="field"><label>کد Google Analytics</label><input type="text" placeholder="G-XXXXXXX"></div>
            <div class="field"><label>متا تگ تأیید Google Search Console</label><input type="text" placeholder="google-site-verification=…"></div>
          </div>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>ساخت خودکار نقشه سایت XML</span></label>
          <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>فشرده‌سازی و کش تصاویر محصولات</span></label>
        </div>
        <div class="adm-card">
          <h3>پشتیبان‌گیری</h3>
          <ul class="kv-list">
            <li><span>آخرین نسخه پشتیبان</span><strong>امروز – ۰۳:۰۰ (خودکار)</strong></li>
            <li><span>حجم کل داده سایت</span><strong>۲٫۴ گیگابایت</strong></li>
            <li><span>تعداد نسخه‌های نگهداری‌شده</span><strong>۱۴ نسخه</strong></li>
          </ul>
          <div class="adm-inline-actions">
            <button class="btn btn-outline sm" type="button">{icon("download")} دانلود نسخه پشتیبان</button>
            <button class="btn btn-outline sm" type="button">{icon("refresh")} پشتیبان‌گیری فوری</button>
            <button class="btn btn-outline sm" type="button">{icon("upload")} بازگردانی از فایل</button>
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
<div class="adm-login">
  <div class="adm-login-card">
    <div class="adm-login-brand">
      <span class="brand-mark">{icon("diamond")}</span>
      <h1>پنل مدیریت عصرجدید</h1>
      <p>نسخه {fa_num(t)} — برای ورود، اطلاعات حساب مدیریتی خود را وارد کنید.</p>
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
      <button class="btn btn-primary btn-block btn-lg" type="submit">{icon("logout")} ورود به پنل</button>
    </form>
    <div class="adm-login-foot">
      <a href="../index.html">{icon("home")} بازگشت به سایت</a>
      <span class="muted">پشتیبانی فنی: ۰۲۱-۹۱۰۰۲۲۳۳ داخلی ۱۰۵</span>
    </div>
  </div>
  <aside class="adm-login-aside">
    <img src="../assets/images/hero-1.jpg" alt="سنگ مصنوعی عصرجدید">
    <div class="ala-body">
      <h2>مدیریت یکپارچه فروشگاه سنگ مصنوعی</h2>
      <ul class="check-list check-light">
        <li>{icon("check-circle")} مدیریت محصولات، دسته‌بندی‌ها و موجودی انبار</li>
        <li>{icon("check-circle")} پیگیری سفارش‌ها و وضعیت ارسال بار</li>
        <li>{icon("check-circle")} مدیریت مشتریان، نقش‌ها و سطوح دسترسی</li>
        <li>{icon("check-circle")} گزارش فروش، نمودارها و خروجی Excel</li>
      </ul>
      <div class="ala-stats">
        <div><strong>۱۶۱</strong><small>محصول فعال</small></div>
        <div><strong>۳۷</strong><small>سفارش این ماه</small></div>
        <div><strong>۱٬۲۴۸</strong><small>مشتری ثبت‌شده</small></div>
      </div>
    </div>
  </aside>
</div>
<div class="toast-wrap" id="toastWrap"></div>
<script src="../assets/js/admin.js"></script>
</body>
</html>
'''
