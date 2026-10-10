# -*- coding: utf-8 -*-
"""لایه‌های مشترک، آیکون‌ها و کامپوننت‌های دو پوسته + پنل مدیریت"""
from data import SITE, CATEGORIES, fa_num, money

# ---------------------------------------------------------------- icons ----
I = {
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.5c.9.4 1.9.6 2.9.7a2 2 0 0 1 1.7 2Z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h2.2l2.4 12.2a2 2 0 0 0 2 1.6h8.6a2 2 0 0 0 2-1.6L21 7H5"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-6 8-6s8 2 8 6"/>',
    "heart": '<path d="M12 20s-7-4.4-7-9.5A4.5 4.5 0 0 1 12 7a4.5 4.5 0 0 1 7 3.5C19 15.6 12 20 12 20Z"/>',
    "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "chev-down": '<path d="m6 9 6 6 6-6"/>',
    "chev-left": '<path d="m15 18-6-6 6-6"/>',
    "chev-right": '<path d="m9 6 6 6-6 6"/>',
    "arrow-left": '<path d="M19 12H5m7-7-7 7 7 7"/>',
    "arrow-right": '<path d="M5 12h14m-7-7 7 7-7 7"/>',
    "arrow-up": '<path d="M12 19V5m-7 7 7-7 7 7"/>',
    "check": '<path d="m4 12 5 5L20 6"/>',
    "check-circle": '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
    "x-circle": '<circle cx="12" cy="12" r="9"/><path d="m9 9 6 6M15 9l-6 6"/>',
    "star": '<path d="m12 3 2.7 5.7 6.3.9-4.6 4.4 1.1 6.2-5.5-3-5.5 3 1.1-6.2L3 9.6l6.3-.9L12 3Z"/>',
    "truck": '<path d="M1 4h11v11H1zM12 8h5l3 3.5V15h-8z"/><circle cx="5.5" cy="17.5" r="2"/><circle cx="16.5" cy="17.5" r="2"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.4 8.5-8 10-4.6-1.5-8-5-8-10V6l8-3Z"/><path d="m9 12 2 2 4-4"/>',
    "ruler": '<path d="M3 15 15 3l6 6L9 21z"/><path d="m7 11 2 2M10 8l2 2M13 5l2 2"/>',
    "layers": '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 13 9 5 9-5"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-11.5 7.2L4 21l1.8-5.5A8 8 0 1 1 21 12Z"/>',
    "tools": '<path d="M14 6a4 4 0 0 0 5.4 5.4L21 13l-8 8-2-2-4-4-2-2 8-8 1 1.6Z"/><path d="M6 6l3 3"/>',
    "scissors": '<circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><path d="M20 4 8.5 15.5M8.5 8.5 20 20"/>',
    "box": '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5v-9Z"/><path d="m3 7.5 9 4.5 9-4.5M12 12v9"/>',
    "building": '<path d="M4 21V4h10v17M14 9h6v12M7 8h4M7 12h4M7 16h4M17 13h1M17 17h1"/>',
    "grid": '<path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/>',
    "waves": '<path d="M2 8c3 0 3 3 6 3s3-3 6-3 3 3 6 3M2 14c3 0 3 3 6 3s3-3 6-3 3 3 6 3"/>',
    "counter": '<path d="M3 10h18v10H3z"/><path d="M5 10V6a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v4M9 20v-6h6v6"/>',
    "brick": '<path d="M3 6h18v4H3zM3 14h18v4H3z"/><path d="M9 6v4M15 14v4"/>',
    "diamond": '<path d="m12 3 8 6-8 12L4 9l8-6Z"/><path d="M4 9h16"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "minus": '<path d="M5 12h14"/>',
    "trash": '<path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/>',
    "edit": '<path d="M4 20h4l10-10-4-4L4 16v4Z"/><path d="m14 6 4 4"/>',
    "eye": '<path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6Z"/><circle cx="12" cy="12" r="2.5"/>',
    "filter": '<path d="M4 5h16l-6 7v6l-4 2v-8L4 5Z"/>',
    "sort": '<path d="M7 4v16m0 0-3-3m3 3 3-3M17 20V4m0 0-3 3m3-3 3 3"/>',
    "grid-view": '<path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/>',
    "list-view": '<path d="M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01"/>',
    "download": '<path d="M12 3v12m0 0-4-4m4 4 4-4M4 20h16"/>',
    "upload": '<path d="M12 21V9m0 0-4 4m4-4 4 4M4 4h16"/>',
    "print": '<path d="M7 8V4h10v4M7 18H4V9h16v9h-3"/><path d="M7 14h10v7H7z"/>',
    "share": '<circle cx="18" cy="5" r="2.5"/><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="19" r="2.5"/><path d="m8.2 10.8 7.6-4.4M8.2 13.2l7.6 4.4"/>',
    "home": '<path d="M3 11 12 3l9 8"/><path d="M5 10v11h14V10"/>',
    "dashboard": '<path d="M4 4h7v7H4zM13 4h7v16h-7zM4 13h7v7H4z"/>',
    "package": '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5v-9Z"/><path d="m3 7.5 9 4.5 9-4.5M12 12v9"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 21c0-3.5 3.1-5.5 7-5.5s7 2 7 5.5"/><path d="M17 5.5a3.5 3.5 0 0 1 0 7M18.5 15c2.2.6 3.5 2.2 3.5 4.5"/>',
    "tag": '<path d="M3 12.5V4h8.5L21 13.5 12.5 22 3 12.5Z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
    "message": '<path d="M4 4h16v11H9l-5 5V4Z"/>',
    "settings": '<circle cx="12" cy="12" r="3"/><path d="M12 3v3m0 12v3M3 12h3m12 0h3M5.6 5.6l2.1 2.1m8.6 8.6 2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "bar-chart": '<path d="M4 20h16M6 20V9M11 20V4M16 20v-7"/>',
    "logout": '<path d="M10 4H5v16h5M15 8l4 4-4 4M19 12H9"/>',
    "lock": '<rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "inbox": '<path d="M3 13 6 5h12l3 8v6H3v-6Z"/><path d="M3 13h5l1 2h6l1-2h5"/>',
    "alert": '<path d="M12 3 2 20h20L12 3Z"/><path d="M12 9v5m0 3h.01"/>',
    "trend-up": '<path d="m3 17 6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
    "trend-down": '<path d="m3 7 6 6 4-4 8 8"/><path d="M15 17h6v-6"/>',
    "wallet": '<path d="M3 7a2 2 0 0 1 2-2h12v4"/><rect x="3" y="7" width="18" height="12" rx="2"/><path d="M17 13h.01"/>',
    "credit-card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
    "percent": '<path d="m6 6 12 12"/><circle cx="7.5" cy="7.5" r="2"/><circle cx="16.5" cy="16.5" r="2"/>',
    "gift": '<path d="M4 11h16v10H4zM2 7h20v4H2zM12 7v14"/><path d="M12 7S10 3 7.5 3.6 8 7 12 7s4.5-3 2-3.6S12 7 12 7Z"/>',
    "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 .9-1 1.7M12 17h.01"/>',
    "file": '<path d="M14 3H7v18h10V6l-3-3Z"/><path d="M14 3v3h3M9 13h6M9 17h6"/>',
    "image": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.5"/><path d="m4 18 5-5 4 4 3-3 4 4"/>',
    "link": '<path d="M10 14a4 4 0 0 1 0-6l3-3a4 4 0 0 1 6 6l-2 2M14 10a4 4 0 0 1 0 6l-3 3a4 4 0 0 1-6-6l2-2"/>',
    "refresh": '<path d="M20 11A8 8 0 0 0 6 6L4 8M4 13a8 8 0 0 0 14 5l2-2"/><path d="M4 4v4h4M20 20v-4h-4"/>',
    "save": '<path d="M5 3h11l3 3v15H5z"/><path d="M8 3v6h7V3M8 14h8v7H8z"/>',
    "bell": '<path d="M18 15V10a6 6 0 1 0-12 0v5l-2 3h16l-2-3Z"/><path d="M10 21h4"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M5 5l2 2m10 10 2 2M19 5l-2 2M7 17l-2 2"/>',
    "ig": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
    "tg": '<path d="M21 4 3 11l4 1.5 2 6 3-4 5 3z"/>',
    "wa": '<path d="M20 12a8 8 0 0 1-11.6 7L4 20l1.2-4A8 8 0 1 1 20 12Z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5"/>',
    "in": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M7 10v7M7 7h.01M11 17v-4a2 2 0 0 1 4 0v4"/>',
    "map": '<path d="M9 3 3 5v16l6-2 6 2 6-2V3l-6 2-6-2Z"/><path d="M9 3v16M15 5v16"/>',
    "play": '<circle cx="12" cy="12" r="9"/><path d="m10 8.5 6 3.5-6 3.5v-7Z"/>',
    "spark": '<path d="M12 3v4m0 10v4M3 12h4m10 0h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M8.5 15.5 6 18"/>',
    "flag": '<path d="M5 21V4h9l1 2h5v9h-6l-1-2H5"/>',
}


def icon(name, cls=""):
    body = I.get(name, I["check"])
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


def stars(rate):
    full = int(round(rate))
    out = ['<span class="stars" aria-label="امتیاز">']
    for i in range(5):
        out.append(f'<i class="{"on" if i < full else ""}">{icon("star")}</i>')
    return "".join(out) + "</span>"


def sprite():
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none">']
    for k, v in I.items():
        parts.append(f'<symbol id="i-{k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                     f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{v}</symbol>')
    return "".join(parts) + "</svg>"


# ------------------------------------------------------------ helpers ----
def cat_by_slug(slug):
    for c in CATEGORIES:
        if c["slug"] == slug:
            return c
    return CATEGORIES[0]


def cat_name(slug):
    return cat_by_slug(slug)["name"]


def price_html(s, big=False):
    cls = "price big" if big else "price"
    old = f'<del class="price-old">{money(s["old"])}</del>' if s.get("old") else ""
    return (f'<div class="{cls}"><span class="amount">{fa_num(s["price"])}</span>'
            f'<span class="cur">تومان / {s["unit"]}</span>{old}</div>')


def product_card(s, compact=False):
    badge = f'<span class="badge badge-primary">{s["badge"]}</span>' if s.get("badge") else ""
    out_stock = '<span class="chip chip-warn">ناموجود</span>' if s["stock"] <= 0 else '<span class="chip chip-ok">موجود در انبار</span>'
    return f'''
<article class="card product-card{' compact' if compact else ''}" data-cat="{s['cat']}" data-price="{s['price']}" data-id="{s['id']}" data-name="{s['name']}">
  <div class="card-media">
    <a href="product.html" class="media-link" aria-label="{s['name']}">
      <img src="assets/images/{s['image']}" alt="{s['name']}" loading="lazy">
    </a>
    {badge}
    <div class="card-actions">
      <button class="icon-btn js-wish" type="button" title="افزودن به علاقه‌مندی‌ها" data-id="{s['id']}">{icon("heart")}</button>
      <button class="icon-btn js-compare" type="button" title="افزودن به مقایسه" data-id="{s['id']}">{icon("sort")}</button>
      <button class="icon-btn js-quick" type="button" title="نمایش سریع" data-id="{s['id']}">{icon("eye")}</button>
    </div>
  </div>
  <div class="card-body">
    <div class="card-meta">
      <a href="category.html" class="cat-link">{cat_name(s['cat'])}</a>
      <span class="code">کد {s['code']}</span>
    </div>
    <h3 class="card-title"><a href="product.html">{s['name']}</a></h3>
    <p class="card-text">{s['short']}</p>
    <div class="card-rate">{stars(s["rate"])}<span class="rate-num">{fa_num(s["rate"], 1)}</span><span class="muted">({fa_num(s["sold"])} فروش)</span></div>
    <div class="card-foot">
      {price_html(s)}
      <div class="card-buy">
        <div class="qty" data-qty>
          <button type="button" class="qty-btn js-minus" aria-label="کاهش">{icon("minus")}</button>
          <input type="text" value="۱" inputmode="numeric" aria-label="تعداد">
          <button type="button" class="qty-btn js-plus" aria-label="افزایش">{icon("plus")}</button>
        </div>
        <button class="btn btn-primary btn-icon js-add" type="button" data-id="{s['id']}" title="افزودن به سبد خرید">{icon("cart")}<span>افزودن</span></button>
      </div>
    </div>
    <div class="card-stock">{out_stock}</div>
  </div>
</article>'''


def cat_card(c):
    return f'''
<a class="cat-card" href="category.html">
  <img src="assets/images/{c['image']}" alt="{c['name']}" loading="lazy">
  <span class="cat-overlay"></span>
  <span class="cat-body">
    <span class="cat-icon">{icon(c['icon'])}</span>
    <span class="cat-name">{c['name']}</span>
    <span class="cat-desc">{c['desc'][:58]}…</span>
    <span class="cat-count">{fa_num(c['count'])} محصول <i>{icon("arrow-left")}</i></span>
  </span>
</a>'''


def section_head(eyebrow, title, sub="", align="center", more=None, more_label="مشاهده همه"):
    more_html = ""
    if more:
        more_html = (f'<a class="link-more" href="{more}">{more_label} {icon("arrow-left")}</a>')
    sub_html = f'<p class="sec-sub">{sub}</p>' if sub else ""
    return f'''
<div class="section-head align-{align}">
  <div class="sec-text">
    <span class="eyebrow">{eyebrow}</span>
    <h2 class="sec-title">{title}</h2>
    {sub_html}
  </div>
  {more_html}
</div>'''


def breadcrumb(items):
    parts = []
    for i, (label, href) in enumerate(items):
        if href and i < len(items) - 1:
            parts.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            parts.append(f'<li aria-current="page">{label}</li>')
    return f'''<nav class="breadcrumb-wrap" aria-label="مسیر صفحه">
  <div class="container">
    <ol class="breadcrumb">{''.join(parts)}</ol>
  </div>
</nav>'''


def page_hero(title, sub="", breadcrumb_items=None, crumb=True, bg=None):
    bg_style = f' style="--ph-img:url(assets/images/{bg})"' if bg else ""
    crumbs = breadcrumb(breadcrumb_items) if breadcrumb_items else ""
    return f'''
<section class="page-hero"{bg_style}>
  <div class="container">
    <div class="ph-inner">
      <h1 class="ph-title">{title}</h1>
      {f'<p class="ph-sub">{sub}</p>' if sub else ''}
    </div>
  </div>
</section>
{crumbs if crumb else ''}'''


def pagination(current=1, total=5):
    items = ['<ul class="pagination">']
    items.append(f'<li><a class="page-link prev" href="#" aria-label="قبلی">{icon("chev-right")}</a></li>')
    for i in range(1, total + 1):
        cls = " active" if i == current else ""
        items.append(f'<li><a class="page-link{cls}" href="#">{fa_num(i)}</a></li>')
    items.append(f'<li><a class="page-link next" href="#" aria-label="بعدی">{icon("chev-left")}</a></li>')
    items.append("</ul>")
    return "".join(items)


def newsletter_block():
    return f'''
<div class="newsletter">
  <div class="nl-text">
    <h3>خبرنامه عصرجدید</h3>
    <p>تخفیف‌های فصلی، طرح‌های جدید و مقالات کاربردی را اول از همه دریافت کنید.</p>
  </div>
  <form class="nl-form js-form" novalidate>
    <div class="field">
      <input type="email" placeholder="ایمیل خود را وارد کنید" required aria-label="ایمیل">
    </div>
    <button class="btn btn-primary" type="submit">{icon("mail")} عضویت در خبرنامه</button>
  </form>
</div>'''


def footer_links():
    cats = "".join(f'<li><a href="category.html">{c["name"]}</a></li>' for c in CATEGORIES[:5])
    return cats


# --------------------------------------------------------- theme 1 ---- #
def header_t1(active=""):
    nav = [
        ("index.html", "صفحه اصلی", ""),
        ("about.html", "درباره ما", ""),
        ("categories.html", "محصولات", "products"),
        ("services.html", "خدمات", ""),
        ("projects.html", "پروژه‌ها", ""),
        ("gallery.html", "گالری", ""),
        ("blog.html", "وبلاگ", ""),
        ("contact.html", "تماس با ما", ""),
    ]
    items = "".join(
        f'<li class="nav-item{ " active" if h == active else "" }"><a class="nav-link" href="{h}">{t}</a></li>'
        for h, t, _ in nav)
    return f'''
<div class="topbar">
  <div class="container topbar-inner">
    <div class="tb-right">
      <span class="tb-item">{icon("phone")} <a href="tel:{SITE['phone_link']}">{SITE['phone']}</a></span>
      <span class="tb-item tb-hide">{icon("clock")} {SITE['hours_short']}</span>
    </div>
    <div class="tb-left">
      <span class="tb-item tb-hide">{icon("pin")} {SITE['address_short']}</span>
      <span class="tb-social">
        <a href="#" aria-label="اینستاگرام">{icon("ig")}</a>
        <a href="#" aria-label="تلگرام">{icon("tg")}</a>
        <a href="#" aria-label="واتس‌اپ">{icon("wa")}</a>
        <a href="#" aria-label="لینکدین">{icon("in")}</a>
      </span>
    </div>
  </div>
</div>
<header class="site-header t1-header js-header">
  <div class="container header-inner">
    <a class="brand" href="index.html">
      <span class="brand-mark">{icon("diamond")}</span>
      <span class="brand-text">
        <strong>{SITE['name']}</strong>
        <small>{SITE['tagline']}</small>
      </span>
    </a>
    <nav class="nav-main" id="mainNav" aria-label="منوی اصلی">
      <ul class="nav-list">
        {items}
      </ul>
      <div class="nav-mobile-extra">
        <a class="btn btn-outline btn-block" href="login.html">{icon("user")} ورود / ثبت‌نام</a>
        <a class="btn btn-primary btn-block" href="price-list.html">{icon("file")} لیست قیمت</a>
      </div>
    </nav>
    <div class="header-actions">
      <button class="icon-btn js-search-open" type="button" title="جستجو">{icon("search")}</button>
      <a class="icon-btn" href="wishlist.html" title="علاقه‌مندی‌ها">{icon("heart")}<span class="dot-count js-wish-count">۰</span></a>
      <a class="icon-btn" href="cart.html" title="سبد خرید">{icon("cart")}<span class="dot-count js-cart-count">۰</span></a>
      <a class="btn btn-primary btn-lg header-cta" href="contact.html">{icon("phone")} مشاوره رایگان</a>
      <button class="icon-btn nav-toggle js-nav-toggle" type="button" aria-label="منو">{icon("menu")}</button>
    </div>
  </div>
</header>'''


def footer_t1():
    return f'''
<footer class="site-footer t1-footer">
  <div class="footer-main">
    <div class="container footer-grid">
      <div class="f-col f-about">
        <a class="brand brand-light" href="index.html">
          <span class="brand-mark">{icon("diamond")}</span>
          <span class="brand-text"><strong>{SITE['name']}</strong><small>{SITE['tagline']}</small></span>
        </a>
        <p>{SITE['about_short'][:190]}…</p>
        <div class="f-social">
          <a href="#" aria-label="اینستاگرام">{icon("ig")}</a>
          <a href="#" aria-label="تلگرام">{icon("tg")}</a>
          <a href="#" aria-label="واتس‌اپ">{icon("wa")}</a>
          <a href="#" aria-label="لینکدین">{icon("in")}</a>
        </div>
      </div>
      <div class="f-col">
        <h4 class="f-title">دسترسی سریع</h4>
        <ul class="f-links">
          <li><a href="about.html">درباره عصرجدید</a></li>
          <li><a href="categories.html">دسته‌بندی محصولات</a></li>
          <li><a href="price-list.html">لیست قیمت</a></li>
          <li><a href="projects.html">پروژه‌های اجرایی</a></li>
          <li><a href="gallery.html">گالری تصاویر</a></li>
          <li><a href="blog.html">مقالات و اخبار</a></li>
        </ul>
      </div>
      <div class="f-col">
        <h4 class="f-title">گروه محصولات</h4>
        <ul class="f-links">{footer_links()}</ul>
      </div>
      <div class="f-col f-contact">
        <h4 class="f-title">اطلاعات تماس</h4>
        <ul class="f-contact-list">
          <li>{icon("pin")}<span>{SITE['address']}</span></li>
          <li>{icon("phone")}<a href="tel:{SITE['phone_link']}">{SITE['phone']}</a></li>
          <li>{icon("wa")}<span>{SITE['mobile']}</span></li>
          <li>{icon("mail")}<a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
          <li>{icon("clock")}<span>{SITE['hours']}</span></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="footer-trust">
    <div class="container trust-grid">
      <div class="trust-item">{icon("shield")}<span>۱۸ ماه ضمانت‌نامه کتبی</span></div>
      <div class="trust-item">{icon("truck")}<span>ارسال و بیمه بار به سراسر کشور</span></div>
      <div class="trust-item">{icon("credit-card")}<span>پرداخت امن درگاه بانکی</span></div>
      <div class="trust-item">{icon("help")}<span>پشتیبانی ۷ روز هفته</span></div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container fb-inner">
      <p>© ۱۴۰۴ تمامی حقوق مادی و معنوی این سایت متعلق به شرکت <strong>{SITE['name']}</strong> است.</p>
      <ul class="fb-links">
        <li><a href="terms.html">قوانین و مقررات</a></li>
        <li><a href="privacy.html">حریم خصوصی</a></li>
        <li><a href="sitemap.html">نقشه سایت</a></li>
        <li><a href="faq.html">سوالات متداول</a></li>
      </ul>
    </div>
  </div>
</footer>'''


# --------------------------------------------------------- theme 2 ---- #
def header_t2(active=""):
    nav = [
        ("index.html", "خانه", ""),
        ("categories.html", "محصولات", ""),
        ("services.html", "خدمات", ""),
        ("projects.html", "پروژه‌ها", ""),
        ("about.html", "درباره ما", ""),
        ("blog.html", "وبلاگ", ""),
    ]
    items = "".join(
        f'<li class="nav-item{ " active" if h == active else "" }"><a class="nav-link" href="{h}">{t}</a></li>'
        for h, t, _ in nav)
    cats = "".join(
        f'''<li><a href="category.html"><img src="assets/images/{c['image']}" alt="{c['name']}" loading="lazy">
        <span><strong>{c['name']}</strong><small>{fa_num(c['count'])} محصول</small></span></a></li>'''
        for c in CATEGORIES)
    return f'''
<header class="site-header t2-header js-header">
  <div class="container header-inner">
    <a class="brand" href="index.html">
      <span class="brand-mark">{icon("layers")}</span>
      <span class="brand-text">
        <strong>{SITE['name']}</strong>
        <small>سنگ مصنوعی نسل جدید</small>
      </span>
    </a>
    <nav class="nav-main" id="mainNav" aria-label="منوی اصلی">
      <ul class="nav-list">
        {items}
        <li class="nav-item has-mega">
          <a class="nav-link" href="categories.html">گروه محصولات {icon("chev-down")}</a>
          <div class="mega">
            <ul class="mega-grid">{cats}</ul>
          </div>
        </li>
      </ul>
      <div class="nav-mobile-extra">
        <a class="btn btn-outline btn-block" href="gallery.html">{icon("image")} گالری نمونه کارها</a>
        <a class="btn btn-primary btn-block" href="price-list.html">{icon("download")} دانلود لیست قیمت</a>
      </div>
    </nav>
    <div class="header-actions">
      <button class="icon-btn js-search-open" type="button" title="جستجو">{icon("search")}</button>
      <a class="icon-btn hide-xs" href="compare.html" title="مقایسه">{icon("sort")}</a>
      <a class="icon-btn" href="cart.html" title="سبد خرید">{icon("cart")}<span class="dot-count js-cart-count">۰</span></a>
      <a class="btn btn-dark header-cta" href="contact.html">{icon("chat")} استعلام قیمت</a>
      <button class="icon-btn nav-toggle js-nav-toggle" type="button" aria-label="منو">{icon("menu")}</button>
    </div>
  </div>
  <div class="t2-ticker">
    <div class="container ticker-inner">
      <span class="ticker-tag">{icon("spark")} این هفته</span>
      <p>٪۱۳ تخفیف روی نانوسنگ نما و پنل‌های سه‌بعدی • ارسال رایگان سفارش‌های بالای ۵۰ مترمربع در تهران و کرج • مشاوره فنی رایگان با کارشناسان عصرجدید</p>
      <a href="products.html">مشاهده تخفیف‌ها {icon("arrow-left")}</a>
    </div>
  </div>
</header>'''


def footer_t2():
    cats = footer_links()
    return f'''
<footer class="site-footer t2-footer">
  <div class="container">
    {newsletter_block()}
  </div>
  <div class="footer-main">
    <div class="container footer-grid">
      <div class="f-col f-about">
        <a class="brand brand-light" href="index.html">
          <span class="brand-mark">{icon("layers")}</span>
          <span class="brand-text"><strong>{SITE['name']}</strong><small>سنگ مصنوعی نسل جدید</small></span>
        </a>
        <p>تولیدکننده سنگ مصنوعی، نانوسنگ، پنل سه‌بعدی و صفحات یکپارچه کوارتز و کورین با ۱۹ سال سابقه و خط تولید ۱۲٬۰۰۰ متری در چهاردانگه تهران.</p>
        <ul class="f-badges">
          <li>{icon("shield")} ISO 9001</li>
          <li>{icon("check-circle")} استاندارد ملی</li>
        </ul>
        <div class="f-social">
          <a href="#" aria-label="اینستاگرام">{icon("ig")}</a>
          <a href="#" aria-label="تلگرام">{icon("tg")}</a>
          <a href="#" aria-label="واتس‌اپ">{icon("wa")}</a>
          <a href="#" aria-label="لینکدین">{icon("in")}</a>
        </div>
      </div>
      <div class="f-col">
        <h4 class="f-title">حساب کاربری</h4>
        <ul class="f-links">
          <li><a href="login.html">ورود به حساب</a></li>
          <li><a href="register.html">ثبت‌نام</a></li>
          <li><a href="dashboard.html">پنل کاربری</a></li>
          <li><a href="orders.html">سفارش‌های من</a></li>
          <li><a href="wishlist.html">علاقه‌مندی‌ها</a></li>
          <li><a href="compare.html">مقایسه محصولات</a></li>
        </ul>
      </div>
      <div class="f-col">
        <h4 class="f-title">گروه محصولات</h4>
        <ul class="f-links">{cats}</ul>
      </div>
      <div class="f-col f-contact">
        <h4 class="f-title">تماس با ما</h4>
        <ul class="f-contact-list">
          <li>{icon("pin")}<span>{SITE['address']}</span></li>
          <li>{icon("phone")}<a href="tel:{SITE['phone_link']}">{SITE['phone']}</a></li>
          <li>{icon("mail")}<a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
          <li>{icon("clock")}<span>{SITE['hours']}</span></li>
        </ul>
        <div class="f-news-badge">{icon("bell")} پاسخ‌گویی تلفنی تا ساعت ۲۰</div>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container fb-inner">
      <p>© ۱۴۰۴ شرکت <strong>{SITE['name']}</strong> — تولیدکننده سنگ مصنوعی و صفحات یکپارچه</p>
      <ul class="fb-links">
        <li><a href="terms.html">قوانین</a></li>
        <li><a href="privacy.html">حریم خصوصی</a></li>
        <li><a href="sitemap.html">نقشه سایت</a></li>
        <li><a href="admin/login.html">ورود مدیران</a></li>
      </ul>
      <div class="fb-pay">
        <span>{icon("credit-card")} پرداخت امن</span>
        <span>{icon("shield")} SSL</span>
      </div>
    </div>
  </div>
</footer>'''


# --------------------------------------------------------- shell ----- #
def head_extra():
    return f'''
<div class="search-overlay" id="searchOverlay" hidden>
  <div class="search-box">
    <form class="search-form js-form" novalidate>
      <input type="search" placeholder="جستجوی محصول، طرح یا مقاله… (مثلاً: نانوسنگ نما)" aria-label="جستجو" autofocus>
      <button class="btn btn-primary" type="submit">{icon("search")} جستجو</button>
    </form>
    <div class="search-suggest">
      <span class="ss-title">جستجوهای پرطرفدار:</span>
      <a href="products.html">نانوسنگ نما</a>
      <a href="products.html">صفحه کوارتز</a>
      <a href="products.html">کورین یکپارچه</a>
      <a href="products.html">آجرنما تراکوتا</a>
      <a href="products.html">پنل سه‌بعدی</a>
    </div>
    <button class="search-close js-search-close" type="button" aria-label="بستن">{icon("x")}</button>
  </div>
</div>'''


def whatsapp_float():
    return f'''
<div class="float-tools">
  <a class="ft-btn ft-wa" href="#" title="واتس‌اپ">{icon("wa")}</a>
  <a class="ft-btn ft-tel" href="tel:{SITE['phone_link']}" title="تماس تلفنی">{icon("phone")}</a>
  <button class="ft-btn ft-top js-top" type="button" title="بازگشت به بالا">{icon("arrow-up")}</button>
</div>'''


def page(t, title, body, active="", desc="", extra_class="", scripts=""):
    """t = 1 یا 2"""
    if t == 1:
        head_func, foot_func, css = header_t1, footer_t1, "assets/css/style-1.css"
    else:
        head_func, foot_func, css = header_t2, footer_t2, "assets/css/style-2.css"
    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {SITE['name']} — {SITE['tagline']}</title>
<meta name="description" content="{desc or SITE['about_short'][:150]}">
<meta name="theme-color" content="#2c231b">
<link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
<link rel="stylesheet" href="{css}">
</head>
<body class="theme-{t} {extra_class}">
{sprite()}
<a class="skip-link" href="#main">رفتن به محتوای اصلی</a>
{head_func(active)}
<main id="main" class="site-main">
{body}
</main>
{foot_func()}
{head_extra()}
{whatsapp_float()}
<div class="toast-wrap" id="toastWrap"></div>
<div class="modal" id="quickModal" hidden>
  <div class="modal-backdrop js-modal-close"></div>
  <div class="modal-card modal-lg">
    <button class="modal-close js-modal-close" type="button" aria-label="بستن">{icon("x")}</button>
    <div class="modal-body" id="quickBody"></div>
  </div>
</div>
<script src="assets/js/main.js"></script>
{scripts}
</body>
</html>
'''


# ------------------------------------------------------- admin shell ---- #
def admin_page(t, title, body, active="dashboard", desc=""):
    items = ""
    for item in ADMIN_NAV:
        if item["type"] == "group":
            items += f'<li class="adm-nav-group">{item["label"]}</li>'
        else:
            cls = " active" if item["href"] == active else ""
            badge = f'<span class="adm-badge">{item["badge"]}</span>' if item.get("badge") else ""
            items += (f'<li><a class="adm-nav-link{cls}" href="{item["href"]}">{icon(item["icon"])}'
                      f'<span>{item["label"]}</span>{badge}</a></li>')
    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | پنل مدیریت عصرجدید</title>
<meta name="description" content="{desc or 'پنل مدیریت فروشگاه سنگ مصنوعی عصرجدید'}">
<link rel="icon" type="image/svg+xml" href="../assets/images/favicon.svg">
<link rel="stylesheet" href="../assets/css/admin.css">
</head>
<body class="admin admin-theme-{t}">
{sprite()}
<div class="adm-shell">
  <aside class="adm-side" id="admSide">
    <div class="adm-brand">
      <a href="dashboard.html">
        <span class="brand-mark">{icon("diamond")}</span>
        <span class="brand-text"><strong>{SITE['name']}</strong><small>پنل مدیریت فروشگاه</small></span>
      </a>
      <button class="adm-side-close js-adm-side-close" type="button" aria-label="بستن">{icon("x")}</button>
    </div>
    <nav class="adm-nav"><ul>{items}</ul></nav>
    <div class="adm-side-foot">
      <a href="../index.html" class="adm-site-link">{icon("home")} مشاهده سایت</a>
      <a href="login.html" class="adm-site-link danger">{icon("logout")} خروج از حساب</a>
    </div>
  </aside>
  <div class="adm-main">
    <header class="adm-top">
      <button class="adm-top-btn js-adm-side" type="button" aria-label="منو">{icon("menu")}</button>
      <div class="adm-crumb">
        <h1>{title}</h1>
        <span class="adm-crumb-sub">{desc}</span>
      </div>
      <div class="adm-top-actions">
        <div class="adm-search">{icon("search")}<input type="search" placeholder="جستجو…" class="js-admin-search" aria-label="جستجو"></div>
        <button class="adm-top-btn js-theme-toggle" type="button" title="حالت تیره">{icon("sun")}</button>
        <button class="adm-top-btn has-dot" type="button" title="اعلان‌ها">{icon("bell")}</button>
        <a class="adm-user" href="profile.html">
          <span class="avatar">س‌ر</span>
          <span class="adm-user-text"><strong>مهندس سعید رضایی</strong><small>مدیر سیستم</small></span>
          {icon("chev-down")}
        </a>
      </div>
    </header>
    <div class="adm-content">
{body}
    </div>
  </div>
</div>
<div class="toast-wrap" id="toastWrap"></div>
<div class="modal" id="admModal" hidden>
  <div class="modal-backdrop js-modal-close"></div>
  <div class="modal-card">
    <button class="modal-close js-modal-close" type="button" aria-label="بستن">{icon("x")}</button>
    <div class="modal-body" id="admModalBody"></div>
  </div>
</div>
<script src="../assets/js/admin.js"></script>
</body>
</html>
'''


ADMIN_NAV = [
    {"type": "link", "href": "dashboard.html", "label": "داشبورد", "icon": "dashboard"},
    {"type": "group", "label": "فروشگاه"},
    {"type": "link", "href": "products.html", "label": "محصولات", "icon": "package", "badge": "۱۶۱"},
    {"type": "link", "href": "categories.html", "label": "دسته‌بندی‌ها", "icon": "grid"},
    {"type": "link", "href": "orders.html", "label": "سفارش‌ها", "icon": "cart", "badge": "۳۷"},
    {"type": "link", "href": "comments.html", "label": "دیدگاه‌ها", "icon": "message", "badge": "۵"},
    {"type": "group", "label": "کاربران"},
    {"type": "link", "href": "customers.html", "label": "مشتریان", "icon": "users"},
    {"type": "link", "href": "roles.html", "label": "نقش‌ها و دسترسی‌ها", "icon": "lock"},
    {"type": "group", "label": "تنظیمات"},
    {"type": "link", "href": "profile.html", "label": "پروفایل مدیر", "icon": "user"},
    {"type": "link", "href": "settings.html", "label": "تنظیمات سایت", "icon": "settings"},
]
