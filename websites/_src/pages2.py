# -*- coding: utf-8 -*-
"""صفحات حساب کاربری، پنل مشتری و صفحات حقوقی/کاربردی"""
from data import *
from layouts import icon, stars, product_card, section_head, page_hero, pagination, cat_name
from pages import cta_band

# --------------------------------------------------------------- auth ---- #


def login(t):
    return f'''
<section class="auth-page">
  <div class="container auth-layout">
    <div class="auth-card card">
      <div class="auth-head">
        <span class="auth-logo">{icon("diamond")}</span>
        <h1>ورود به حساب کاربری</h1>
        <p>برای پیگیری سفارش‌ها، لیست قیمت اختصاصی و مدیریت پروژه‌ها وارد شوید.</p>
      </div>
      <div class="notice-bar notice-demo">{icon("alert")}<p>این صفحه نمونه است. برای ورود آزمایشی از شماره <strong>۰۹۱۲۱۱۱۲۲۳۳</strong> و رمز <strong>demo1234</strong> استفاده کنید.</p></div>
      <form class="form js-login js-form" novalidate data-demo-phone="۰۹۱۲۱۱۱۲۲۳۳" data-demo-pass="demo1234">
        <div class="field"><label>شماره همراه یا ایمیل</label>
          <div class="input-icon">{icon("user")}<input type="text" placeholder="۰۹۱۲۱۱۱۲۲۳۳" required></div></div>
        <div class="field"><label>رمز عبور</label>
          <div class="input-icon">{icon("lock")}<input type="password" placeholder="••••••••" required>
            <button class="input-btn js-pass-toggle" type="button" aria-label="نمایش رمز">{icon("eye")}</button></div></div>
        <div class="auth-row">
          <label class="check-row"><input type="checkbox" checked><span>مرا به خاطر بسپار</span></label>
          <a href="forgot-password.html" class="link">رمز عبور را فراموش کرده‌اید؟</a>
        </div>
        <button class="btn btn-primary btn-block btn-lg" type="submit">{icon("logout")} ورود به حساب</button>
      </form>
      <div class="auth-sep"><span>یا ورود با</span></div>
      <div class="auth-social">
        <a class="btn btn-outline" href="#">{icon("tg")} ورود با تلگرام</a>
        <a class="btn btn-outline" href="#">{icon("mail")} ورود با ایمیل</a>
      </div>
      <p class="auth-foot">حساب کاربری ندارید؟ <a href="register.html" class="link">ثبت‌نام کنید</a></p>
      <p class="auth-foot muted">مدیر سایت هستید؟ <a href="admin/login.html" class="link">ورود به پنل مدیریت</a></p>
    </div>
    <aside class="auth-aside">
      <img src="assets/images/hero-2.jpg" alt="عصرجدید">
      <div class="aa-body">
        <h2>مزایای عضویت در عصرجدید</h2>
        <ul class="check-list check-light">
          <li>{icon("check-circle")} مشاهده قیمت اختصاصی همکاران و پروژه‌ها</li>
          <li>{icon("check-circle")} پیگیری آنلاین سفارش و بارنامه</li>
          <li>{icon("check-circle")} ذخیره لیست خرید و مقایسه محصولات</li>
          <li>{icon("check-circle")} دریافت فاکتور رسمی و ضمانت‌نامه دیجیتال</li>
        </ul>
      </div>
    </aside>
  </div>
</section>'''


def register(t):
    return f'''
<section class="auth-page">
  <div class="container auth-layout">
    <div class="auth-card card">
      <div class="auth-head">
        <span class="auth-logo">{icon("user")}</span>
        <h1>ساخت حساب کاربری جدید</h1>
        <p>در کمتر از یک دقیقه ثبت‌نام کنید و از قیمت‌های همکاری بهره‌مند شوید.</p>
      </div>
      <form class="form js-form" novalidate>
        <div class="form-grid">
          <div class="field"><label>نام <span class="req">*</span></label><input type="text" required></div>
          <div class="field"><label>نام خانوادگی <span class="req">*</span></label><input type="text" required></div>
        </div>
        <div class="field"><label>شماره همراه <span class="req">*</span></label>
          <div class="input-icon">{icon("phone")}<input type="tel" placeholder="۰۹۱۲۳۴۵۶۷۸۹" required></div></div>
        <div class="field"><label>ایمیل</label>
          <div class="input-icon">{icon("mail")}<input type="email" placeholder="you@example.com"></div></div>
        <div class="form-grid">
          <div class="field"><label>رمز عبور <span class="req">*</span></label><input type="password" required></div>
          <div class="field"><label>تکرار رمز عبور <span class="req">*</span></label><input type="password" required></div>
        </div>
        <div class="field"><label>نوع حساب کاربری</label><select>
          <option>مشتری شخصی</option><option>معمار / طراح داخلی</option><option>پیمانکار و شرکت ساختمانی</option><option>فروشگاه و نمایندگی</option></select></div>
        <label class="check-row"><input type="checkbox" required><span>قوانین و مقررات و <a href="privacy.html" class="link">سیاست حریم خصوصی</a> را می‌پذیرم.</span></label>
        <label class="check-row"><input type="checkbox" checked><span>مایل به دریافت خبرنامه و پیشنهادهای ویژه هستم.</span></label>
        <button class="btn btn-primary btn-block btn-lg" type="submit">{icon("check-circle")} تکمیل ثبت‌نام</button>
      </form>
      <p class="auth-foot">قبلاً ثبت‌نام کرده‌اید؟ <a href="login.html" class="link">ورود به حساب</a></p>
    </div>
    <aside class="auth-aside">
      <img src="assets/images/cat-1.jpg" alt="نمای سنگ مصنوعی">
      <div class="aa-body">
        <h2>حساب همکاری حرفه‌ای</h2>
        <p>اگر معمار، طراح داخلی یا پیمانکار هستید، حساب خود را با نوع «همکاری» ثبت کنید تا به لیست قیمت ویژه، شرایط پرداخت اعتباری و مشاوره فنی اختصاصی دسترسی داشته باشید.</p>
        <div class="auth-stat"><strong>٪۸</strong><span>تخفیف پلکانی پروژه‌های انبوه</span></div>
      </div>
    </aside>
  </div>
</section>'''


def forgot(t):
    return f'''
<section class="auth-page">
  <div class="container auth-narrow">
    <div class="auth-card card">
      <div class="auth-head">
        <span class="auth-logo">{icon("lock")}</span>
        <h1>بازیابی رمز عبور</h1>
        <p>شماره همراه خود را وارد کنید؛ کد تأیید برای شما پیامک می‌شود.</p>
      </div>
      <form class="form js-form" novalidate>
        <div class="field"><label>شماره همراه ثبت‌شده</label>
          <div class="input-icon">{icon("phone")}<input type="tel" placeholder="۰۹۱۲۳۴۵۶۷۸۹" required></div></div>
        <div class="otp-row js-otp">
          <input type="text" maxlength="1" inputmode="numeric" aria-label="رقم ۱">
          <input type="text" maxlength="1" inputmode="numeric" aria-label="رقم ۲">
          <input type="text" maxlength="1" inputmode="numeric" aria-label="رقم ۳">
          <input type="text" maxlength="1" inputmode="numeric" aria-label="رقم ۴">
          <input type="text" maxlength="1" inputmode="numeric" aria-label="رقم ۵">
        </div>
        <div class="auth-row">
          <span class="muted">کد را دریافت نکردید؟</span>
          <button class="link js-resend" type="button">ارسال مجدد کد (<span class="js-timer">۰۱:۳۰</span>)</button>
        </div>
        <button class="btn btn-primary btn-block btn-lg" type="submit">{icon("check-circle")} تأیید و تغییر رمز</button>
      </form>
      <div class="auth-sep"><span>مراحل بازیابی</span></div>
      <ol class="auth-steps">
        <li>{icon("check-circle")} وارد کردن شماره همراه ثبت‌شده</li>
        <li>{icon("check-circle")} تأیید کد پیامک‌شده</li>
        <li>{icon("check-circle")} تعیین رمز عبور جدید</li>
      </ol>
      <p class="auth-foot">شماره همراه خود را به یاد ندارید؟ <a href="contact.html" class="link">با پشتیبانی تماس بگیرید</a></p>
    </div>
  </div>
</section>'''


# ------------------------------------------------------------ account ---- #
def _user_side(active):
    items = [
        ("dashboard.html", "dashboard", "داشبورد", "dashboard"),
        ("orders.html", "orders", "سفارش‌های من", "cart"),
        ("wishlist.html", "wishlist", "علاقه‌مندی‌ها", "heart"),
        ("compare.html", "compare", "مقایسه محصولات", "sort"),
    ]
    li = "".join(
        f'<li><a class="{"active" if slug == active else ""}" href="{href}">{icon(ico_name)}'
        f'<span>{label}</span><i>{icon("chev-left")}</i></a></li>'
        for href, slug, label, ico_name in items)
    other = f'''
    <li class="side-group">حساب کاربری</li>
    <li><a href="profile.html">{icon("user")}<span>اطلاعات حساب</span><i>{icon("chev-left")}</i></a></li>
    <li><a href="login.html">{icon("logout")}<span>خروج از حساب</span><i>{icon("chev-left")}</i></a></li>'''
    return f'''
<aside class="panel-side">
  <div class="ps-user">
    <span class="avatar avatar-xl">{DEMO_USER['initials']}</span>
    <div><strong>{DEMO_USER['name']}</strong><small>{DEMO_USER['level']}</small></div>
  </div>
  <ul class="ps-nav">{li}{other}</ul>
  <div class="ps-help">{icon("help")}<p>پشتیبانی سفارش‌ها</p><a href="tel:{SITE['phone_link']}">{SITE['phone']}</a></div>
</aside>'''


def dashboard(t):
    order_rows = ""
    for o in ORDERS_DEMO[:3]:
        order_rows += f'''<tr>
      <td><a href="order.html" class="link">{o['code']}</a></td><td>{o['date']}</td>
      <td>{fa_num(o['items'])} قلم</td><td>{money(o['total'])}</td>
      <td><span class="status status-{o['status_key']}">{o['status']}</span></td>
      <td><a class="icon-btn sm" href="order.html" title="جزئیات">{icon("eye")}</a></td></tr>'''
    return f'''
<section class="panel-page">
  <div class="container panel-layout">
    {_user_side("dashboard")}
    <div class="panel-main">
      <div class="panel-head">
        <div><h1>سلام {DEMO_USER['name'].split()[-1]} 👋</h1>
          <p class="muted">خوش آمدید! وضعیت سفارش‌ها و علاقه‌مندی‌های شما در یک نگاه.</p></div>
        <a class="btn btn-primary" href="products.html">{icon("cart")} خرید جدید</a>
      </div>
      <div class="panel-cards">
        <div class="p-card"><span class="pc-ico">{icon("cart")}</span><div><strong>{fa_num(len(ORDERS_DEMO))}</strong><small>سفارش ثبت‌شده</small></div></div>
        <div class="p-card"><span class="pc-ico">{icon("heart")}</span><div><strong>{fa_num(len(WISHLIST_DEMO))}</strong><small>محصول در علاقه‌مندی</small></div></div>
        <div class="p-card"><span class="pc-ico">{icon("wallet")}</span><div><strong>{fa_num(DEMO_USER['points'])}</strong><small>امتیاز باشگاه مشتریان</small></div></div>
        <div class="p-card"><span class="pc-ico">{icon("gift")}</span><div><strong>٪۳</strong><small>سطح تخفیف فعلی شما</small></div></div>
      </div>
      <div class="grid grid-2">
        <div class="card">
          <div class="card-head-row"><h3 class="card-title">{icon("cart")} آخرین سفارش‌ها</h3><a class="link-more" href="orders.html">همه سفارش‌ها {icon("arrow-left")}</a></div>
          <div class="table-wrap"><table class="table table-compact">
            <thead><tr><th>کد سفارش</th><th>تاریخ</th><th>اقلام</th><th>مبلغ</th><th>وضعیت</th><th></th></tr></thead>
            <tbody>{order_rows}</tbody></table></div>
        </div>
        <div class="card">
          <div class="card-head-row"><h3 class="card-title">{icon("shield")} وضعیت حساب</h3></div>
          <ul class="account-status">
            <li>{icon("check-circle")}<span>شماره همراه تأیید شده</span><strong>{DEMO_USER['phone']}</strong></li>
            <li>{icon("check-circle")}<span>ایمیل ثبت‌شده</span><strong>{DEMO_USER['email']}</strong></li>
            <li>{icon("alert")}<span>تکمیل آدرس تحویل بار</span><a href="profile.html" class="link">تکمیل اطلاعات</a></li>
            <li>{icon("check-circle")}<span>عضویت از تاریخ</span><strong>{DEMO_USER['member_since']}</strong></li>
          </ul>
          <div class="progress-note">
            <div class="pn-head"><span>تکمیل پروفایل</span><strong>۸۵٪</strong></div>
            <div class="pn-bar"><b style="width:85%"></b></div>
            <p class="muted">با تکمیل آدرس و بارگذاری کارت ملی، از تخفیف‌های سطح طلایی بهره‌مند می‌شوید.</p>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-head-row"><h3 class="card-title">{icon("heart")} علاقه‌مندی‌های اخیر</h3><a class="link-more" href="wishlist.html">مشاهده همه {icon("arrow-left")}</a></div>
        <div class="grid grid-3">{''.join(product_card(s, compact=True) for s in [STONES[0], STONES[7], STONES[10]])}</div>
      </div>
      <div class="card side-cta">
        {icon("chat")}
        <div><h3>مشاوره اختصاصی پروژه</h3><p>اگر در حال برنامه‌ریزی برای پروژه‌ای هستید، کارشناس فنی ما می‌تواند برآورد متراژ و هزینه را برای شما تهیه کند.</p></div>
        <a class="btn btn-primary" href="contact.html">درخواست مشاوره</a>
      </div>
    </div>
  </div>
</section>'''


def orders(t):
    rows = ""
    for o in ORDERS_DEMO:
        rows += f'''<tr>
      <td><a href="order.html" class="link">{o['code']}</a></td>
      <td>{o['date']}</td>
      <td>{fa_num(o['items'])} قلم</td>
      <td>{o['pay']}</td>
      <td>{money(o['total'])}</td>
      <td><span class="status status-{o['status_key']}">{o['status']}</span></td>
      <td class="row-actions">
        <a class="icon-btn sm" href="order.html" title="جزئیات">{icon("eye")}</a>
        <button class="icon-btn sm" type="button" title="دانلود فاکتور">{icon("download")}</button>
        <button class="icon-btn sm danger" type="button" title="لغو سفارش">{icon("x-circle")}</button>
      </td></tr>'''
    return f'''
<section class="panel-page">
  <div class="container panel-layout">
    {_user_side("orders")}
    <div class="panel-main">
      <div class="panel-head">
        <div><h1>سفارش‌های من</h1><p class="muted">پیگیری وضعیت، دانلود فاکتور و ثبت سفارش مجدد.</p></div>
        <a class="btn btn-primary" href="products.html">{icon("plus")} ثبت سفارش جدید</a>
      </div>
      <div class="filter-chips panel-chips">
        <button class="chip-btn active" type="button">همه سفارش‌ها</button>
        <button class="chip-btn" type="button">در انتظار پرداخت</button>
        <button class="chip-btn" type="button">در حال آماده‌سازی</button>
        <button class="chip-btn" type="button">در حال ارسال</button>
        <button class="chip-btn" type="button">تحویل شده</button>
      </div>
      <div class="card">
        <div class="table-wrap"><table class="table table-compact">
          <thead><tr><th>کد سفارش</th><th>تاریخ</th><th>اقلام</th><th>شیوه پرداخت</th><th>مبلغ کل</th><th>وضعیت</th><th></th></tr></thead>
          <tbody>{rows}</tbody></table></div>
      </div>
      <div class="card info-card">
        <span class="svc-icon">{icon("help")}</span>
        <h3 class="card-title">پیگیری بار و بارنامه</h3>
        <p class="card-text">کد رهگیری بارنامه پس از تحویل بار به باربری، در همین صفحه و پیامک برای شما ارسال می‌شود. برای پیگیری فوری، شماره سفارش را به واحد پشتیبانی اعلام کنید.</p>
        <a class="btn btn-outline" href="contact.html">{icon("chat")} تماس با پشتیبانی</a>
      </div>
    </div>
  </div>
</section>'''


def order(t):
    o = ORDER_DEMO
    items = ""
    sub = 0
    for it in o["items"]:
        s = next(x for x in STONES if x["id"] == it["id"])
        line = s["price"] * it["qty"]
        sub += line
        items += f'''<tr>
      <td class="ci-prod"><a href="product.html" class="ci-media"><img src="assets/images/{s['image']}" alt="{s['name']}"></a>
        <div class="ci-info"><a href="product.html" class="ci-name">{s['name']}</a>
        <span class="ci-meta">کد {s['code']} • {fa_num(it['qty'])} {s['unit']}</span></div></td>
      <td>{money(s['price'])}</td><td>{fa_num(it['qty'])}</td><td>{money(line)}</td></tr>'''
    tax = int(sub * 0.09)
    tl = "".join(f'''<div class="ot-step{' done' if done else ''}">
      <span class="ot-dot">{icon("check") if done else icon("clock")}</span>
      <div><strong>{title}</strong><small>{when}</small></div></div>''' for title, when, done in o["timeline"])
    return f'''
<section class="panel-page">
  <div class="container panel-layout">
    {_user_side("orders")}
    <div class="panel-main">
      <div class="panel-head">
        <div><h1>سفارش {o['code']}</h1><p class="muted">تاریخ ثبت: {o['date']} • وضعیت: <span class="status status-shipping">{o['status']}</span></p></div>
        <div class="panel-head-actions">
          <button class="btn btn-outline" type="button">{icon("print")} چاپ فاکتور</button>
          <button class="btn btn-primary" type="button">{icon("download")} دانلود PDF</button>
        </div>
      </div>
      <div class="card">
        <h3 class="card-title">{icon("truck")} روند سفارش</h3>
        <div class="order-timeline">{tl}</div>
      </div>
      <div class="grid grid-2">
        <div class="card">
          <h3 class="card-title">{icon("pin")} اطلاعات ارسال</h3>
          <ul class="kv-list">
            <li><span>گیرنده</span><strong>{DEMO_USER['name']}</strong></li>
            <li><span>شماره تماس</span><strong>{DEMO_USER['phone']}</strong></li>
            <li><span>نشانی</span><strong>{o['address']}</strong></li>
            <li><span>شیوه ارسال</span><strong>{o['shipping']}</strong></li>
          </ul>
        </div>
        <div class="card">
          <h3 class="card-title">{icon("credit-card")} اطلاعات پرداخت</h3>
          <ul class="kv-list">
            <li><span>شیوه پرداخت</span><strong>{o['pay']}</strong></li>
            <li><span>تاریخ پرداخت</span><strong>{o['date']} – ۱۰:۳۱</strong></li>
            <li><span>کد پیگیری بانکی</span><strong>۹۸۴۵۲۱۷۷۳۳</strong></li>
            <li><span>وضعیت فاکتور</span><strong>صادر شده (قابل دانلود)</strong></li>
          </ul>
        </div>
      </div>
      <div class="card">
        <h3 class="card-title">{icon("package")} اقلام سفارش</h3>
        <div class="table-wrap"><table class="table cart-table">
          <thead><tr><th>محصول</th><th>قیمت واحد</th><th>تعداد</th><th>جمع</th></tr></thead>
          <tbody>{items}</tbody></table></div>
        <div class="order-total">
          <ul class="sum-list">
            <li><span>جمع کالاها</span><strong>{money(sub)}</strong></li>
            <li><span>مالیات بر ارزش افزوده</span><strong>{money(tax)}</strong></li>
            <li><span>هزینه حمل</span><strong>{money(1850000)}</strong></li>
          </ul>
          <div class="sum-total"><span>مبلغ نهایی</span><strong>{money(sub + tax + 1850000)}</strong></div>
        </div>
      </div>
      <div class="card side-cta">
        {icon("refresh")}
        <div><h3>خرید مجدد این سفارش</h3><p>می‌خواهید همین اقلام را دوباره سفارش دهید؟ با یک کلیک همه اقلام به سبد خرید اضافه می‌شوند.</p></div>
        <a class="btn btn-primary" href="cart.html">{icon("cart")} افزودن همه به سبد</a>
      </div>
    </div>
  </div>
</section>'''


def wishlist(t):
    items = "".join(product_card(s) for s in [next(x for x in STONES if x["id"] == i) for i in WISHLIST_DEMO])
    return f'''
<section class="panel-page">
  <div class="container panel-layout">
    {_user_side("wishlist")}
    <div class="panel-main">
      <div class="panel-head">
        <div><h1>علاقه‌مندی‌های من</h1><p class="muted">{fa_num(len(WISHLIST_DEMO))} محصول ذخیره‌شده — قیمت‌ها به‌صورت خودکار به‌روزرسانی می‌شوند.</p></div>
        <button class="btn btn-primary" type="button">{icon("cart")} افزودن همه به سبد خرید</button>
      </div>
      <div class="grid grid-3">{items}</div>
      <div class="card info-card">
        <span class="svc-icon">{icon("bell")}</span>
        <h3 class="card-title">اطلاع از تغییر قیمت</h3>
        <p class="card-text">با فعال‌سازی اعلان، هر زمان قیمت یا موجودی محصولات مورد علاقه شما تغییر کند، پیامک و ایمیل دریافت می‌کنید.</p>
        <label class="switch-row"><input type="checkbox" checked><span class="switch"></span><span>فعال‌سازی اعلان تغییر قیمت</span></label>
      </div>
    </div>
  </div>
</section>'''


def compare(t):
    items = [next(x for x in STONES if x["id"] == i) for i in COMPARE_DEMO]
    heads = "".join(f'''<th><div class="cmp-head"><a href="product.html"><img src="assets/images/{s['image']}" alt="{s['name']}"></a>
      <a href="product.html" class="cmp-name">{s['name']}</a>{stars(s['rate'])}</div></th>''' for s in items)
    def row(label, key, money_fmt=False):
        cells = ""
        for s in items:
            val = s.get(key, "—")
            if money_fmt:
                val = f'{fa_num(val)} تومان'
            elif isinstance(val, int):
                val = fa_num(val)
            cells += f"<td>{val}</td>"
        return f"<tr><th>{label}</th>{cells}</tr>"
    rows = "".join([
        row("دسته‌بندی", "cat"),
        '<tr><th>قیمت واحد</th>' + "".join('<td class="cmp-price">' + fa_num(s['price']) + ' تومان</td>' for s in items) + '</tr>',
        row("واحد فروش", "unit"), row("ابعاد", "size"), row("ضخامت", "thickness"),
        row("رنگ", "color"), row("موجودی انبار", "stock"), row("امتیاز کاربران", "rate"),
    ])
    return f'''
<section class="panel-page">
  <div class="container panel-layout">
    {_user_side("compare")}
    <div class="panel-main">
      <div class="panel-head">
        <div><h1>مقایسه محصولات</h1><p class="muted">{fa_num(len(items))} محصول در جدول مقایسه — برای افزودن یا حذف، از صفحه محصولات استفاده کنید.</p></div>
        <button class="btn btn-outline" type="button">{icon("trash")} پاک کردن جدول</button>
      </div>
      <div class="table-wrap card">
        <table class="table compare-table">
          <thead><tr><th>ویژگی</th>{heads}</tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
      <div class="cmp-actions">
        <a class="btn btn-primary btn-lg" href="cart.html">{icon("cart")} افزودن همه به سبد خرید</a>
        <a class="btn btn-outline btn-lg" href="products.html">{icon("plus")} افزودن محصول به مقایسه</a>
      </div>
      <div class="card info-card">
        <span class="svc-icon">{icon("chat")}</span>
        <h3 class="card-title">هنوز مطمئن نیستید کدام محصول مناسب است؟</h3>
        <p class="card-text">کارشناسان فنی عصرجدید با بررسی کاربری فضا و بودجه پروژه، در انتخاب بین این محصولات شما را راهنمایی می‌کنند.</p>
        <a class="btn btn-primary" href="contact.html">درخواست مشاوره تخصصی</a>
      </div>
    </div>
  </div>
</section>'''


# ------------------------------------------------------- legal & misc ---- #
def terms(t):
    blocks = "".join(f'''<div class="legal-block">
      <h2>{icon("check-circle")} {title}</h2><p>{text}</p></div>''' for title, text in TERMS)
    return f'''
{page_hero("قوانین و مقررات", "شرایط خرید، ارسال، ضمانت و مرجوعی در فروشگاه عصرجدید", [("صفحه اصلی", "index.html"), ("قوانین و مقررات", "")])}
<section class="section">
  <div class="container legal-layout">
    <aside class="side-card">
      <h3 class="side-title-static">{icon("list-view")} فهرست بندها</h3>
      <ul class="side-nav">{''.join(f'<li><a href="#b{i}">{title}<span>{fa_num(i + 1)}</span></a></li>' for i, (title, _) in enumerate(TERMS))}</ul>
      <div class="side-help">{icon("help")}<h3>پرسشی دارید؟</h3><p>واحد پشتیبانی پاسخ‌گوی شماست.</p>
        <a class="btn btn-primary btn-block" href="contact.html">تماس با پشتیبانی</a></div>
    </aside>
    <div class="legal-main">
      <div class="notice-bar">{icon("alert")}<p>آخرین به‌روزرسانی این سند: <strong>۱۴۰۴/۰۶/۰۱</strong> — استفاده از فروشگاه به معنای پذیرش این شرایط است.</p></div>
      <div class="prose">{blocks}</div>
      <div class="card info-card">
        <span class="svc-icon">{icon("file")}</span>
        <h3 class="card-title">دریافت نسخه PDF قرارداد فروش</h3>
        <p class="card-text">برای پروژه‌های سازمانی، نسخه رسمی قرارداد تأمین کالا با شرایط اختصاصی قابل تنظیم است.</p>
        <a class="btn btn-outline" href="contact.html">{icon("download")} درخواست نسخه رسمی</a>
      </div>
    </div>
  </div>
</section>'''


def privacy(t):
    blocks = "".join(f'''<div class="legal-block">
      <h2>{icon("lock")} {title}</h2><p>{text}</p></div>''' for title, text in PRIVACY)
    return f'''
{page_hero("حریم خصوصی", "نحوه جمع‌آوری، استفاده و نگهداری اطلاعات کاربران عصرجدید", [("صفحه اصلی", "index.html"), ("حریم خصوصی", "")])}
<section class="section">
  <div class="container legal-layout">
    <aside class="side-card">
      <h3 class="side-title-static">{icon("list-view")} سرفصل‌ها</h3>
      <ul class="side-nav">{''.join(f'<li><a href="#p{i}">{title}<span>{fa_num(i + 1)}</span></a></li>' for i, (title, _) in enumerate(PRIVACY))}</ul>
      <div class="side-help">{icon("shield")}<h3>امنیت اطلاعات</h3><p>ارتباط شما با سایت روی HTTPS رمزنگاری می‌شود.</p></div>
    </aside>
    <div class="legal-main">
      <div class="notice-bar">{icon("alert")}<p>ما هیچ‌گاه اطلاعات شما را نمی‌فروشیم و فقط برای ارائه بهتر خدمات از آن استفاده می‌کنیم.</p></div>
      <div class="prose">{blocks}</div>
      <div class="card info-card">
        <span class="svc-icon">{icon("mail")}</span>
        <h3 class="card-title">درخواست حذف یا اصلاح اطلاعات</h3>
        <p class="card-text">برای حذف حساب کاربری یا اصلاح اطلاعات شخصی، از طریق ایمیل پشتیبانی با ما در تماس باشید.</p>
        <a class="btn btn-primary" href="mailto:{SITE['email']}">{icon("mail")} {SITE['email']}</a>
      </div>
    </div>
  </div>
</section>'''


def sitemap(t):
    cols = "".join(f'''<div class="card sitemap-col">
      <h3 class="card-title">{icon("link")} {g['name']}</h3>
      <ul class="side-nav">{''.join(f'<li><a href="{h}">{n}<span>{icon("arrow-left")}</span></a></li>' for n, h in g['items'])}</ul>
    </div>''' for g in SITEMAP_TREE)
    return f'''
{page_hero("نقشه سایت", "دسترسی سریع به همه صفحات سایت عصرجدید", [("صفحه اصلی", "index.html"), ("نقشه سایت", "")])}
<section class="section">
  <div class="container">
    {section_head("ساختار سایت", "همه صفحه‌ها در یک نگاه", "برای دسترسی سریع، از دسته‌بندی‌های زیر استفاده کنید.")}
    <div class="grid grid-3 sitemap-grid">{cols}</div>
  </div>
</section>
{cta_band("صفحه مورد نظر را پیدا نکردید؟", "با جستجوی سایت یا کارشناسان ما، سریع‌تر به پاسخ می‌رسید.")}'''


def notfound(t):
    return f'''
<section class="error-page">
  <div class="container">
    <div class="error-code">۴۰۴</div>
    <h1>صفحه مورد نظر پیدا نشد</h1>
    <p>ممکن است آدرس تغییر کرده باشد یا صفحه حذف شده باشد. از راه‌های زیر ادامه دهید:</p>
    <div class="error-actions">
      <a class="btn btn-primary btn-lg" href="index.html">{icon("home")} بازگشت به صفحه اصلی</a>
      <a class="btn btn-outline btn-lg" href="products.html">{icon("grid")} مشاهده محصولات</a>
      <a class="btn btn-ghost btn-lg" href="contact.html">{icon("chat")} تماس با پشتیبانی</a>
    </div>
    <form class="form error-search js-form" novalidate>
      <div class="field"><input type="search" placeholder="جستجو در سایت… مثلاً: نانوسنگ نما" aria-label="جستجو"></div>
      <button class="btn btn-dark" type="submit">{icon("search")} جستجو</button>
    </form>
    <div class="error-links">
      <span>لینک‌های پرطرفدار:</span>
      <a href="categories.html">دسته‌بندی محصولات</a>
      <a href="price-list.html">لیست قیمت ۱۴۰۴</a>
      <a href="faq.html">سوالات متداول</a>
      <a href="blog.html">مقالات</a>
      <a href="gallery.html">گالری تصاویر</a>
    </div>
  </div>
</section>'''


def search(t):
    results = "".join(product_card(s) for s in STONES[:6])
    return f'''
{page_hero("نتایج جستجو", "جستجو برای: «نانوسنگ» — ۱۸ نتیجه در محصولات و مقالات", [("صفحه اصلی", "index.html"), ("نتایج جستجو", "")])}
<section class="section">
  <div class="container search-layout">
    <aside class="search-side">
      <div class="card">
        <h3 class="card-title">{icon("search")} جستجوی دوباره</h3>
        <form class="form js-form" novalidate>
          <div class="field"><input type="search" value="نانوسنگ" aria-label="جستجو"></div>
          <button class="btn btn-primary btn-block" type="submit">جستجو</button>
        </form>
      </div>
      <div class="card">
        <h3 class="card-title">{icon("filter")} محدود کردن نتایج</h3>
        <div class="side-body">
          <label class="check-row"><input type="radio" name="rtype" checked><span>همه نتایج</span><small>(۱۸)</small></label>
          <label class="check-row"><input type="radio" name="rtype"><span>محصولات</span><small>(۱۲)</small></label>
          <label class="check-row"><input type="radio" name="rtype"><span>مقالات</span><small>(۴)</small></label>
          <label class="check-row"><input type="radio" name="rtype"><span>پروژه‌ها</span><small>(۲)</small></label>
        </div>
      </div>
      <div class="card">
        <h3 class="card-title">{icon("tag")} جستجوهای مرتبط</h3>
        <div class="tag-cloud">
          <a href="#">نانوسنگ نما</a><a href="#">تراورتن مصنوعی</a><a href="#">پنل سه‌بعدی</a>
          <a href="#">آجرنما</a><a href="#">صفحه کوارتز</a><a href="#">کورین</a>
        </div>
      </div>
    </aside>
    <div class="search-main">
      <div class="toolbar">
        <div class="toolbar-right"><span class="tb-count">۱۸ نتیجه در ۰٫۱۲ ثانیه</span></div>
        <div class="toolbar-left">
          <label class="sort-select">{icon("sort")}<select aria-label="ترتیب">
            <option>مرتب‌سازی: بیشترین ارتباط</option><option>ارزان‌ترین</option><option>گران‌ترین</option><option>جدیدترین</option></select></label>
        </div>
      </div>
      <div class="grid grid-3">{results}</div>
      <div class="card info-card">
        <span class="svc-icon">{icon("file")}</span>
        <h3 class="card-title">۴ مقاله مرتبط با «نانوسنگ»</h3>
        <ul class="side-nav">{''.join(f'<li><a href="article.html">{a["title"]}<span>{icon("arrow-left")}</span></a></li>' for a in ARTICLES[:4])}</ul>
      </div>
      <div class="shop-pagination">{pagination(1, 3)}</div>
    </div>
  </div>
</section>'''


def profile(t):
    return f'''
<section class="panel-page">
  <div class="container panel-layout">
    {_user_side("dashboard")}
    <div class="panel-main">
      <div class="panel-head">
        <div><h1>اطلاعات حساب کاربری</h1><p class="muted">اطلاعات شخصی و آدرس‌های تحویل بار خود را مدیریت کنید.</p></div>
      </div>
      <div class="grid grid-2">
        <form class="card form-card js-form" novalidate>
          <h3 class="card-title">{icon("user")} اطلاعات شخصی</h3>
          <div class="form-grid">
            <div class="field"><label>نام</label><input type="text" value="رضا"></div>
            <div class="field"><label>نام خانوادگی</label><input type="text" value="محمدی"></div>
            <div class="field"><label>شماره همراه</label><input type="tel" value="{DEMO_USER['phone']}"></div>
            <div class="field"><label>ایمیل</label><input type="email" value="{DEMO_USER['email']}"></div>
            <div class="field"><label>کد ملی</label><input type="text" placeholder="۱۰ رقم"></div>
            <div class="field"><label>تاریخ تولد</label><input type="text" placeholder="۱۳۷۰/۰۵/۱۲"></div>
          </div>
          <div class="form-actions"><button class="btn btn-primary" type="submit">{icon("save")} ذخیره تغییرات</button></div>
        </form>
        <div class="stack-forms">
          <form class="card form-card js-form" novalidate>
            <h3 class="card-title">{icon("lock")} تغییر رمز عبور</h3>
            <div class="field"><label>رمز عبور فعلی</label><input type="password"></div>
            <div class="field"><label>رمز عبور جدید</label><input type="password"></div>
            <div class="field"><label>تکرار رمز عبور جدید</label><input type="password"></div>
            <div class="form-actions"><button class="btn btn-outline" type="submit">{icon("refresh")} تغییر رمز</button></div>
          </form>
          <form class="card form-card js-form" novalidate>
            <h3 class="card-title">{icon("pin")} آدرس تحویل بار</h3>
            <div class="field"><label>استان / شهر</label><input type="text" value="تهران"></div>
            <div class="field"><label>نشانی کامل</label><textarea rows="3">تهران، سعادت‌آباد، خیابان علامه شمالی، پلاک ۱۲۴، واحد ۷</textarea></div>
            <div class="field"><label>کد پستی</label><input type="text" value="۱۹۹۸۷۶۵۴۳۲"></div>
            <div class="form-actions"><button class="btn btn-primary" type="submit">{icon("save")} ذخیره آدرس</button></div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>'''
