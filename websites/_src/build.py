# -*- coding: utf-8 -*-
"""ساخت دو پوسته کامل سایت + پنل مدیریت عصرجدید
خروجی: websites/1-asrjadid-classic و websites/2-asrjadid-modern
"""
import os
import shutil

import admin as admp
import pages as pg
import pages2 as pg2
from layouts import page, admin_page, ADMIN_NAV

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(ROOT)

SITE_PAGES = [
    ("index.html", "صفحه اصلی", "index.html", pg.index, "سنگ مصنوعی عصرجدید؛ نانوسنگ نما، صفحات کوارتز و کورین، پنل سه‌بعدی و آجرنما با ۱۹ سال سابقه تولید"),
    ("about.html", "درباره ما", "about.html", pg.about, "معرفی شرکت عصرجدید، تاریخچه، ارزش‌ها، گواهی‌نامه‌ها و تیم"),
    ("categories.html", "دسته‌بندی محصولات", "categories.html", pg.categories, "شش گروه محصول سنگ مصنوعی عصرجدید"),
    ("products.html", "محصولات", "products.html", pg.products, "لیست محصولات سنگ مصنوعی با فیلتر قیمت، رنگ و دسته‌بندی"),
    ("product.html", "جزئیات محصول", "products.html", pg.product, "مشخصات فنی، گالری، دیدگاه‌ها و راهنمای نصب محصول"),
    ("category.html", "آرشیو دسته‌بندی", "categories.html", pg.category, "آرشیو محصولات یک دسته‌بندی نمونه"),
    ("services.html", "خدمات", "services.html", pg.services, "خدمات مشاوره، اندازه‌گیری، اجرا، برش CNC و خدمات پس از فروش"),
    ("service.html", "جزئیات خدمت", "services.html", pg.service, "جزئیات خدمت اجرای تخصصی و نصب"),
    ("projects.html", "پروژه‌های اجرایی", "projects.html", pg.projects, "نمونه پروژه‌های اجراشده با محصولات عصرجدید"),
    ("project.html", "جزئیات پروژه", "projects.html", pg.project, "شرح و جزئیات یک پروژه اجرایی نمونه"),
    ("gallery.html", "گالری تصاویر", "gallery.html", pg.gallery, "گالری تصاویر محصولات و پروژه‌های عصرجدید"),
    ("blog.html", "وبلاگ", "blog.html", pg.blog, "مقالات تخصصی سنگ مصنوعی، راهنمای خرید و مقایسه محصولات"),
    ("article.html", "جزئیات مقاله", "blog.html", pg.article, "مطالعه کامل مقاله راهنمای خرید سنگ مصنوعی"),
    ("price-list.html", "لیست قیمت ۱۴۰۴", "price-list.html", pg.price_list, "لیست قیمت به‌روز محصولات عصرجدید"),
    ("cart.html", "سبد خرید", "", pg.cart, "سبد خرید و خلاصه سفارش"),
    ("checkout.html", "تسویه حساب", "", pg.checkout, "تکمیل اطلاعات ارسال و پرداخت سفارش"),
    ("contact.html", "تماس با ما", "contact.html", pg.contact, "فرم تماس، اطلاعات شعب و ساعت کاری عصرجدید"),
    ("faq.html", "سوالات متداول", "faq.html", pg.faq, "پاسخ پرسش‌های متداول مشتریان"),
    ("careers.html", "فرصت‌های شغلی", "careers.html", pg.careers, "فرصت‌های شغلی فعال در شرکت عصرجدید"),
    ("job.html", "جزئیات موقعیت شغلی", "careers.html", pg.job, "شرح موقعیت شغلی و فرم ارسال رزومه"),
    ("search.html", "نتایج جستجو", "", pg2.search, "نتایج جستجوی محصولات و مقالات"),
    ("login.html", "ورود به حساب", "", pg2.login, "ورود کاربران به حساب کاربری عصرجدید"),
    ("register.html", "ثبت‌نام", "", pg2.register, "ساخت حساب کاربری جدید در عصرجدید"),
    ("forgot-password.html", "بازیابی رمز عبور", "", pg2.forgot, "بازیابی رمز عبور با کد پیامکی"),
    ("dashboard.html", "پنل کاربری", "", pg2.dashboard, "داشبورد کاربری مشتریان عصرجدید"),
    ("orders.html", "سفارش‌های من", "", pg2.orders, "فهرست سفارش‌های ثبت‌شده کاربر"),
    ("order.html", "جزئیات سفارش", "", pg2.order, "جزئیات یک سفارش نمونه با روند ارسال"),
    ("wishlist.html", "علاقه‌مندی‌ها", "", pg2.wishlist, "محصولات ذخیره‌شده در علاقه‌مندی‌ها"),
    ("compare.html", "مقایسه محصولات", "", pg2.compare, "جدول مقایسه مشخصات محصولات"),
    ("profile.html", "اطلاعات حساب", "", pg2.profile, "ویرایش اطلاعات حساب کاربری و آدرس‌ها"),
    ("terms.html", "قوانین و مقررات", "", pg2.terms, "شرایط خرید، ارسال، ضمانت و مرجوعی"),
    ("privacy.html", "حریم خصوصی", "", pg2.privacy, "سیاست حفظ حریم خصوصی کاربران"),
    ("sitemap.html", "نقشه سایت", "", pg2.sitemap, "دسترسی سریع به همه صفحات سایت"),
    ("404.html", "صفحه یافت نشد", "", pg2.notfound, "صفحه خطای ۴۰۴ عصرجدید"),
]

ADMIN_PAGES = [
    ("dashboard.html", "داشبورد مدیریت", "dashboard", admp.dashboard, "نمودار فروش، سفارش‌های اخیر و وضعیت انبار"),
    ("products.html", "مدیریت محصولات", "products.html", admp.products, "لیست، فیلتر و عملیات گروهی محصولات"),
    ("product-form.html", "افزودن / ویرایش محصول", "product-form.html", admp.product_form, "فرم کامل ثبت محصول با تصاویر و مشخصات فنی"),
    ("categories.html", "مدیریت دسته‌بندی‌ها", "categories.html", admp.categories, "افزودن و ویرایش گروه‌های محصول"),
    ("orders.html", "مدیریت سفارش‌ها", "orders.html", admp.orders, "پیگیری وضعیت سفارش‌ها و فاکتورها"),
    ("comments.html", "مدیریت دیدگاه‌ها", "comments.html", admp.comments, "تأیید، پاسخ و مدیریت دیدگاه محصولات"),
    ("customers.html", "مدیریت مشتریان", "customers.html", admp.customers, "فهرست کاربران، نقش‌ها و وضعیت حساب"),
    ("roles.html", "نقش‌ها و دسترسی‌ها", "roles.html", admp.roles, "تعریف نقش و ماتریس سطوح دسترسی"),
    ("profile.html", "پروفایل مدیر", "profile.html", admp.profile, "اطلاعات حساب مدیر و امنیت ورود"),
    ("settings.html", "تنظیمات سایت", "settings.html", admp.settings, "تنظیمات عمومی، تماس، ارسال، پرداخت و سئو"),
]

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#c9a227"/><stop offset="1" stop-color="#8a6a1f"/></linearGradient></defs>
  <rect width="64" height="64" rx="14" fill="#2c231b"/>
  <path d="M32 10 52 24 32 54 12 24 32 10Z" fill="url(#g)"/>
  <path d="M12 24h40M32 10v44" stroke="#2c231b" stroke-width="2.4" fill="none"/>
</svg>
'''

THEMES = {
    1: "1-asrjadid-classic",
    2: "2-asrjadid-modern",
}
THEME_TITLES = {1: "پوسته ۱ — کلاسیک لوکس", 2: "پوسته ۲ — مدرن شهری"}


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def read_src(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return f.read()


def copy_assets(dest, t):
    """CSS هر پوسته از ترکیب «پایه مشترک + تم» ساخته می‌شود و به‌صورت یک فایل مستقل تحویل داده می‌شود."""
    for sub in ("images", "fonts"):
        src = os.path.join(ROOT, "assets", sub)
        dst = os.path.join(dest, "assets", sub)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)

    shared = read_src("theme", "shared.css")
    theme = read_src("theme", f"theme{t}.css")
    write(os.path.join(dest, "assets", "css", f"style-{t}.css"),
          f"/* عصرجدید — پوسته {t} | فایل کامل و مستقل */\n" + shared + "\n" + theme)

    write(os.path.join(dest, "assets", "js", "main.js"), read_src("theme", "main.js"))
    write(os.path.join(dest, "assets", "js", "admin.js"), read_src("theme", "admin.js"))
    write(os.path.join(dest, "assets", "css", "admin.css"), read_src("theme", "admin.css"))
    write(os.path.join(dest, "assets", "images", "favicon.svg"), FAVICON)
    # فونت وزیرمتن: مسیرهای تصاویر/فونت‌ها داخل CSS نسبی است
    write(os.path.join(dest, "assets", "fonts", "README.txt"),
          "فونت وزیرمتن (Vazirmatn) — مجوز SIL Open Font License 1.1\n"
          "منبع: https://github.com/rastikerdar/vazirmatn\n")


def build_theme(t):
    dest = os.path.join(OUT, THEMES[t])
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    copy_assets(dest, t)

    for fname, title, active, builder, desc in SITE_PAGES:
        body = builder(t)
        extra = "page-404" if fname == "404.html" else ""
        write(os.path.join(dest, fname), page(t, title, body, active=active, desc=desc, extra_class=extra))

    write(os.path.join(dest, "admin", "login.html"), admp.admin_login(t))
    for fname, title, active, builder, desc in ADMIN_PAGES:
        write(os.path.join(dest, "admin", fname),
              admin_page(t, title, builder(t), active=active, desc=desc))

    readme = read_src("README_TEMPLATE.md").replace("__THEME_TITLE__", THEME_TITLES[t]).replace("__T__", str(t))
    write(os.path.join(dest, "README.md"), readme)

    # صفحه پیش‌فرض پوشه ادمین
    write(os.path.join(dest, "admin", "index.html"),
          f'<!DOCTYPE html><html lang="fa" dir="rtl"><head><meta charset="utf-8">'
          f'<meta http-equiv="refresh" content="0; url=login.html"><title>ورود به پنل مدیریت</title></head>'
          f'<body><p>در حال انتقال به صفحه ورود پنل مدیریت… <a href="login.html">ورود</a></p></body></html>')
    return dest


def check_links(dest):
    """بررسی وجود فایل مقصد لینک‌های داخلی"""
    import re
    missing, checked = set(), 0
    for root, _, files in os.walk(dest):
        for f in files:
            if not f.endswith(".html"):
                continue
            p = os.path.join(root, f)
            html = open(p, encoding="utf-8").read()
            for m in re.finditer(r'(?:href|src)="([^"#][^":]*?)"', html):
                url = m.group(1).split("?")[0].split("#")[0]
                if not url or url.startswith(("http", "mailto:", "tel:", "//", "data:")):
                    continue
                target = os.path.normpath(os.path.join(root, url))
                checked += 1
                if not os.path.exists(target):
                    missing.add(os.path.relpath(target, dest))
    return checked, sorted(missing)


if __name__ == "__main__":
    for t in (1, 2):
        dest = build_theme(t)
        n_files = sum(len(fs) for _, _, fs in os.walk(dest))
        checked, missing = check_links(dest)
        print(f"✔ پوسته {t} → {os.path.basename(dest)} | {n_files} فایل | {checked} لینک بررسی شد")
        if missing:
            print("  ⚠ فایل‌های یافت‌نشده:")
            for m in missing:
                print("   -", m)
        else:
            print("  ✔ همه لینک‌های داخلی سالم هستند")
