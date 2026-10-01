# -*- coding: utf-8 -*-
"""ساخت بدنه صفحات عمومی سایت (هر دو پوسته)"""
from data import *
from layouts import (icon, stars, product_card, cat_card, section_head, page_hero, pagination,
                     newsletter_block, cat_name, cat_by_slug, price_html)

# ------------------------------------------------------------ components ----


def feature_strip():
    items = "".join(
        f'<div class="feature"><span class="feat-icon">{icon(f["icon"])}</span>'
        f'<span class="feat-body"><strong>{f["title"]}</strong><small>{f["text"]}</small></span></div>'
        for f in FEATURES)
    return f'<section class="feature-strip"><div class="container feature-grid">{items}</div></section>'


def stats_row(cls="stats-row"):
    items = "".join(
        f'<div class="stat"><span class="stat-value js-count" data-to="{s["value"]}">{fa_num(s["value"])}</span>'
        f'<span class="stat-suffix">{s["suffix"]}</span><span class="stat-label">{s["label"]}</span></div>'
        for s in STATS)
    return f'<div class="{cls}">{items}</div>'


def testimonials_section():
    cards = "".join(
        f'''<article class="card testi-card">
      <div class="testi-head"><span class="avatar avatar-lg">{t['name'].split()[-1][:1]}</span>
        <span class="testi-who"><strong>{t['name']}</strong><small>{t['role']}</small></span></div>
      <div class="testi-rate">{stars(t['rate'])}</div>
      <p class="testi-text">«{t['text']}»</p>
      <span class="testi-quote">{icon("chat")}</span>
    </article>''' for t in TESTIMONIALS)
    return f'''<section class="section section-alt">
  <div class="container">
    {section_head("نظر مشتریان", "تجربه کارفرمایان و معماران با عصرجدید", "کیفیت محصول و دقت اجرا، دو شاخصی است که مشتریان ما بیشترین اشاره را به آن دارند.")}
    <div class="grid grid-3 testi-grid">{cards}</div>
  </div>
</section>'''


def services_grid(limit=None):
    items = SERVICES[:limit] if limit else SERVICES
    cards = "".join(
        f'''<article class="card service-card">
      <span class="svc-icon">{icon(s['icon'])}</span>
      <h3 class="card-title"><a href="service.html">{s['name']}</a></h3>
      <p class="card-text">{s['short']}</p>
      <ul class="svc-list">{''.join(f'<li>{icon("check")} {i}</li>' for i in s['items'][:3])}</ul>
      <a class="link-more" href="service.html">جزئیات خدمت {icon("arrow-left")}</a>
    </article>''' for s in items)
    return cards


def gallery_grid(limit=None, filterable=False):
    items = GALLERY[:limit] if limit else GALLERY
    cards = "".join(
        f'''<figure class="g-item" data-cat="{g['cat']}">
      <a href="assets/images/{g['image']}" class="g-link js-lightbox" aria-label="{g['title']}">
        <img src="assets/images/{g['image']}" alt="{g['title']}" loading="lazy">
        <span class="g-overlay"><strong>{g['title']}</strong><small>{g['cat']}</small><i>{icon("search")}</i></span>
      </a>
    </figure>''' for g in items)
    filt = ""
    if filterable:
        cats = sorted({g["cat"] for g in GALLERY})
        chips = f'<button class="chip-btn active" type="button" data-filter="all">همه</button>' + "".join(
            f'<button class="chip-btn" type="button" data-filter="{c}">{c}</button>' for c in cats)
        filt = f'<div class="filter-chips js-gallery-filter">{chips}</div>'
    return filt + f'<div class="gallery-grid" id="galleryGrid">{cards}</div>'


def blog_cards(limit=None):
    items = ARTICLES[:limit] if limit else ARTICLES
    return "".join(
        f'''<article class="card blog-card" data-cat="{a['cat']}">
      <a class="card-media" href="article.html"><img src="assets/images/{a['image']}" alt="{a['title']}" loading="lazy">
        <span class="badge badge-soft">{a['cat']}</span></a>
      <div class="card-body">
        <div class="card-meta"><span>{icon("calendar")} {a['date']}</span><span>{icon("clock")} {a['read']}</span></div>
        <h3 class="card-title"><a href="article.html">{a['title']}</a></h3>
        <p class="card-text">{a['excerpt'][:120]}…</p>
        <a class="link-more" href="article.html">ادامه مطلب {icon("arrow-left")}</a>
      </div>
    </article>''' for a in items)


def projects_grid(limit=None):
    items = PROJECTS[:limit] if limit else PROJECTS
    return "".join(
        f'''<article class="card project-card">
      <a class="card-media" href="project.html"><img src="assets/images/{p['image']}" alt="{p['name']}" loading="lazy">
        <span class="badge badge-primary">{p['cat']}</span></a>
      <div class="card-body">
        <h3 class="card-title"><a href="project.html">{p['name']}</a></h3>
        <ul class="meta-list">
          <li>{icon("pin")} {p['city']}</li>
          <li>{icon("grid-view")} {p['area']}</li>
          <li>{icon("calendar")} {p['year']}</li>
        </ul>
        <p class="card-text">{p['text'][:96]}…</p>
        <a class="link-more" href="project.html">مشاهده پروژه {icon("arrow-left")}</a>
      </div>
    </article>''' for p in items)


def faq_list():
    out = []
    for i, f in enumerate(FAQ):
        opened = " open" if i == 0 else ""
        out.append(f'''<div class="acc-item{opened}">
      <button class="acc-head js-acc" type="button" aria-expanded="{'true' if i == 0 else 'false'}">
        <span>{icon("help")} {f['q']}</span><i class="acc-ico">{icon("chev-down")}</i>
      </button>
      <div class="acc-body"><p>{f['a']}</p></div>
    </div>''')
    return f'<div class="accordion">{ "".join(out) }</div>'


def cta_band(title="مشاوره و استعلام قیمت رایگان", text="کارشناسان عصرجدید آماده بررسی پروژه شما و ارائه پیش‌فاکتور دقیق هستند.", btns=True):
    b = '''<div class="cta-actions">
      <a class="btn btn-primary btn-lg" href="contact.html">درخواست مشاوره</a>
      <a class="btn btn-outline btn-lg" href="price-list.html">دریافت لیست قیمت</a>
    </div>''' if btns else ""
    return f'''<section class="cta-band">
  <div class="container cta-inner">
    <div class="cta-text">
      <span class="eyebrow eyebrow-light">{icon("spark")} عصرجدید</span>
      <h2>{title}</h2>
      <p>{text}</p>
      {b}
    </div>
    <ul class="cta-points">
      <li>{icon("check-circle")} بازدید و اندازه‌گیری رایگان در تهران و کرج</li>
      <li>{icon("check-circle")} برش CNC طبق نقشه پروژه با تلرانس ±۰٫۵ میلی‌متر</li>
      <li>{icon("check-circle")} ضمانت‌نامه کتبی ۱۸ ماهه و ضمانت سطح کوارتز ۱۰ ساله</li>
    </ul>
  </div>
</section>'''


# ---------------------------------------------------------------- pages ---- #
def index(t):
    chips = "".join(f'<a class="tab-btn{" active" if i == 0 else ""}" href="#tab-{i}" data-tab="tab-{i}">{n}</a>'
                    for i, n in enumerate(["پرفروش‌ترین‌ها", "جدیدترین محصولات", "پیشنهاد ویژه"]))
    grids = ""
    for i, sel in enumerate(["تراورتن", "کوارتز", "پنل"]):
        if i == 0:
            items = [s for s in STONES if s["featured"]][:6]
        elif i == 1:
            items = sorted(STONES, key=lambda s: -s["id"])[:6]
        else:
            items = [s for s in STONES if s.get("old")][:6]
        grids += f'<div class="tab-panel{" active" if i == 0 else ""}" id="tab-{i}"><div class="grid grid-3">{"".join(product_card(s) for s in items)}</div></div>'

    if t == 1:
        slides = "".join(f'''<div class="slide{' active' if i == 0 else ''}" data-i="{i}">
      <img src="assets/images/{img}" alt="{ttl}">
      <div class="slide-overlay"></div>
      <div class="container slide-inner">
        <span class="slide-tag">{tag}</span>
        <h2 class="slide-title">{ttl}</h2>
        <p class="slide-text">{txt}</p>
        <div class="slide-actions">
          <a class="btn btn-primary btn-lg" href="products.html">{icon("cart")} مشاهده و خرید</a>
          <a class="btn btn-ghost btn-lg" href="contact.html">{icon("chat")} استعلام قیمت</a>
        </div>
      </div>
    </div>''' for i, (img, tag, ttl, txt) in enumerate([
            ("hero-1.jpg", "نمای ساختمان", "نمای سنگی مدرن، با وزن سبک و اجرای سریع",
             "نانوسنگ نما با جذب آب زیر ۱٪ و ثبات رنگ در برابر آفتاب؛ انتخابی اقتصادی برای نمای ویلا، برج و مجتمع تجاری."),
            ("hero-2.jpg", "دکوراسیون داخلی", "دیوارپوش و پنل سه‌بعدی برای دیوار شاخص",
             "بیش از ۹۰ طرح و رنگ در ۶ گروه محصولی؛ از پنل‌های موج داخلی تا آجرنما و سنگ آنتیک مسی."),
            ("hero-3.jpg", "صفحات یکپارچه", "صفحه کوارتز و کورین، بدون درز و بدون لکه",
             "اجرای یکپارچه کانتر، سینک و میز با ضمانت سطح ۱۰ ساله و برش CNC طبق نقشه پروژه.")]))

        hero = f'''<section class="hero-slider js-slider">
  <div class="slides">{slides}</div>
  <div class="slider-nav">
    <button class="s-nav js-slide-prev" type="button" aria-label="قبلی">{icon("chev-right")}</button>
    <div class="s-dots js-slide-dots"></div>
    <button class="s-nav js-slide-next" type="button" aria-label="بعدی">{icon("chev-left")}</button>
  </div>
  <div class="hero-quick">
    <div class="container hq-inner">
      <div class="hq-item">{icon("ruler")}<div><strong>اندازه‌گیری رایگان</strong><small>تهران و کرج، بدون هزینه</small></div></div>
      <div class="hq-item">{icon("truck")}<div><strong>ارسال سریع</strong><small>موجودی انبار، ۲۴ ساعته</small></div></div>
      <div class="hq-item">{icon("shield")}<div><strong>ضمانت کتبی</strong><small>۱۸ ماه روی محصولات</small></div></div>
    </div>
  </div>
</section>'''
        intro = f'''<section class="section">
  <div class="container about-split">
    <div class="as-media">{icon_image_stack()}</div>
    <div class="as-text">
      {section_head("درباره عصرجدید", "تولیدکننده تخصصی سنگ مصنوعی از سال ۱۳۸۵", "", align="start")}
      <p>{SITE['about_short']}</p>
      <ul class="check-list">
        <li>{icon("check-circle")} خط تولید ۱۲٬۰۰۰ مترمربعی با پرس تحت خلأ و کوره پخت</li>
        <li>{icon("check-circle")} آزمایشگاه کنترل کیفیت با آزمون جذب آب و مقاومت فشاری</li>
        <li>{icon("check-circle")} تیم اجرایی اختصاصی و پشتیبانی فنی پس از فروش</li>
      </ul>
      {stats_row()}
      <a class="btn btn-primary" href="about.html">بیشتر بدانید {icon("arrow-left")}</a>
    </div>
  </div>
</section>'''
    else:
        hero = f'''<section class="hero-split">
  <div class="container hero-split-inner">
    <div class="hs-text">
      <span class="hs-tag">{icon("spark")} ۱۹ سال تجربه تولید، ۴۲۰ پروژه اجراشده</span>
      <h1 class="hs-title">سنگ مصنوعی <em>عصرجدید</em><br>از نما تا صفحه کابینت</h1>
      <p class="hs-lead">نانوسنگ، کوارتز، کورین، پنل سه‌بعدی و آجرنما — با مشاوره فنی رایگان، برش CNC طبق نقشه و ضمانت‌نامه کتبی.</p>
      <div class="hs-actions">
        <a class="btn btn-primary btn-lg" href="categories.html">{icon("grid")} انتخاب محصول</a>
        <a class="btn btn-outline btn-lg" href="price-list.html">{icon("download")} لیست قیمت ۱۴۰۴</a>
      </div>
      <ul class="hs-points">
        <li>{icon("check")} جذب آب زیر ۱٪</li>
        <li>{icon("check")} ضمانت ۱۸ ماهه</li>
        <li>{icon("check")} برش CNC دقیق</li>
        <li>{icon("check")} ارسال سراسر کشور</li>
      </ul>
    </div>
    <div class="hs-media">
      <div class="hs-img hs-img-main"><img src="assets/images/hero-1.jpg" alt="نمای سنگی مدرن"></div>
      <div class="hs-img hs-img-a"><img src="assets/images/p-1.jpg" alt="صفحه کوارتز"></div>
      <div class="hs-img hs-img-b"><img src="assets/images/cat-3.jpg" alt="پنل سه‌بعدی"></div>
      <div class="hs-card">
        <span class="hs-card-ico">{icon("shield")}</span>
        <div><strong>۱۸ ماه ضمانت نامه کتبی</strong><small>روی همه محصولات تولیدی</small></div>
      </div>
      <div class="hs-card hs-card-2">
        <span class="hs-card-ico">{icon("truck")}</span>
        <div><strong>ارسال ۲۴ ساعته</strong><small>برای اقلام موجود انبار</small></div>
      </div>
    </div>
  </div>
  <div class="hs-marquee">
    <div class="container hs-marquee-inner">
      <span>۲۶ طرح</span><span>نانوسنگ نما</span><span>•</span><span>۴۰ طرح</span><span>آجر و سنگ آنتیک</span>
      <span>•</span><span>۲۱ طرح</span><span>صفحات کوارتز</span><span>•</span><span>۲۴ طرح</span><span>کورین یکپارچه</span>
      <span>•</span><span>۱۸ طرح</span><span>پنل سه‌بعدی</span>
    </div>
  </div>
</section>'''
        intro = f'''<section class="section">
  <div class="container about-split">
    <div class="as-text">
      {section_head("درباره عصرجدید", "از یک کارگاه ۲۰۰ متری تا ظرفیت تولید ۴۰۰٬۰۰۰ مترمربع", "", align="start")}
      <p>{SITE['about_short']}</p>
      <ul class="check-list">
        <li>{icon("check-circle")} آزمایشگاه کنترل کیفیت با آزمون جذب آب و مقاومت فشاری</li>
        <li>{icon("check-circle")} ۱۸ نمایندگی فروش در ۵ استان کشور</li>
        <li>{icon("check-circle")} اجرای پروژه‌های تجاری و مسکونی با تیم فنی اختصاصی</li>
      </ul>
      <div class="as-actions">
        <a class="btn btn-dark" href="about.html">داستان عصرجدید {icon("arrow-left")}</a>
        <a class="btn btn-ghost-dark" href="projects.html">پروژه‌های اجراشده</a>
      </div>
    </div>
    <div class="as-media as-media-t2">
      <img class="as-img-1" src="assets/images/hero-3.jpg" alt="نمایشگاه محصولات">
      <img class="as-img-2" src="assets/images/cat-1.jpg" alt="نانوسنگ نما">
      <div class="as-badge">{icon("flag")}<div><strong>۱۹</strong><small>سال سابقه تولید</small></div></div>
    </div>
  </div>
</section>'''

    return f'''
{hero}
{feature_strip()}
<section class="section">
  <div class="container">
    {section_head("گروه محصولات", "دسته‌بندی محصولات عصرجدید", "شش گروه محصولی برای نما، کف، دیوار، کانتر و فضای داخلی؛ همراه با مشاوره انتخاب طرح.", align="center", more="categories.html")}
    <div class="grid grid-3 cat-grid">{"".join(cat_card(c) for c in CATEGORIES)}</div>
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    {section_head("فروشگاه", "محصولات منتخب عصرجدید", "محصولات پرطرفدار با موجودی انبار و امکان ارسال فوری.", align="center", more="products.html")}
    <div class="tabs js-tabs">
      <div class="tabs-head">{chips}</div>
      <div class="tabs-body">{grids}</div>
    </div>
  </div>
</section>
{intro}
<section class="section">
  <div class="container">
    {section_head("خدمات عصرجدید", "از مشاوره تا اجرا، همراه شما هستیم", "خدمات فنی و اجرایی کامل برای پروژه‌های مسکونی، تجاری و اداری.")}
    <div class="grid grid-3">{services_grid(6)}</div>
  </div>
</section>
{testimonials_section()}
<section class="section">
  <div class="container">
    {section_head("نمونه کارها", "گالری تصاویر و پروژه‌ها", "نگاهی به رنگ‌ها، طرح‌ها و پروژه‌های اجراشده عصرجدید.", align="center", more="gallery.html")}
    {gallery_grid(8)}
    <div class="center-actions"><a class="btn btn-outline" href="projects.html">{icon("building")} مشاهده پروژه‌های اجرایی</a></div>
  </div>
</section>
{cta_band()}
<section class="section section-soft">
  <div class="container">
    {section_head("وبلاگ", "مقالات و راهنمای خرید", "هر آنچه برای انتخاب، محاسبه و نگهداری سنگ مصنوعی لازم است بدانید.", align="center", more="blog.html")}
    <div class="grid grid-3">{blog_cards(3)}</div>
  </div>
</section>'''


def icon_image_stack():
    return f'''<div class="stack">
  <img class="stack-1" src="assets/images/hero-3.jpg" alt="نمایشگاه عصرجدید">
  <img class="stack-2" src="assets/images/cat-2.jpg" alt="دیوارپوش سنگ مصنوعی">
  <div class="stack-card">{icon("shield")}
    <div><strong>ISO 9001</strong><small>سیستم مدیریت کیفیت</small></div></div>
  <div class="stack-years"><strong>۱۳۸۵</strong><small>سال تأسیس</small></div>
</div>'''


def about(t):
    team = "".join(f'''<article class="card team-card">
      <span class="avatar avatar-xl">{tm['initials']}</span>
      <h3 class="card-title">{tm['name']}</h3>
      <span class="role">{tm['role']}</span>
      <p class="card-text">{tm['bio']}</p>
    </article>''' for tm in TEAM)
    tl = "".join(f'''<div class="tl-item">
      <span class="tl-year">{x['year']}</span>
      <div class="tl-body"><h3>{x['title']}</h3><p>{x['text']}</p></div>
    </div>''' for x in TIMELINE)
    certs = "".join(f'''<article class="card cert-card">
      <span class="cert-ico">{icon("check-circle")}</span>
      <h3 class="card-title">{c['name']}</h3>
      <span class="muted">{c['year']}</span>
      <p class="card-text">{c['text']}</p>
    </article>''' for c in CERTIFICATES)
    return f'''
{page_hero("درباره عصرجدید", "۱۹ سال تولید سنگ مصنوعی؛ از کارگاه ۲۰۰ متری تا خط تولید ۱۲٬۰۰۰ مترمربعی", [("صفحه اصلی", "index.html"), ("درباره ما", "")], bg="hero-3.jpg")}
<section class="section">
  <div class="container about-split">
    <div class="as-media">
      <img class="as-img-1" src="assets/images/hero-3.jpg" alt="کارخانه عصرجدید">
      <img class="as-img-2" src="assets/images/cat-5.jpg" alt="نمونه محصولات">
      <div class="as-badge">{icon("flag")}<div><strong>۴۲۰+</strong><small>پروژه اجراشده</small></div></div>
    </div>
    <div class="as-text">
      {section_head("معرفی شرکت", "سنگ مصنوعی، این بار با استانداردهای صنعتی", "", align="start")}
      <p>{SITE['about_short']}</p>
      <p>ما در عصرجدید باور داریم سنگ مصنوعی باید مثل سنگ طبیعی زیبا، اما بادوام‌تر، سبک‌تر و اقتصادی‌تر باشد. به همین دلیل از سال ۱۳۸۵ روی فرمولاسیون و پوشش نانو محصولات سرمایه‌گذاری کرده‌ایم و امروز محصولات ما در پروژه‌های مسکونی، تجاری، اداری و درمانی به کار می‌رود.</p>
      {stats_row()}
      <div class="as-actions">
        <a class="btn btn-primary" href="projects.html">{icon("building")} پروژه‌های اجراشده</a>
        <a class="btn btn-outline" href="contact.html">{icon("chat")} تماس با ما</a>
      </div>
    </div>
  </div>
</section>
{feature_strip()}
<section class="section section-soft">
  <div class="container">
    {section_head("مسیر رشد", "تاریخچه عصرجدید", "نقاط عطف فعالیت ما در دو دهه گذشته.")}
    <div class="timeline">{tl}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    {section_head("ارزش‌های ما", "چرا کارفرمایان عصرجدید را انتخاب می‌کنند؟", "سه تعهد اصلی ما در همه پروژه‌ها.")}
    <div class="grid grid-3">
      <article class="card value-card"><span class="svc-icon">{icon("shield")}</span><h3 class="card-title">کیفیت کنترل‌شده</h3>
        <p class="card-text">هر بچ تولیدی پیش از ارسال، آزمون جذب آب، مقاومت فشاری و ثبات رنگ را در آزمایشگاه داخلی می‌گذراند. برگه آزمون به سفارش‌های بالای ۵۰۰ مترمربع پیوست می‌شود.</p></article>
      <article class="card value-card"><span class="svc-icon">{icon("tools")}</span><h3 class="card-title">اجرای تخصصی</h3>
        <p class="card-text">نصب سنگ مصنوعی جزئیات فنی دارد؛ از انتخاب چسب و بند تا جهت چیدمان. تیم اجرایی ما با چک‌لیست استاندارد و فرم رضایت‌نامه کار را تحویل می‌دهد.</p></article>
      <article class="card value-card"><span class="svc-icon">{icon("chat")}</span><h3 class="card-title">پشتیبانی بلندمدت</h3>
        <p class="card-text">پس از تحویل هم کنار شما هستیم؛ از ترمیم موضعی و پولیش سطح تا تأمین قطعات پله و قرنیز برای توسعه‌های بعدی پروژه.</p></article>
    </div>
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    {section_head("افتخارات و تأییدیه‌ها", "گواهی‌نامه‌ها و استانداردها", "مدارک کیفیتی که پشتوانه محصولات عصرجدید است.")}
    <div class="grid grid-4">{certs}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    {section_head("تیم عصرجدید", "افرادی که پروژه شما را پیش می‌برند", "تیم فنی، فروش و پشتیبانی ما در یک نگاه.")}
    <div class="grid grid-4">{team}</div>
  </div>
</section>
{cta_band("همکاری با عصرجدید را شروع کنیم؟", "برای پروژه‌های عمرانی، همکاری با معماران و اخذ نمایندگی فروش، آماده گفتگو هستیم.")}'''


def categories(t):
    return f'''
{page_hero("دسته‌بندی محصولات", "شش گروه محصولی برای همه نیازهای نما، کف، دیوار و سطوح داخلی", [("صفحه اصلی", "index.html"), ("دسته‌بندی‌ها", "")], bg="cat-2.jpg")}
<section class="section">
  <div class="container">
    {section_head("گروه محصولات", "محصول مناسب پروژه خود را انتخاب کنید", "هر گروه شامل طرح‌ها و رنگ‌های متعدد با امکان ارسال نمونه فیزیکی است.")}
    <div class="grid grid-3 cat-grid">{"".join(cat_card(c) for c in CATEGORIES)}</div>
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    <div class="grid grid-2">
      <div class="card info-card">
        <span class="svc-icon">{icon("layers")}</span>
        <h3 class="card-title">مقایسه سریع کاربردها</h3>
        <div class="table-wrap">
          <table class="table">
            <thead><tr><th>کاربرد</th><th>گروه پیشنهادی</th><th>مزیت کلیدی</th></tr></thead>
            <tbody>
              <tr><td>نمای ساختمان</td><td>نما و فاسد</td><td>ثبات رنگ، جذب آب زیر ۱٪</td></tr>
              <tr><td>صفحه کابینت</td><td>کوارتز / کورین</td><td>مقاوم به خط و حرارت</td></tr>
              <tr><td>دیوار شاخص داخلی</td><td>پنل سه‌بعدی</td><td>عمق و جلوه نورپردازی</td></tr>
              <tr><td>کف پرتردد</td><td>کفپوش و دیوارپوش</td><td>ضدلغزش R10، ضدخش</td></tr>
              <tr><td>نمای کافه و رستوران</td><td>آجر و سنگ آنتیک</td><td>بافت طبیعی، رنگ گرم</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="card info-card">
        <span class="svc-icon">{icon("ruler")}</span>
        <h3 class="card-title">نمی‌دانید کدام محصول مناسب است؟</h3>
        <p class="card-text">تیم فنی عصرجدید بر اساس کاربری فضا، شرایط اقلیمی و بودجه پروژه، سه گزینه پیشنهادی ارائه می‌کند و نمونه فیزیکی رنگ را برای شما ارسال می‌کند.</p>
        <ul class="check-list">
          <li>{icon("check-circle")} مشاوره تلفنی و ویدیویی رایگان</li>
          <li>{icon("check-circle")} ارسال بسته نمونه ۱۲ طرحی</li>
          <li>{icon("check-circle")} محاسبه متراژ و برآورد هزینه</li>
        </ul>
        <a class="btn btn-primary" href="contact.html">{icon("chat")} درخواست مشاوره فنی</a>
      </div>
    </div>
  </div>
</section>
{cta_band("آماده دریافت پیش‌فاکتور هستید؟", "متراژ و کاربری پروژه را بگویید تا برآورد دقیق قیمت را برایتان ارسال کنیم.")}'''


def products(t):
    side_cats = "".join(f'''<label class="check-row">
      <input type="checkbox" class="js-filter-cat" value="{c['slug']}">
      <span>{c['name']}</span><small>({fa_num(c['count'])})</small></label>''' for c in CATEGORIES)
    colors = [("سفید", "#f4f3f1"), ("کرم", "#e2d3bd"), ("طوسی", "#b9bcc0"), ("مشکی", "#24262a"), ("مسی", "#a0663f"), ("آجری", "#b05a3c")]
    color_chips = "".join(f'<button class="color-chip" type="button" style="--c:{hexv}" title="{n}" data-color="{n}"><span></span>{n}</button>' for n, hexv in colors)
    cards = "".join(product_card(s) for s in STONES)
    units = sorted({s["unit"] for s in STONES})
    unit_rows = "".join(f'<label class="check-row"><input type="radio" name="unit" value="{u}"><span>{u}</span></label>' for u in units[:3])
    return f'''
{page_hero("محصولات عصرجدید", "۱۲ محصول منتخب از ۱۶۱ طرح و رنگ؛ با فیلتر سریع محصول مناسب پروژه را پیدا کنید", [("صفحه اصلی", "index.html"), ("محصولات", "")], bg="p-1.jpg")}
<section class="section">
  <div class="container shop-layout">
    <aside class="shop-side">
      <div class="side-card">
        <button class="side-title js-side-toggle" type="button">{icon("grid")} دسته‌بندی محصولات <i>{icon("chev-down")}</i></button>
        <div class="side-body">{side_cats}</div>
      </div>
      <div class="side-card">
        <button class="side-title js-side-toggle" type="button">{icon("wallet")} محدوده قیمت <i>{icon("chev-down")}</i></button>
        <div class="side-body">
          <div class="price-range">
            <div class="field"><input type="text" id="priceFrom" placeholder="از (تومان)" inputmode="numeric" aria-label="حداقل قیمت"></div>
            <span class="dash">—</span>
            <div class="field"><input type="text" id="priceTo" placeholder="تا (تومان)" inputmode="numeric" aria-label="حداکثر قیمت"></div>
          </div>
          <div class="range-presets">
            <button type="button" class="chip-btn js-range" data-from="0" data-to="500000">تا ۵۰۰ هزار</button>
            <button type="button" class="chip-btn js-range" data-from="500000" data-to="2000000">۵۰۰ هزار تا ۲ میلیون</button>
            <button type="button" class="chip-btn js-range" data-from="2000000" data-to="20000000">بالای ۲ میلیون</button>
          </div>
          <button class="btn btn-outline btn-block js-apply-price" type="button">اعمال فیلتر قیمت</button>
        </div>
      </div>
      <div class="side-card">
        <button class="side-title js-side-toggle" type="button">{icon("percent")} رنگ‌بندی <i>{icon("chev-down")}</i></button>
        <div class="side-body"><div class="color-list">{color_chips}</div></div>
      </div>
      <div class="side-card">
        <button class="side-title js-side-toggle" type="button">{icon("box")} واحد فروش <i>{icon("chev-down")}</i></button>
        <div class="side-body">{unit_rows}</div>
      </div>
      <div class="side-card side-help">
        <span class="svc-icon">{icon("chat")}</span>
        <h3>کمک به انتخاب محصول؟</h3>
        <p>کارشناسان ما در ساعات کاری پاسخ‌گوی شما هستند.</p>
        <a class="btn btn-primary btn-block" href="tel:{SITE['phone_link']}">{icon("phone")} {SITE['phone']}</a>
      </div>
    </aside>
    <div class="shop-main">
      <div class="toolbar">
        <div class="toolbar-right">
          <span class="tb-count js-result-count">{fa_num(len(STONES))} محصول</span>
          <button class="chip-btn js-clear-filters" type="button">{icon("refresh")} حذف فیلترها</button>
        </div>
        <div class="toolbar-left">
          <label class="sort-select">
            {icon("sort")}
            <select class="js-sort" aria-label="ترتیب نمایش">
              <option value="default">مرتب‌سازی: پیش‌فرض</option>
              <option value="cheap">ارزان‌ترین</option>
              <option value="expensive">گران‌ترین</option>
              <option value="new">جدیدترین</option>
              <option value="popular">محبوب‌ترین</option>
            </select>
          </label>
          <div class="view-toggle">
            <button class="chip-btn active js-view" type="button" data-view="grid" title="نمایش شبکه‌ای">{icon("grid-view")}</button>
            <button class="chip-btn js-view" type="button" data-view="list" title="نمایش لیستی">{icon("list-view")}</button>
          </div>
        </div>
      </div>
      <div class="active-filters js-active-filters"></div>
      <div class="grid grid-3 js-products" id="productsGrid">{cards}</div>
      <div class="empty-state" id="noResult" hidden>
        <span class="es-icon">{icon("search")}</span>
        <h3>محصولی با این فیلترها پیدا نشد</h3>
        <p>فیلترها را تغییر دهید یا با کارشناسان ما تماس بگیرید تا محصول سفارشی تولید کنیم.</p>
        <button class="btn btn-primary js-clear-filters" type="button">حذف فیلترها</button>
      </div>
      <div class="shop-pagination">{pagination(1, 4)}</div>
    </div>
  </div>
</section>
{feature_strip()}
{cta_band("طرح مورد نظر را پیدا نکردید؟", "برای سفارش‌های بالای ۵۰ مترمربع، تولید رنگ و طرح سفارشی انجام می‌دهیم.")}'''


def product(t):
    s = STONES[0]
    thumbs = "".join(f'''<button class="pd-thumb{' active' if i == 0 else ''} js-thumb" type="button" data-src="assets/images/{g}">
      <img src="assets/images/{g}" alt="نمای {i + 1}"></button>''' for i, g in enumerate(s["gallery"]))
    specs = "".join(f'<tr><th>{k}</th><td>{v}</td></tr>' for k, v in s["specs"])
    related = "".join(product_card(x) for x in STONES[1:4])
    revs = "".join(f'''<article class="review">
      <div class="rev-head"><span class="avatar">{r['name'][:1]}</span>
        <div><strong>{r['name']}</strong><span class="muted">{r['date']}</span></div>{stars(r['rate'])}</div>
      <p>{r['text']}</p></article>''' for r in [
        {"name": "مهندس پویا رضایی", "date": "۱۴۰۴/۰۶/۱۸", "rate": 5, "text": "کیفیت سطح و یکنواختی رنگ عالی بود. برش‌ها دقیقاً طبق نقشه انجام شد و بسته‌بندی هم بسیار حرفه‌ای بود."},
        {"name": "خانم الهام ن.", "date": "۱۴۰۴/۰۵/۳۰", "rate": 4, "text": "محصول با قیمت مناسب و ارسال سریع. فقط زمان تحویل باربری یک روز بیشتر از اعلام اولیه طول کشید."},
        {"name": "شرکت سازه‌گستر", "date": "۱۴۰۴/۰۵/۱۲", "rate": 5, "text": "برای پروژه ۳۰۰ متری سفارش دادیم؛ پشتیبانی فنی قبل از اجرا خیلی کمک کرد. حتماً دوباره همکاری می‌کنیم."}])

    t2_note = "" if t == 1 else '''
      <div class="pd-t2-note">''' + icon("spark") + ''' محصول دارای موجودی انبار است؛ سفارش‌های ثبت‌شده تا ساعت ۱۴، همان روز ارسال می‌شوند.</div>'''

    return f'''
<nav class="breadcrumb-wrap"><div class="container"><ol class="breadcrumb">
  <li><a href="index.html">صفحه اصلی</a></li><li><a href="products.html">محصولات</a></li>
  <li><a href="category.html">{cat_name(s['cat'])}</a></li><li aria-current="page">{s['name']}</li></ol></div></nav>
<section class="section">
  <div class="container pd-layout">
    <div class="pd-gallery">
      <div class="pd-main"><img id="pdMain" src="assets/images/{s['gallery'][0]}" alt="{s['name']}">
        <span class="badge badge-primary pd-badge">{s['badge']}</span></div>
      <div class="pd-thumbs js-thumbs">{thumbs}</div>
      <div class="pd-share">
        <span>اشتراک‌گذاری:</span>
        <a href="#" class="icon-btn sm" aria-label="تلگرام">{icon("tg")}</a>
        <a href="#" class="icon-btn sm" aria-label="واتس‌اپ">{icon("wa")}</a>
        <a href="#" class="icon-btn sm" aria-label="لینکدین">{icon("in")}</a>
        <button class="icon-btn sm js-wish" type="button" data-id="{s['id']}" aria-label="علاقه‌مندی">{icon("heart")}</button>
        <button class="icon-btn sm" type="button" aria-label="چاپ">{icon("print")}</button>
      </div>
    </div>
    <div class="pd-info">
      <div class="pd-head">
        <span class="cat-link">{cat_name(s['cat'])}</span>
        <h1 class="pd-title">{s['name']}</h1>
        <div class="pd-meta">
          {stars(s['rate'])}<span class="rate-num">{fa_num(s['rate'], 1)}</span>
          <span class="muted">از {fa_num(126)} دیدگاه</span>
          <span class="divider"></span>
          <span class="chip chip-ok">{icon("check")} موجود در انبار</span>
          <span class="muted">کد کالا: {s['code']}</span>
        </div>
        <p class="pd-lead">{s['short']}</p>
      </div>
      {t2_note}
      <div class="pd-price-box">
        {price_html(s, big=True)}
        <div class="pd-price-meta">
          <span>{icon("percent")} خرید بالای ۵۰ مترمربع: تخفیف پلکانی تا ۸٪</span>
          <span>{icon("truck")} ارسال با باربری تخصصی و بیمه کامل</span>
        </div>
      </div>
      <ul class="pd-quick-specs">
        <li><span>ابعاد</span><strong>{s['size']}</strong></li>
        <li><span>ضخامت</span><strong>{s['thickness']}</strong></li>
        <li><span>وزن</span><strong>{s['weight']}</strong></li>
        <li><span>رنگ</span><strong>{s['color']}</strong></li>
      </ul>
      <div class="pd-variant">
        <span class="variant-label">انتخاب طرح و رنگ:</span>
        <div class="variant-list">
          <button class="variant active" type="button"><span style="--c:#f4f3f1"></span>سفید برفی</button>
          <button class="variant" type="button"><span style="--c:#e2d3bd"></span>کرم روشن</button>
          <button class="variant" type="button"><span style="--c:#b9bcc0"></span>طوسی</button>
          <button class="variant" type="button"><span style="--c:#24262a"></span>آنتراسیت</button>
        </div>
      </div>
      <div class="pd-buy">
        <div class="qty qty-lg" data-qty>
          <button type="button" class="qty-btn js-minus" aria-label="کاهش">{icon("minus")}</button>
          <input type="text" value="۱" inputmode="numeric" aria-label="تعداد">
          <button type="button" class="qty-btn js-plus" aria-label="افزایش">{icon("plus")}</button>
        </div>
        <button class="btn btn-primary btn-lg js-add" type="button" data-id="{s['id']}">{icon("cart")} افزودن به سبد خرید</button>
        <a class="btn btn-dark btn-lg" href="checkout.html">{icon("credit-card")} خرید سریع</a>
      </div>
      <div class="pd-assure">
        <div class="assure-item">{icon("shield")}<div><strong>ضمانت اصالت</strong><small>۱۸ ماه ضمانت کتبی</small></div></div>
        <div class="assure-item">{icon("ruler")}<div><strong>برش طبق نقشه</strong><small>تلرانس ±۰٫۵ میلی‌متر</small></div></div>
        <div class="assure-item">{icon("refresh")}<div><strong>مرجوعی ۷ روزه</strong><small>در صورت نقص تولیدی</small></div></div>
        <div class="assure-item">{icon("help")}<div><strong>مشاوره فنی</strong><small>۷ روز هفته</small></div></div>
      </div>
    </div>
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    <div class="tabs js-tabs">
      <div class="tabs-head">
        <a class="tab-btn active" href="#tab-desc" data-tab="tab-desc">توضیحات محصول</a>
        <a class="tab-btn" href="#tab-specs" data-tab="tab-specs">مشخصات فنی</a>
        <a class="tab-btn" href="#tab-reviews" data-tab="tab-reviews">دیدگاه‌ها ({fa_num(3)})</a>
        <a class="tab-btn" href="#tab-install" data-tab="tab-install">راهنمای نصب</a>
      </div>
      <div class="tabs-body">
        <div class="tab-panel active" id="tab-desc">
          <div class="prose">
            <p>{s['desc']}</p>
            <h3>کاربردهای پیشنهادی</h3>
            <ul>
              <li>صفحه کابینت، کانتر آشپزخانه و میز پیشخوان</li>
              <li>کانتر فروشگاهی، کافه و رستوران با ترافیک بالا</li>
              <li>سطوح آزمایشگاهی و فضاهای درمانی به‌دلیل سطح غیرمتخلخل</li>
            </ul>
            <h3>نکات نگهداری</h3>
            <p>شست‌وشوی روزانه با آب گرم و مایع ظرف‌شویی بی‌اسید کافی است. از اسکاچ فلزی و مواد ساینده پرهیز کنید و از زیرقابلمه‌ای برای ظروف داغ استفاده کنید.</p>
          </div>
        </div>
        <div class="tab-panel" id="tab-specs">
          <div class="table-wrap"><table class="table table-spec">
            <tbody>{specs}</tbody>
          </table></div>
        </div>
        <div class="tab-panel" id="tab-reviews">
          <div class="reviews">
            <div class="rev-summary">
              <div class="rev-score"><strong>{fa_num(s['rate'], 1)}</strong><span>از ۵</span>{stars(s['rate'])}<small>بر اساس {fa_num(126)} دیدگاه ثبت‌شده</small></div>
              <div class="rev-bars">
                <div class="rev-bar"><span>۵ ستاره</span><i><b style="width:78%"></b></i><small>۷۸٪</small></div>
                <div class="rev-bar"><span>۴ ستاره</span><i><b style="width:16%"></b></i><small>۱۶٪</small></div>
                <div class="rev-bar"><span>۳ ستاره</span><i><b style="width:4%"></b></i><small>۴٪</small></div>
                <div class="rev-bar"><span>۲ ستاره</span><i><b style="width:1%"></b></i><small>۱٪</small></div>
                <div class="rev-bar"><span>۱ ستاره</span><i><b style="width:1%"></b></i><small>۱٪</small></div>
              </div>
              <button class="btn btn-outline js-modal-btn" type="button" data-modal="review">ثبت دیدگاه جدید</button>
            </div>
            <div class="rev-list">{revs}</div>
          </div>
        </div>
        <div class="tab-panel" id="tab-install">
          <div class="prose">
            <ol class="steps">
              <li><strong>آماده‌سازی سطح:</strong> سطح باید تمیز، خشک و بدون گرد و غبار باشد. در دیوارهای گچی، پوشش تخته‌ای توصیه می‌شود.</li>
              <li><strong>انتقال چیدمان:</strong> خط‌کشی و رگه‌بندی طبق نقشه اجرایی و با در نظر گرفتن جهت صفحه انجام می‌شود.</li>
              <li><strong>چسب‌زنی:</strong> چسب مخصوص سنگ مصنوعی با شیارکش ۸ میلی‌متری روی دیوار و پشت صفحه اجرا می‌شود.</li>
              <li><strong>نصب و تراز:</strong> صفحه با فاصله بند ۲ میلی‌متر نصب و تراز افقی کنترل می‌شود.</li>
              <li><strong>بندکشی و پولیش:</strong> پس از ۲۴ ساعت بندکشی انجام و لبه‌ها پولیش می‌شوند.</li>
            </ol>
            <p class="note">{icon("alert")} توصیه می‌شود نصب صفحات کوارتز و کورین فقط توسط تیم‌های آموزش‌دیده عصرجدید انجام شود تا ضمانت محصول معتبر باقی بماند.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    {section_head("محصولات مرتبط", "محصولات مشابه و مکمل", "ترکیب این محصولات با موارد زیر در پروژه‌های مشابه بیشترین انتخاب را داشته است.", align="center", more="products.html")}
    <div class="grid grid-3">{related}</div>
  </div>
</section>
{cta_band("برای این محصول پیش‌فاکتور می‌خواهید؟", "متراژ و آدرس پروژه را ارسال کنید؛ کارشناس ما قیمت نهایی با حمل را اعلام می‌کند.")}'''


def category(t):
    c = CATEGORIES[0]
    items = [s for s in STONES if s["cat"] == "facade"] + [s for s in STONES if s["cat"] != "facade"][:4]
    cards = "".join(product_card(s) for s in items)
    side = "".join(f'''<li><a class="{'active' if cc['slug'] == c['slug'] else ''}" href="category.html">{cc['name']}<span>{fa_num(cc['count'])}</span></a></li>''' for cc in CATEGORIES)
    return f'''
{page_hero(c['name'], c['desc'], [("صفحه اصلی", "index.html"), ("محصولات", "products.html"), (c['name'], "")], bg=c['image'])}
<section class="section">
  <div class="container shop-layout">
    <aside class="shop-side">
      <div class="side-card">
        <h3 class="side-title-static">{icon("grid")} گروه محصولات</h3>
        <ul class="side-nav">{side}</ul>
      </div>
      <div class="side-card">
        <h3 class="side-title-static">{icon("tag")} برند</h3>
        <ul class="side-nav"><li><a class="active" href="#">عصرجدید<span>۱۲</span></a></li>
          <li><a href="#">وارداتی<span>۴</span></a></li></ul>
      </div>
      <div class="side-help">
        <span class="svc-icon">{icon("ruler")}</span>
        <h3>متراژ پروژه را می‌دانید؟</h3>
        <p>محاسبه‌گر آنلاین متراژ و هزینه را رایگان استفاده کنید.</p>
        <a class="btn btn-primary btn-block" href="price-list.html">محاسبه و لیست قیمت</a>
      </div>
    </aside>
    <div class="shop-main">
      <div class="cat-intro">
        <div class="ci-text">
          <h2>درباره گروه {c['name']}</h2>
          <p>{c['long']}</p>
        </div>
        <ul class="ci-points">
          <li>{icon("check-circle")} {fa_num(c['count'])} طرح و رنگ در این گروه</li>
          <li>{icon("check-circle")} موجودی انبار و ارسال ۲۴ ساعته</li>
          <li>{icon("check-circle")} امکان ارسال نمونه فیزیکی رنگ</li>
        </ul>
      </div>
      <div class="toolbar">
        <div class="toolbar-right"><span class="tb-count">{fa_num(len(items))} محصول در این دسته</span></div>
        <div class="toolbar-left">
          <label class="sort-select">{icon("sort")}
            <select aria-label="ترتیب نمایش">
              <option>مرتب‌سازی: پیشنهاد عصرجدید</option><option>ارزان‌ترین</option><option>گران‌ترین</option><option>جدیدترین</option>
            </select></label>
        </div>
      </div>
      <div class="grid grid-3">{cards}</div>
      <div class="shop-pagination">{pagination(1, 3)}</div>
    </div>
  </div>
</section>
{cta_band()}
<section class="section section-soft">
  <div class="container">
    {section_head("مقالات مرتبط", "راهنمای خرید این گروه محصول", align="center", more="blog.html")}
    <div class="grid grid-3">{blog_cards(3)}</div>
  </div>
</section>'''


def gallery(t):
    return f'''
{page_hero("گالری تصاویر", "نگاهی نزدیک به طرح‌ها، رنگ‌ها و پروژه‌های اجراشده عصرجدید", [("صفحه اصلی", "index.html"), ("گالری", "")], bg="hero-3.jpg")}
<section class="section">
  <div class="container">
    {section_head("گالری", "فیلتر کنید و تصاویر را در اندازه کامل ببینید", "روی هر تصویر کلیک کنید تا در حالت تمام‌صفحه نمایش داده شود.")}
    {gallery_grid(filterable=True)}
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    {section_head("ویدیو معرفی", "خط تولید و پروژه‌های عصرجدید در ۳ دقیقه", "گزارشی کوتاه از فرآیند تولید نانوسنگ و اجرای پروژه‌های شاخص.")}
    <div class="video-box">
      <img src="assets/images/hero-1.jpg" alt="ویدیو معرفی عصرجدید">
      <span class="vb-overlay"></span>
      <button class="video-play js-modal-btn" type="button" data-modal="video" aria-label="پخش ویدیو">{icon("play")}</button>
      <div class="vb-caption"><strong>از قالب‌گیری تا تحویل پروژه</strong><small>مدت زمان: ۳ دقیقه و ۱۲ ثانیه</small></div>
    </div>
  </div>
</section>
{cta_band("نمونه طرح مورد نظرتان را نیافتید؟", "با ارسال یک تصویر مرجع، نزدیک‌ترین طرح موجود را برایتان انتخاب و ارسال می‌کنیم.")}'''


def projects(t):
    return f'''
{page_hero("پروژه‌های اجرایی", "۴۲۰ پروژه مسکونی، تجاری و اداری با محصولات عصرجدید", [("صفحه اصلی", "index.html"), ("پروژه‌ها", "")], bg="cat-6.jpg")}
<section class="section">
  <div class="container">
    {section_head("نمونه پروژه‌ها", "چند پروژه شاخص عصرجدید", "در هر پروژه، محاسبه متراژ، تأمین مصالح، برش CNC و اجرا توسط تیم عصرجدید انجام شده است.")}
    <div class="grid grid-2">{projects_grid()}</div>
    <div class="shop-pagination">{pagination(1, 3)}</div>
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    {stats_row()}
  </div>
</section>
{feature_strip()}
{cta_band("پروژه شما هم در این فهرست باشد؟", "برای دریافت پیش‌فاکتور و برنامه زمان‌بندی اجرا با ما تماس بگیرید.")}'''


def project(t):
    p = PROJECTS[0]
    gal = "".join(f'''<a class="pj-shot js-lightbox" href="assets/images/{g}"><img src="assets/images/{g}" alt="{p['name']}" loading="lazy"></a>''' for g in p["gallery"])
    others = "".join(f'''<a class="pj-mini" href="project.html"><img src="assets/images/{o['image']}" alt="{o['name']}"><span>{o['name']}</span></a>''' for o in PROJECTS[1:])
    testi_cards = "".join(
        '<article class="card testi-card"><div class="testi-head"><span class="avatar avatar-lg">' + tt['name'][:1] +
        '</span><span class="testi-who"><strong>' + tt['name'] + '</strong><small>' + tt['role'] +
        '</small></span></div><div class="testi-rate">' + stars(tt['rate']) + '</div><p class="testi-text">«' +
        tt['text'] + '»</p></article>' for tt in TESTIMONIALS[:3])
    return f'''
{page_hero(p['name'], f"{p['cat']} — {p['city']} — {p['year']}", [("صفحه اصلی", "index.html"), ("پروژه‌ها", "projects.html"), (p['name'], "")], bg=p['image'])}
<section class="section">
  <div class="container">
    <div class="pj-facts">
      <div class="pf-item">{icon("user")}<span>کارفرما</span><strong>{p['client']}</strong></div>
      <div class="pf-item">{icon("pin")}<span>موقعیت</span><strong>{p['city']}</strong></div>
      <div class="pf-item">{icon("grid-view")}<span>متراژ اجرا</span><strong>{p['area']}</strong></div>
      <div class="pf-item">{icon("calendar")}<span>سال اجرا</span><strong>{p['year']}</strong></div>
      <div class="pf-item">{icon("layers")}<span>گروه محصول</span><strong>{p['cat']}</strong></div>
    </div>
    <div class="pj-layout">
      <div class="pj-main">
        <h2>شرح پروژه</h2>
        <p>{p['text']}</p>
        <p>در این پروژه، ابتدا بازدید فنی و متره دقیق انجام شد و نقشه برش صفحات تهیه گردید. با توجه به جهت رگه‌ها و ارتفاع دیوارها، چیدمان به‌گونه‌ای طراحی شد که هدر برش به کمترین میزان برسد. سپس بارها در سه مرحله و مطابق برنامه زمانی کارفرما به محل پروژه ارسال شد تا تداخلی با سایر عوامل اجرایی ایجاد نشود.</p>
        <h3>خروجی پروژه</h3>
        <ul class="check-list">
          <li>{icon("check-circle")} کاهش ۱۲٪ هدر برش نسبت به برآورد اولیه</li>
          <li>{icon("check-circle")} اجرای همزمان بخش نما و محوطه در ۴۵ روز کاری</li>
          <li>{icon("check-circle")} تحویل با فرم رضایت کارفرما و ضمانت‌نامه کتبی</li>
        </ul>
        <div class="pj-gallery">{gal}</div>
      </div>
      <aside class="pj-side">
        <div class="side-card">
          <h3 class="side-title-static">{icon("chat")} پروژه مشابه دارید؟</h3>
          <p class="card-text">کارشناسان ما می‌توانند برآورد متراژ و هزینه پروژه شما را تهیه کنند.</p>
          <a class="btn btn-primary btn-block" href="contact.html">درخواست مشاوره</a>
          <a class="btn btn-outline btn-block" href="tel:{SITE['phone_link']}">{icon("phone")} {SITE['phone']}</a>
        </div>
        <div class="side-card">
          <h3 class="side-title-static">{icon("building")} پروژه‌های دیگر</h3>
          <div class="pj-mini-list">{others}</div>
        </div>
      </aside>
    </div>
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    {section_head("کارفرمایان", "نظر کارفرمای این پروژه", align="center")}
    <div class="grid grid-3">{testi_cards}</div>
  </div>
</section>'''


def services(t):
    return f'''
{page_hero("خدمات عصرجدید", "از مشاوره و اندازه‌گیری رایگان تا اجرا و خدمات پس از فروش", [("صفحه اصلی", "index.html"), ("خدمات", "")], bg="cat-3.jpg")}
<section class="section">
  <div class="container">
    {section_head("خدمات فنی و اجرایی", "شش خدمت تخصصی عصرجدید", "هر خدمت توسط تیم داخلی عصرجدید و با چک‌لیست استاندارد اجرا می‌شود.")}
    <div class="grid grid-3">{services_grid()}</div>
  </div>
</section>
{feature_strip()}
<section class="section section-soft">
  <div class="container">
    {section_head("فرآیند همکاری", "از تماس اولیه تا تحویل پروژه", "مراحل شفاف همکاری، بدون هزینه پنهان.")}
    <ol class="process">
      <li><span class="pr-num">۱</span><h3>تماس و ثبت درخواست</h3><p>درخواست شما از طریق سایت، تلفن یا واتس‌اپ ثبت می‌شود و کارشناس مربوطه در کمتر از ۲ ساعت کاری تماس می‌گیرد.</p></li>
      <li><span class="pr-num">۲</span><h3>مشاوره و پیشنهاد محصول</h3><p>با بررسی کاربری، اقلیم و بودجه، سه گزینه پیشنهادی همراه با نمونه رنگ فیزیکی ارائه می‌شود.</p></li>
      <li><span class="pr-num">۳</span><h3>بازدید و متره دقیق</h3><p>تیم فنی بازدید می‌کند، متراژ نهایی محاسبه و نقشه برش تهیه می‌گردد.</p></li>
      <li><span class="pr-num">۴</span><h3>پیش‌فاکتور و تأمین بار</h3><p>پیش‌فاکتور شفاف با هزینه حمل صادر می‌شود و پس از تسویه، تولید یا ارسال بار آغاز می‌گردد.</p></li>
      <li><span class="pr-num">۵</span><h3>اجرا و تحویل</h3><p>تیم اجرایی با چک‌لیست استاندارد کار را انجام می‌دهد و ضمانت‌نامه کتبی تحویل می‌شود.</p></li>
    </ol>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div class="card info-card">
        <span class="svc-icon">{icon("ruler")}</span><h3 class="card-title">پرتال محاسبه متراژ و هزینه</h3>
        <p class="card-text">متراژ دیوار یا کف را وارد کنید تا برآورد اولیه هزینه همراه با در نظر گرفتن هدر برش نمایش داده شود.</p>
        <form class="form js-calc js-form" novalidate>
          <div class="form-grid">
            <div class="field"><label>طول (متر)</label><input type="number" min="1" value="12" class="js-calc-len"></div>
            <div class="field"><label>ارتفاع (متر)</label><input type="number" min="1" value="6" class="js-calc-hei"></div>
            <div class="field"><label>گروه محصول</label><select class="js-calc-prod">
              <option value="680000">نانوسنگ نما (۶۸۰٬۰۰۰ تومان)</option>
              <option value="450000">پنل سه‌بعدی (۴۵۰٬۰۰۰ تومان)</option>
              <option value="320000">آجرنما تراکوتا (۳۲۰٬۰۰۰ تومان)</option>
              <option value="2850000">صفحه کوارتز (۲٬۸۵۰٬۰۰۰ تومان)</option>
            </select></div>
            <div class="field"><label>هدیه هدر برش</label><select class="js-calc-waste"><option value="5">۵٪ (طرح ساده)</option><option value="10">۱۰٪ (طرح رگه‌ای)</option><option value="15">۱۵٪ (چیدمان پیچیده)</option></select></div>
          </div>
          <div class="calc-result">
            <div><span>متراژ مفید</span><strong class="js-calc-area">۷۲ مترمربع</strong></div>
            <div><span>متراژ با هدر</span><strong class="js-calc-area-w">۷۶ مترمربع</strong></div>
          </div>
          <div class="calc-total">برآورد اولیه: <strong class="js-calc-total">۵۱٬۶۸۰٬۰۰۰ تومان</strong></div>
          <p class="note">{icon("alert")} این عدد برآورد اولیه است؛ قیمت نهایی پس از بازدید فنی و تأیید متراژ اعلام می‌شود.</p>
          <div class="form-actions"><button class="btn btn-primary" type="submit">{icon("save")} ثبت درخواست پیش‌فاکتور</button></div>
        </form>
      </div>
      <div class="card info-card">
        <span class="svc-icon">{icon("shield")}</span><h3 class="card-title">تعهدات ما در قرارداد اجرا</h3>
        <ul class="check-list">
          <li>{icon("check-circle")} اجرا فقط با متریال و چسب تأییدشده عصرجدید</li>
          <li>{icon("check-circle")} رعایت برنامه زمانی توافق‌شده در قرارداد</li>
          <li>{icon("check-circle")} بیمه مسئولیت کارگاه در طول اجرا</li>
          <li>{icon("check-circle")} پوشش و محافظت از سطوح و تجهیزات همجوار</li>
          <li>{icon("check-circle")} تحویل فرم رضایت‌نامه و آموزش نگهداری به کارفرما</li>
        </ul>
        <div class="warranty-note">{icon("shield")}<div><strong>۱۸ ماه ضمانت‌نامه کتبی</strong>
          <p>همه خدمات اجرایی عصرجدید دارای ضمانت کتبی و پشتیبانی فنی رایگان در طول دوره ضمانت هستند.</p></div></div>
        <a class="btn btn-dark btn-block" href="contact.html">درخواست قرارداد و پیش‌فاکتور</a>
      </div>
    </div>
  </div>
</section>
{cta_band()}
<section class="section section-soft">
  <div class="container">
    {section_head("پرسش‌های متداول خدمات", "سوالات پرتکرار درباره خدمات اجرایی", align="center", more="faq.html")}
    {faq_list()}
  </div>
</section>'''


def service(t):
    return f'''
{page_hero("اجرای تخصصی و نصب", "اجرا با تیم فنی آموزش‌دیده عصرجدید، از زیرسازی تا بندکشی نهایی", [("صفحه اصلی", "index.html"), ("خدمات", "services.html"), ("اجرای تخصصی", "")], bg="cat-5.jpg")}
<section class="section">
  <div class="container">
    <div class="grid grid-1-2">
      <aside class="side-card">
        <h3 class="side-title-static">{icon("grid")} همه خدمات</h3>
        <ul class="side-nav">{''.join(f'<li><a class="{"active" if s["slug"] == "install" else ""}" href="service.html">{s["name"]}</a></li>' for s in SERVICES)}</ul>
        <div class="side-help">
          <span class="svc-icon">{icon("phone")}</span>
          <h3>مشاوره فوری</h3>
          <p>همین حالا با کارشناسان ما صحبت کنید.</p>
          <a class="btn btn-primary btn-block" href="tel:{SITE['phone_link']}">{SITE['phone']}</a>
        </div>
      </aside>
      <div class="svc-content">
        <div class="prose">
          <h1>اجرای تخصصی و نصب سنگ مصنوعی</h1>
          <p>نصب سنگ مصنوعی، پنل سه‌بعدی، آجرنما و صفحات یکپارچه کورین نیازمند دانش فنی و ابزار مخصوص است. تفاوت اصلی سطح نهایی یک پروژه موفق و یک اجرای پرمشکل، در جزئیاتی مثل انتخاب چسب سازگار، ضخامت لایه چسب، فاصله بندکشی و جهت رگه‌بندی صفحات است.</p>
          <img class="svc-img" src="assets/images/cat-1.jpg" alt="اجرای نمای سنگ مصنوعی">
          <h2>چرا اجرای عصرجدید متفاوت است؟</h2>
          <ul>
            <li><strong>تیم ثابت و آموزش‌دیده:</strong> اکیپ‌های اجرایی ما آموزش اختصاصی محصولات را گذرانده‌اند و با مشخصات فنی هر صفحه آشنا هستند.</li>
            <li><strong>ابزار و چسب اختصاصی:</strong> فقط از چسب و بند تأییدشده استفاده می‌کنیم تا ضمانت محصول معتبر بماند.</li>
            <li><strong>کنترل کیفیت مرحله‌ای:</strong> در سه مرحله (زیرسازی، چیدمان، بندکشی) فرم کنترل کیفیت تکمیل و به کارفرما تحویل می‌شود.</li>
            <li><strong>تحویل تمیز:</strong> پوشش و محافظت از سطوح، تجهیزات و فضای سبز همجوار بخشی از تعهد ماست.</li>
          </ul>
          <h2>زمان‌بندی اجرا</h2>
          <div class="table-wrap"><table class="table">
            <thead><tr><th>نوع پروژه</th><th>متراژ نمونه</th><th>مدت اجرا</th><th>تعداد اکیپ</th></tr></thead>
            <tbody>
              <tr><td>نمای ساختمان</td><td>۳۰۰ مترمربع</td><td>۷ تا ۱۰ روز کاری</td><td>۲ اکیپ</td></tr>
              <tr><td>دیوارپوش داخلی</td><td>۱۲۰ مترمربع</td><td>۴ تا ۶ روز کاری</td><td>۱ اکیپ</td></tr>
              <tr><td>صفحه کابینت و کانتر</td><td>۴۵ مترمربع</td><td>۲ تا ۳ روز کاری</td><td>۱ اکیپ</td></tr>
              <tr><td>راه‌پله</td><td>۶۰ مترمربع</td><td>۵ تا ۷ روز کاری</td><td>۱ اکیپ</td></tr>
            </tbody></table></div>
          <h2>پرداخت و تسویه</h2>
          <p>پس از توافق، ۳۰٪ مبلغ به‌عنوان پیش‌پرداخت دریافت می‌شود. ۴۰٪ در میانه کار پس از چیدمان اصلی و ۳۰٪ پایانی پس از تحویل و امضای فرم رضایت کارفرما تسویه می‌گردد.</p>
          <div class="info-box">{icon("shield")}<p><strong>ضمانت اجرا:</strong> تمام خدمات اجرایی ۱۸ ماه ضمانت کتبی دارند و در صورت بروز هرگونه ایراد اجرایی، تیم فنی به‌صورت رایگان اصلاح می‌کند.</p></div>
        </div>
        <div class="svc-cta">{cta_band("برای این خدمات پیش‌فاکتور بگیرید", "کافی است متراژ و نوع پروژه را اعلام کنید.", btns=True)}</div>
      </div>
    </div>
  </div>
</section>'''


def mini_posts_html(limit_chars=44):
    return "".join(
        '<li><a href="article.html"><img src="assets/images/' + a['image'] + '" alt="' + a['title'] +
        '"><span><strong>' + a['title'][:limit_chars] + '…</strong><small>' + a['date'] +
        '</small></span></a></li>' for a in ARTICLES[1:4])


def blog(t):
    featured = ARTICLES[0]
    cards = "".join(
        '<article class="card blog-card" data-cat="' + a['cat'] + '">'
        '<a class="card-media" href="article.html"><img src="assets/images/' + a['image'] + '" alt="' + a['title'] + '" loading="lazy">'
        '<span class="badge badge-soft">' + a['cat'] + '</span></a>'
        '<div class="card-body"><div class="card-meta"><span>' + icon("calendar") + ' ' + a['date'] +
        '</span><span>' + icon("clock") + ' ' + a['read'] + '</span></div>'
        '<h3 class="card-title"><a href="article.html">' + a['title'] + '</a></h3>'
        '<p class="card-text">' + a['excerpt'][:120] + '…</p>'
        '<a class="link-more" href="article.html">ادامه مطلب ' + icon("arrow-left") + '</a></div></article>'
        for a in ARTICLES[1:7])
    return f"""
{page_hero("وبلاگ عصرجدید", "مقالات تخصصی سنگ مصنوعی، راهنمای خرید، مقایسه محصولات و نکات اجرایی", [("صفحه اصلی", "index.html"), ("وبلاگ", "")], bg="hero-2.jpg")}
<section class="section">
  <div class="container">
    <article class="post-featured">
      <a class="pf-media" href="article.html"><img src="assets/images/{featured['image']}" alt="{featured['title']}"></a>
      <div class="pf-body">
        <span class="badge badge-primary">{featured['cat']}</span>
        <h2 class="pf-title"><a href="article.html">{featured['title']}</a></h2>
        <div class="card-meta"><span>{icon("user")} {featured['author']}</span><span>{icon("calendar")} {featured['date']}</span><span>{icon("clock")} {featured['read']}</span></div>
        <p>{featured['excerpt']}</p>
        <a class="btn btn-primary" href="article.html">خواندن مقاله {icon("arrow-left")}</a>
      </div>
    </article>
    <div class="filter-chips" style="margin-bottom:22px">{''.join(f'<a class="tab-btn{" active" if h == "blog.html" else ""}" href="{h}">{n}</a>' for h, n in [("blog.html", "گرید ۳ ستونه"), ("blog-grid-2cols.html", "گرید ۲ ستونه"), ("blog-grid-3cols.html", "گرید ۳ ستونه"), ("blog-grid-4cols.html", "گرید ۴ ستونه"), ("blog-grid-sidebar.html", "با نوار کنار"), ("blog-listing.html", "نمایش لیستی")])}</div>
    <div class="grid grid-3 js-blog">{cards}</div>
    <div class="shop-pagination">{pagination(1, 3)}</div>
  </div>
</section>"""


def blog_grid(t, cols=3):
    """آرشیو وبلاگ در حالت گرید با تعداد ستون دلخواه"""
    per = {2: 4, 3: 6, 4: 8}[cols]
    cards = "".join(
        '<article class="card blog-card" data-cat="' + a['cat'] + '">'
        '<a class="card-media" href="article.html"><img src="assets/images/' + a['image'] + '" alt="' + a['title'] + '" loading="lazy">'
        '<span class="badge badge-soft">' + a['cat'] + '</span></a>'
        '<div class="card-body"><div class="card-meta"><span>' + icon("calendar") + ' ' + a['date'] + '</span>'
        '<span>' + icon("clock") + ' ' + a['read'] + '</span></div>'
        '<h3 class="card-title"><a href="article.html">' + a['title'] + '</a></h3>'
        '<p class="card-text">' + a['excerpt'][:96] + '…</p></div></article>'
        for a in (ARTICLES * 2)[:per])
    tabs = "".join(
        f'<a class="tab-btn{" active" if c == cols else ""}" href="blog-grid-{c}cols.html">گرید {fa_num(c)} ستونه</a>'
        for c in (2, 3, 4))
    return f"""
{page_hero(f"آرشیو وبلاگ — گرید {fa_num(cols)} ستونه", "مقالات و راهنمای خرید محصولات عصرجدید", [("صفحه اصلی", "index.html"), ("وبلاگ", "blog.html"), (f"گرید {fa_num(cols)} ستونه", "")], crumb=True, bg="cat-4.jpg")}
<section class="section">
  <div class="container">
    <div class="filter-chips" style="margin-bottom:24px">
      <a class="tab-btn" href="blog.html">صفحه وبلاگ</a>{tabs}
      <a class="tab-btn" href="blog-grid-sidebar.html">با نوار کنار</a>
      <a class="tab-btn" href="blog-listing.html">لیستی</a>
    </div>
    <div class="grid grid-{cols}">{cards}</div>
    <div class="shop-pagination">{pagination(1, 3)}</div>
  </div>
</section>"""


def blog_sidebar(t):
    """وبلاگ با نوار کنار (دسته‌بندی، پرطرفدار، خبرنامه)"""
    cards = "".join(
        '<article class="card blog-card" data-cat="' + a['cat'] + '">'
        '<a class="card-media" href="article.html"><img src="assets/images/' + a['image'] + '" alt="' + a['title'] + '" loading="lazy">'
        '<span class="badge badge-soft">' + a['cat'] + '</span></a>'
        '<div class="card-body"><div class="card-meta"><span>' + icon("calendar") + ' ' + a['date'] + '</span></div>'
        '<h3 class="card-title"><a href="article.html">' + a['title'] + '</a></h3>'
        '<p class="card-text">' + a['excerpt'][:110] + '…</p>'
        '<a class="link-more" href="article.html">ادامه مطلب ' + icon("arrow-left") + '</a></div></article>'
        for a in ARTICLES[:4])
    return f"""
{page_hero("وبلاگ عصرجدید — با نوار کنار", "جستجو، دسته‌بندی و مقالات پرطرفدار در کنار فهرست مقالات", [("صفحه اصلی", "index.html"), ("وبلاگ", "blog.html"), ("با نوار کنار", "")], bg="cat-3.jpg")}
<section class="section">
  <div class="container blog-layout">
    <div class="blog-main">
      <div class="grid grid-2">{cards}</div>
      <div class="shop-pagination">{pagination(1, 3)}</div>
    </div>
    <aside class="blog-side">
      <div class="side-card">
        <h3 class="side-title-static">{icon("search")} جستجو در مقالات</h3>
        <form class="form js-form" novalidate><div class="field"><input type="search" placeholder="عنوان مقاله…" aria-label="جستجو"></div>
          <button class="btn btn-primary btn-block" type="submit">جستجو</button></form>
      </div>
      <div class="side-card">
        <h3 class="side-title-static">{icon("tag")} دسته‌بندی‌ها</h3>
        <ul class="side-nav">
          <li><a href="#">راهنمای خرید<span>{fa_num(2)}</span></a></li>
          <li><a href="#">دانستنی سنگ مصنوعی<span>{fa_num(2)}</span></a></li>
          <li><a href="#">مقایسه محصولات<span>{fa_num(1)}</span></a></li>
          <li><a href="#">نگهداری و ترمیم<span>{fa_num(1)}</span></a></li>
        </ul>
      </div>
      <div class="side-card">
        <h3 class="side-title-static">{icon("spark")} پربازدیدترین‌ها</h3>
        <ul class="mini-posts">{mini_posts_html(44)}</ul>
      </div>
      <div class="side-card side-news">{icon("mail")}<h3>عضویت در خبرنامه</h3>
        <p>مقالات جدید را در ایمیل خود دریافت کنید.</p>
        <form class="form js-form" novalidate><div class="field"><input type="email" placeholder="ایمیل" required aria-label="ایمیل"></div>
          <button class="btn btn-primary btn-block" type="submit">عضویت</button></form></div>
    </aside>
  </div>
</section>"""


def blog_listing(t):
    """نمایش لیستی مقالات"""
    rows = "".join(
        '<article class="card" style="padding:18px"><div style="display:flex;gap:18px;flex-wrap:wrap">'
        '<a href="article.html" style="width:230px;flex:none;border-radius:14px;overflow:hidden">'
        '<img src="assets/images/' + a['image'] + '" alt="' + a['title'] + '" style="width:100%;height:160px;object-fit:cover" loading="lazy"></a>'
        '<div style="flex:1;min-width:240px">'
        '<div class="card-meta"><span class="badge badge-soft">' + a['cat'] + '</span>'
        '<span>' + icon("calendar") + ' ' + a['date'] + '</span><span>' + icon("clock") + ' ' + a['read'] + '</span></div>'
        '<h3 class="card-title" style="margin-top:8px"><a href="article.html">' + a['title'] + '</a></h3>'
        '<p class="card-text">' + a['excerpt'] + '</p>'
        '<a class="link-more" href="article.html">ادامه مطلب ' + icon("arrow-left") + '</a></div></div></article>'
        for a in ARTICLES)
    return f"""
{page_hero("آرشیو لیستی مقالات", "همه مقالات عصرجدید در یک نگاه", [("صفحه اصلی", "index.html"), ("وبلاگ", "blog.html"), ("نمایش لیستی", "")], bg="cat-5.jpg")}
<section class="section">
  <div class="container">
    <div class="filter-chips" style="margin-bottom:24px">
      <a class="tab-btn" href="blog.html">صفحه وبلاگ</a>
      <a class="tab-btn" href="blog-grid-2cols.html">گرید ۲ ستونه</a>
      <a class="tab-btn" href="blog-grid-3cols.html">گرید ۳ ستونه</a>
      <a class="tab-btn" href="blog-grid-4cols.html">گرید ۴ ستونه</a>
      <a class="tab-btn" href="blog-grid-sidebar.html">با نوار کنار</a>
      <a class="tab-btn active" href="blog-listing.html">لیستی</a>
    </div>
    <div style="display:flex;flex-direction:column;gap:18px">{rows}</div>
    <div class="shop-pagination">{pagination(1, 3)}</div>
  </div>
</section>"""


def about2(t):
    """نسخه دوم صفحه درباره ما — تمرکز بر اعداد، گواهی‌ها و تیم"""
    certs = "".join(
        '<article class="card cert-card"><span class="cert-ico">' + icon("check-circle") + '</span>'
        '<h3 class="card-title">' + c['name'] + '</h3><span class="muted">' + c['year'] + '</span>'
        '<p class="card-text">' + c['text'] + '</p></article>' for c in CERTIFICATES)
    team = "".join(
        '<article class="card team-card"><span class="avatar avatar-xl">' + tm['initials'] + '</span>'
        '<h3 class="card-title">' + tm['name'] + '</h3><span class="role">' + tm['role'] + '</span>'
        '<p class="card-text">' + tm['bio'] + '</p></article>' for tm in TEAM)
    return f"""
{page_hero("درباره عصرجدید — روایت اعداد", "۱۹ سال تولید، ۴۲۰ پروژه، ۶٬۸۰۰ مشتری وفادار", [("صفحه اصلی", "index.html"), ("درباره ما", "about.html"), ("نسخه دوم", "")], bg="hero-1.jpg")}
<section class="section">
  <div class="container">
    {stats_row()}
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    {section_head("کیفیت و استانداردها", "گواهی‌نامه‌ها و آزمون‌های کیفی", "همه محصولات پیش از ارسال در آزمایشگاه داخلی بررسی می‌شوند.")}
    <div class="grid grid-4">{certs}</div>
  </div>
</section>
<section class="section">
  <div class="container about-split">
    <div class="as-media">
      <img class="as-img-1" src="assets/images/cat-1.jpg" alt="خط تولید عصرجدید">
      <img class="as-img-2" src="assets/images/hero-3.jpg" alt="نمایشگاه محصولات">
      <div class="as-badge">{icon("flag")}<div><strong>۴۰۰٬۰۰۰</strong><small>مترمربع ظرفیت سالانه</small></div></div>
    </div>
    <div class="as-text">
      {section_head("فرآیند تولید", "از تأمین مواد اولیه تا بسته‌بندی", "", align="start")}
      <p>پودر سنگ، رزین و رنگدانه‌های معدنی پس از کنترل ورودی وارد خط میکسر می‌شوند. صفحات با پرس تحت خلأ و ویبره شکل می‌گیرند، در کوره پخت می‌شوند و سپس پرداخت سطح (پولیش یا مات) انجام می‌شود. پیش از بسته‌بندی، هر بچ تولیدی آزمون جذب آب، مقاومت فشاری و ثبات رنگ را می‌گذراند.</p>
      <ul class="check-list">
        <li>{icon("check-circle")} ۴ ایستگاه کنترل کیفیت در طول خط تولید</li>
        <li>{icon("check-circle")} آزمون جذب آب زیر ۱٪ روی همه بچ‌ها</li>
        <li>{icon("check-circle")} بسته‌بندی با پالت چوبی و گوشه‌گیر فوم</li>
      </ul>
      <div class="as-actions">
        <a class="btn btn-primary" href="projects.html">{icon("building")} پروژه‌های اجراشده</a>
        <a class="btn btn-outline" href="gallery.html">{icon("image")} گالری محصولات</a>
      </div>
    </div>
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    {section_head("تیم عصرجدید", "افرادی که پروژه شما را پیش می‌برند", "تیم فنی، فروش و پشتیبانی ما در یک نگاه.")}
    <div class="grid grid-4">{team}</div>
  </div>
</section>
{cta_band("برای پروژه بعدی خود آماده‌اید؟", "کارشناسان ما برآورد متراژ و هزینه پروژه شما را رایگان تهیه می‌کنند.")}"""


def product_list(t):
    """لیست محصولات در حالت لیستی"""
    rows = "".join(
        '<article class="card" style="padding:18px" data-cat="' + s['cat'] + '" data-price="' + str(s['price']) + '" data-id="' + str(s['id']) + '">'
        '<div style="display:flex;gap:18px;flex-wrap:wrap">'
        '<a href="product.html" style="width:240px;flex:none;border-radius:14px;overflow:hidden">'
        '<img src="assets/images/' + s['image'] + '" alt="' + s['name'] + '" style="width:100%;height:180px;object-fit:cover" loading="lazy"></a>'
        '<div style="flex:1;min-width:260px;display:flex;flex-direction:column;gap:8px">'
        '<div class="card-meta"><a class="cat-link" href="category.html">' + cat_name(s['cat']) + '</a><span class="code">کد ' + s['code'] + '</span>'
        + stars(s['rate']) + '<span class="rate-num">' + fa_num(s['rate'], 1) + '</span></div>'
        '<h3 class="card-title"><a href="product.html">' + s['name'] + '</a></h3>'
        '<p class="card-text">' + s['short'] + '</p>'
        '<ul class="meta-list"><li>' + icon("ruler") + ' ' + s['size'] + '</li><li>' + icon("box") + ' موجودی: ' + fa_num(s['stock']) + ' ' + s['unit'] + '</li></ul>'
        '<div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-top:auto">'
        + price_html(s) +
        '<button class="btn btn-primary btn-icon js-add" type="button" data-id="' + str(s['id']) + '">' + icon("cart") + ' افزودن به سبد</button>'
        '<a class="btn btn-outline" href="product.html">جزئیات محصول</a></div>'
        '</div></div></article>' for s in STONES)
    return f"""
{page_hero("لیست محصولات", "نمایش لیستی محصولات عصرجدید با مشخصات کلیدی هر محصول", [("صفحه اصلی", "index.html"), ("محصولات", "products.html"), ("نمایش لیستی", "")], bg="p-3.jpg")}
<section class="section">
  <div class="container">
    <div class="toolbar">
      <div class="toolbar-right">
        <span class="tb-count">{fa_num(len(STONES))} محصول</span>
        <a class="chip-btn" href="products.html">{icon("grid-view")} نمایش شبکه‌ای</a>
        <a class="chip-btn active" href="product-list.html">{icon("list-view")} نمایش لیستی</a>
      </div>
      <div class="toolbar-left">
        <label class="sort-select">{icon("sort")}
          <select aria-label="ترتیب نمایش"><option>مرتب‌سازی: پیشنهاد عصرجدید</option><option>ارزان‌ترین</option><option>گران‌ترین</option><option>جدیدترین</option></select></label>
      </div>
    </div>
    <div class="js-products" style="display:flex;flex-direction:column;gap:18px">{rows}</div>
    <div class="shop-pagination">{pagination(1, 3)}</div>
  </div>
</section>
{cta_band()}"""


def article(t):
    a = ARTICLES[0]
    mini_posts = mini_posts_html(40)
    body = "".join(f"<p>{p}</p>" for p in a["body"])
    toc = "".join(f'<li><a href="#s{i}">{p[:38]}…</a></li>' for i, p in enumerate(a["body"][:6]))
    return f'''
{page_hero(a['title'], f"{a['cat']} — {a['read']} مطالعه", [("صفحه اصلی", "index.html"), ("وبلاگ", "blog.html"), (a['title'][:28] + "…", "")], bg=a['image'])}
<section class="section">
  <div class="container art-layout">
    <article class="art-main">
      <img class="art-hero" src="assets/images/{a['image']}" alt="{a['title']}">
      <div class="art-meta">
        <span>{icon("user")} {a['author']}</span><span>{icon("calendar")} {a['date']}</span>
        <span>{icon("clock")} {a['read']}</span><span class="badge badge-soft">{a['cat']}</span>
      </div>
      <div class="prose art-prose">
        <p class="lead">{a['excerpt']}</p>
        {body}
        <h2 id="s5">جمع‌بندی</h2>
        <p>انتخاب سنگ مصنوعی مناسب، ترکیبی از آگاهی فنی و مشاوره درست است. اگر در انتخاب تردید دارید، برگه فنی محصول را بخواهید و نمونه فیزیکی را پیش از سفارش ببینید. کارشناسان عصرجدید آماده بررسی پروژه شما و پیشنهاد دقیق‌ترین گزینه هستند.</p>
        <div class="info-box">{icon("alert")}<p><strong>نکته مهم:</strong> همیشه پیش از سفارش نهایی، برگه فنی محصول و شرایط ضمانت را مطالعه کنید تا در اجرا با غافلگیری روبه‌رو نشوید.</p></div>
      </div>
      <div class="art-tags">
        <span>برچسب‌ها:</span>
        <a href="#">سنگ مصنوعی</a><a href="#">نانوسنگ</a><a href="#">نمای ساختمان</a><a href="#">راهنمای خرید</a>
      </div>
      <div class="art-share">
        <span>اشتراک‌گذاری این مقاله:</span>
        <a class="icon-btn sm" href="#" aria-label="تلگرام">{icon("tg")}</a>
        <a class="icon-btn sm" href="#" aria-label="واتس‌اپ">{icon("wa")}</a>
        <a class="icon-btn sm" href="#" aria-label="لینکدین">{icon("in")}</a>
        <a class="icon-btn sm" href="#" aria-label="کپی لینک">{icon("link")}</a>
      </div>
      <div class="art-author">
        <span class="avatar avatar-xl">{a['author'].split()[-1][:1]}</span>
        <div><strong>{a['author']}</strong><span class="muted">کارشناس فنی عصرجدید</span>
          <p>نویسنده این مقاله با تیم فنی و فروش عصرجدید همکاری می‌کند و تجربه اجرایی پروژه‌های نما و صفحات یکپارچه را در قالب راهنماهای کاربردی منتشر می‌کند.</p></div>
      </div>
      <div class="art-comments">
        <h3>دیدگاه‌ها ({fa_num(2)})</h3>
        <article class="review"><div class="rev-head"><span class="avatar">ن</span><div><strong>نگار شریفی</strong><span class="muted">۱۴۰۴/۰۶/۱۴</span></div></div>
          <p>ممنون از توضیح کامل. برای نمای شمالی ساختمان ما هم پیشنهادتان همین نانوسنگ است؟ عرض دیوار ۱۴ متر و ارتفاع ۸ متر است.</p></article>
        <article class="review"><div class="rev-head"><span class="avatar">ب</span><div><strong>مهندس بهنام الف</strong><span class="muted">۱۴۰۴/۰۶/۱۵</span></div></div>
          <p>تجربه ما در پروژه اصفهان نشان داد انتخاب رنگدانه معدنی حرف اول را می‌زند؛ بعد از سه تابستان هنوز رنگ ثابت است.</p></article>
        <form class="form card js-form" novalidate>
          <h3>دیدگاه خود را ثبت کنید</h3>
          <div class="form-grid">
            <div class="field"><label>نام و نام خانوادگی</label><input type="text" required></div>
            <div class="field"><label>ایمیل (منتشر نمی‌شود)</label><input type="email" required></div>
            <div class="field full"><label>متن دیدگاه</label><textarea rows="4" required></textarea></div>
          </div>
          <div class="form-actions"><button class="btn btn-primary" type="submit">{icon("message")} ارسال دیدگاه</button></div>
        </form>
      </div>
    </article>
    <aside class="art-side">
      <div class="side-card">
        <h3 class="side-title-static">{icon("list-view")} فهرست مطالب</h3>
        <ul class="toc">{toc}</ul>
      </div>
      <div class="side-card">
        <h3 class="side-title-static">{icon("spark")} مقالات مرتبط</h3>
        <ul class="mini-posts">{mini_posts}</ul>
      </div>
      <div class="side-card side-cta">
        {icon("chat")}<h3>مشاوره خرید</h3><p>در انتخاب محصول شک دارید؟ کارشناسان ما رایگان راهنمایی می‌کنند.</p>
        <a class="btn btn-primary btn-block" href="contact.html">درخواست مشاوره</a>
      </div>
    </aside>
  </div>
</section>'''


def cart(t):
    rows = ""
    subtotal = 0
    for item in CART_DEMO:
        s = next(x for x in STONES if x["id"] == item["id"])
        line = s["price"] * item["qty"]
        subtotal += line
        rows += f'''<tr>
      <td class="ci-prod"><a href="product.html" class="ci-media"><img src="assets/images/{s['image']}" alt="{s['name']}"></a>
        <div class="ci-info"><a href="product.html" class="ci-name">{s['name']}</a>
          <span class="ci-meta">کد {s['code']} • واحد: {s['unit']}</span>
          <span class="ci-meta">{(s['size'])}</span></div></td>
      <td data-label="قیمت واحد">{money(s['price'])}</td>
      <td data-label="تعداد"><div class="qty" data-qty>
        <button type="button" class="qty-btn js-minus">{icon("minus")}</button>
        <input type="text" value="{fa_num(item['qty'])}" aria-label="تعداد">
        <button type="button" class="qty-btn js-plus">{icon("plus")}</button></div></td>
      <td data-label="جمع">{money(line)}</td>
      <td><button class="icon-btn sm danger" type="button" aria-label="حذف">{icon("trash")}</button></td>
    </tr>'''
    tax = int(subtotal * 0.09)
    shipping = 1850000
    total = subtotal + tax + shipping
    return f'''
{page_hero("سبد خرید", "۳ قلم کالا در سبد خرید شما", [("صفحه اصلی", "index.html"), ("سبد خرید", "")])}
<section class="section">
  <div class="container">
    <div class="cart-steps">
      <span class="cs-item active"><i>۱</i> سبد خرید</span>
      <span class="cs-line"></span>
      <span class="cs-item"><i>۲</i> اطلاعات ارسال</span>
      <span class="cs-line"></span>
      <span class="cs-item"><i>۳</i> پرداخت</span>
      <span class="cs-line"></span>
      <span class="cs-item"><i>۴</i> سفارش کامل</span>
    </div>
    <div class="cart-layout">
      <div class="cart-main">
        <div class="table-wrap card">
          <table class="table cart-table">
            <thead><tr><th>محصول</th><th>قیمت واحد</th><th>تعداد</th><th>جمع</th><th></th></tr></thead>
            <tbody>{rows}</tbody>
          </table>
        </div>
        <div class="cart-coupon">
          <div class="field"><input type="text" placeholder="کد تخفیف را وارد کنید" aria-label="کد تخفیف"></div>
          <button class="btn btn-outline" type="button">{icon("percent")} اعمال کد تخفیف</button>
          <a class="btn btn-ghost" href="products.html">{icon("refresh")} به‌روزرسانی سبد</a>
        </div>
      </div>
      <aside class="cart-side">
        <div class="card summary">
          <h3>خلاصه سفارش</h3>
          <ul class="sum-list">
            <li><span>جمع کالاها</span><strong>{money(subtotal)}</strong></li>
            <li><span>مالیات بر ارزش افزوده (۹٪)</span><strong>{money(tax)}</strong></li>
            <li><span>هزینه حمل (باربری تخصصی)</span><strong>{money(shipping)}</strong></li>
            <li class="sum-note">{icon("alert")} هزینه حمل برای سفارش‌های بالای ۵۰ مترمربع در تهران و کرج رایگان است.</li>
          </ul>
          <div class="sum-total"><span>مبلغ قابل پرداخت</span><strong>{money(total)}</strong></div>
          <a class="btn btn-primary btn-block btn-lg" href="checkout.html">{icon("credit-card")} ادامه فرآیند خرید</a>
          <a class="btn btn-ghost btn-block" href="products.html">افزودن محصول دیگر</a>
        </div>
        <div class="card cart-help">
          <span class="svc-icon">{icon("phone")}</span>
          <h3>سفارش تلفنی</h3>
          <p>می‌خواهید سفارش خود را تلفنی ثبت کنید؟ کارشناسان ما در ساعات کاری پاسخ‌گو هستند.</p>
          <a class="btn btn-outline btn-block" href="tel:{SITE['phone_link']}">{SITE['phone']}</a>
        </div>
      </aside>
    </div>
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    {section_head("محصولات پیشنهادی", "تکمیل‌کننده‌های سفارش شما", "مشتریانی که این محصولات را خریده‌اند، موارد زیر را هم انتخاب کرده‌اند.", align="center")}
    <div class="grid grid-3">{''.join(product_card(s) for s in [STONES[9], STONES[6], STONES[4]])}</div>
  </div>
</section>'''


def checkout(t):
    methods = [("bar" , "ارسال با باربری", "مناسب بارهای سنگین و شهرستان", True),
               ("post", "پست پیشتاز", "مناسب سفارش‌های کوچک تا ۳۰ کیلوگرم", False),
               ("pickup", "تحویل حضوری در کارخانه", "چهاردانگه تهران – بدون هزینه حمل", False)]
    ship = "".join(f'''<label class="pay-row"><input type="radio" name="ship" {'checked' if ok else ''}>
      <span class="pay-body"><strong>{n}</strong><small>{d}</small></span>
      <span class="pay-tag">{'پیشنهاد عصرجدید' if ok else ''}</span></label>''' for _, n, d, ok in methods)
    pays = [("online", "پرداخت آنلاین (درگاه بانکی)", "امن، سریع و با امکان صدور فاکتور رسمی", True),
            ("card", "کارت به کارت", "ارسال تصویر فیش پس از واریز", False),
            ("credit", "خرید اعتباری سازمانی", "برای مشتریان سازمانی با قرارداد فعال", False)]
    payrows = "".join(f'''<label class="pay-row"><input type="radio" name="pay" {'checked' if ok else ''}>
      <span class="pay-body"><strong>{n}</strong><small>{d}</small></span></label>''' for _, n, d, ok in pays)
    return f'''
{page_hero("تسویه حساب", "اطلاعات ارسال و پرداخت را تکمیل کنید", [("صفحه اصلی", "index.html"), ("سبد خرید", "cart.html"), ("تسویه حساب", "")])}
<section class="section">
  <div class="container">
    <div class="cart-steps">
      <span class="cs-item done"><i>{icon("check")}</i> سبد خرید</span><span class="cs-line done"></span>
      <span class="cs-item active"><i>۲</i> اطلاعات ارسال</span><span class="cs-line"></span>
      <span class="cs-item"><i>۳</i> پرداخت</span><span class="cs-line"></span>
      <span class="cs-item"><i>۴</i> سفارش کامل</span>
    </div>
    <div class="checkout-layout">
      <form class="checkout-main form js-form" novalidate>
        <div class="card form-card">
          <h3 class="card-title">{icon("user")} اطلاعات خریدار</h3>
          <div class="form-grid">
            <div class="field"><label>نام</label><input type="text" value="رضا" required></div>
            <div class="field"><label>نام خانوادگی</label><input type="text" value="محمدی" required></div>
            <div class="field"><label>شماره همراه</label><input type="tel" value="۰۹۱۲۱۱۱۲۲۳۳" required></div>
            <div class="field"><label>ایمیل</label><input type="email" value="reza.mohammadi@example.com"></div>
          </div>
        </div>
        <div class="card form-card">
          <h3 class="card-title">{icon("pin")} آدرس تحویل بار</h3>
          <div class="form-grid">
            <div class="field"><label>استان</label><select><option>تهران</option><option>البرز</option><option>اصفهان</option><option>خراسان رضوی</option><option>فارس</option></select></div>
            <div class="field"><label>شهر</label><input type="text" value="تهران" required></div>
            <div class="field full"><label>نشانی کامل</label><textarea rows="3" required>تهران، سعادت‌آباد، خیابان علامه شمالی، پلاک ۱۲۴، واحد ۷</textarea></div>
            <div class="field"><label>کد پستی</label><input type="text" value="۱۹۹۸۷۶۵۴۳۲"></div>
            <div class="field"><label>نام گیرنده بار</label><input type="text" value="رضا محمدی"></div>
            <div class="field full"><label>توضیحات سفارش (اختیاری)</label><textarea rows="2" placeholder="مثلاً: بار در ساعات ۸ تا ۱۲ تحویل داده شود."></textarea></div>
          </div>
        </div>
        <div class="card form-card">
          <h3 class="card-title">{icon("truck")} شیوه ارسال</h3>
          <div class="pay-list">{ship}</div>
        </div>
        <div class="card form-card">
          <h3 class="card-title">{icon("credit-card")} شیوه پرداخت</h3>
          <div class="pay-list">{payrows}</div>
          <label class="check-row check-terms"><input type="checkbox" required><span>قوانین و مقررات فروش عصرجدید را مطالعه کرده و می‌پذیرم.</span></label>
        </div>
        <div class="form-actions">
          <a class="btn btn-ghost" href="cart.html">{icon("arrow-right")} بازگشت به سبد خرید</a>
          <button class="btn btn-primary btn-lg" type="submit">{icon("lock")} پرداخت و ثبت سفارش</button>
        </div>
      </form>
      <aside class="checkout-side">
        <div class="card summary">
          <h3>خلاصه سفارش</h3>
          <ul class="mini-cart">
            <li><img src="assets/images/p-2.jpg" alt="نانوسنگ تراورتن"><span><strong>نانوسنگ نمای تراورتن کرم</strong><small>۴۵ مترمربع</small></span><b>۳۰٬۶۰۰٬۰۰۰</b></li>
            <li><img src="assets/images/p-5.jpg" alt="پنل سه‌بعدی"><span><strong>پنل سه‌بعدی موج اطلس</strong><small>۱۸ مترمربع</small></span><b>۸٬۱۰۰٬۰۰۰</b></li>
            <li><img src="assets/images/p-4.jpg" alt="آجرنما"><span><strong>آجرنما نسوز تراکوتا</strong><small>۶۰ مترمربع</small></span><b>۱۹٬۲۰۰٬۰۰۰</b></li>
          </ul>
          <ul class="sum-list">
            <li><span>جمع کالاها</span><strong>۵۷٬۹۰۰٬۰۰۰ تومان</strong></li>
            <li><span>مالیات بر ارزش افزوده</span><strong>۵٬۲۱۱٬۰۰۰ تومان</strong></li>
            <li><span>هزینه حمل</span><strong>۱٬۸۵۰٬۰۰۰ تومان</strong></li>
          </ul>
          <div class="sum-total"><span>مبلغ قابل پرداخت</span><strong>۶۴٬۹۶۱٬۰۰۰ تومان</strong></div>
          <div class="secure-badges">
            <span>{icon("shield")} پرداخت امن SSL</span><span>{icon("check-circle")} ضمانت اصل بودن کالا</span>
          </div>
        </div>
        <div class="card side-help">
          <span class="svc-icon">{icon("help")}</span>
          <h3>در ثبت سفارش مشکل دارید؟</h3>
          <p>برای ثبت سفارش از طریق تلفن یا بررسی موجودی، با ما تماس بگیرید.</p>
          <a class="btn btn-outline btn-block" href="tel:{SITE['phone_link']}">{icon("phone")} {SITE['phone']}</a>
        </div>
      </aside>
    </div>
  </div>
</section>'''


def contact(t):
    br = "".join(f'''<article class="card branch-card">
      <h3 class="card-title">{icon("building")} {b['city']}</h3>
      <ul class="f-contact-list">
        <li>{icon("pin")}<span>{b['address']}</span></li>
        <li>{icon("phone")}<a href="tel:+98">{b['phone']}</a></li>
        <li>{icon("clock")}<span>{b['hours']}</span></li>
      </ul></article>''' for b in BRANCHES)
    return f'''
{page_hero("تماس با ما", "پاسخ‌گویی ۷ روز هفته؛ از مشاوره فنی تا پیگیری سفارش", [("صفحه اصلی", "index.html"), ("تماس با ما", "")], bg="hero-3.jpg")}
<section class="section">
  <div class="container">
    <div class="contact-cards">
      <a class="contact-card" href="tel:{SITE['phone_link']}">{icon("phone")}<strong>{SITE['phone']}</strong><span>واحد فروش و مشاوره فنی</span></a>
      <a class="contact-card" href="mailto:{SITE['email']}">{icon("mail")}<strong>{SITE['email']}</strong><span>ایمیل رسمی شرکت</span></a>
      <a class="contact-card" href="#"><span class="cc-ico">{icon("wa")}</span><strong>{SITE['mobile']}</strong><span>واتس‌اپ (ارسال نقشه و عکس)</span></a>
      <div class="contact-card">{icon("pin")}<strong>{SITE['address_short']}</strong><span>کارخانه و نمایشگاه مرکزی</span></div>
    </div>
    <div class="contact-layout">
      <form class="card form-card contact-form js-form" novalidate>
        <h2 class="card-title">{icon("chat")} فرم تماس و استعلام قیمت</h2>
        <p class="card-text">فرم زیر را تکمیل کنید؛ کارشناس مربوطه در کمتر از ۲ ساعت کاری با شما تماس می‌گیرد.</p>
        <div class="form-grid">
          <div class="field"><label>نام و نام خانوادگی <span class="req">*</span></label><input type="text" required></div>
          <div class="field"><label>شماره همراه <span class="req">*</span></label><input type="tel" required></div>
          <div class="field"><label>ایمیل</label><input type="email"></div>
          <div class="field"><label>موضوع درخواست</label><select>
            <option>استعلام قیمت محصول</option><option>مشاوره فنی و انتخاب طرح</option>
            <option>پیگیری سفارش</option><option>همکاری و نمایندگی</option><option>سایر موارد</option></select></div>
          <div class="field"><label>نوع پروژه</label><select>
            <option>مسکونی</option><option>تجاری / اداری</option><option>صنعتی</option><option>بازسازی</option></select></div>
          <div class="field"><label>متراژ تقریبی (مترمربع)</label><input type="text" placeholder="مثلاً ۱۲۰"></div>
          <div class="field full"><label>توضیحات</label><textarea rows="5" placeholder="کاربری فضا، طرح مورد نظر، شهر پروژه و زمان‌بندی مورد انتظار را بنویسید…" required></textarea></div>
          <div class="field full"><label>پیوست نقشه یا عکس (اختیاری)</label>
            <div class="file-drop js-file-drop">{icon("upload")}<span>فایل نقشه، عکس یا لیست متراژ را اینجا رها کنید یا انتخاب نمایید</span><input type="file" hidden></div></div>
        </div>
        <label class="check-row"><input type="checkbox" required><span>با ثبت این فرم، با تماس کارشناسان عصرجدید موافقت می‌کنم.</span></label>
        <div class="form-actions"><button class="btn btn-primary btn-lg" type="submit">{icon("save")} ارسال درخواست</button></div>
      </form>
      <aside class="contact-side">
        <div class="card">
          <h3 class="card-title">{icon("clock")} ساعات کاری</h3>
          <ul class="hours-list">
            <li><span>شنبه تا چهارشنبه</span><strong>۸:۳۰ – ۱۷:۳۰</strong></li>
            <li><span>پنجشنبه</span><strong>۸:۳۰ – ۱۳:۰۰</strong></li>
            <li><span>جمعه</span><strong>تعطیل (پاسخ‌گویی تلفنی اضطراری)</strong></li>
          </ul>
        </div>
        <div class="card">
          <h3 class="card-title">{icon("share")} شبکه‌های اجتماعی</h3>
          <ul class="f-contact-list">
            <li>{icon("ig")}<a href="#">{SITE['instagram']}@</a></li>
            <li>{icon("tg")}<a href="#">{SITE['telegram']}@</a></li>
            <li>{icon("wa")}<span>{SITE['whatsapp']}</span></li>
            <li>{icon("in")}<a href="#">{SITE['linkedin']}</a></li>
          </ul>
        </div>
        <div class="card map-card">
          <h3 class="card-title">{icon("pin")} موقعیت روی نقشه</h3>
          <div class="map-embed">
            <div class="map-ph">{icon("map")}<strong>نقشه محل کارخانه عصرجدید</strong>
              <small>تهران، بزرگراه فتح، شهرک صنعتی چهاردانگه</small>
              <span class="map-chip">{icon("pin")} ۳۵٫۴۶۵۸° N، ۵۱٫۱۳۳۲° E</span></div>
          </div>
          <p class="muted">در صفحه واقعی، نقشه تعاملی (Google Maps یا نشان) در همین قاب بارگذاری می‌شود.</p>
        </div>
      </aside>
    </div>
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    {section_head("شعب و نمایندگی‌ها", "در شهرهای مختلف کنار شما هستیم", "برای بازدید حضوری از نمونه‌ها، نزدیک‌ترین نمایندگی را انتخاب کنید.")}
    <div class="grid grid-3">{br}</div>
  </div>
</section>
{cta_band("همکاری سازمانی و اخذ نمایندگی", "برای پروژه‌های انبوه، قرارداد تأمین و نمایندگی فروش، شرایط ویژه داریم.")}'''


def faq(t):
    return f'''
{page_hero("سوالات متداول", "پاسخ پرتکرارترین پرسش‌های مشتریان درباره محصولات، ارسال و ضمانت", [("صفحه اصلی", "index.html"), ("سوالات متداول", "")], bg="cat-4.jpg")}
<section class="section">
  <div class="container faq-layout">
    <div class="faq-main">
      <div class="faq-tabs filter-chips">
        <button class="chip-btn active" type="button">همه پرسش‌ها</button>
        <button class="chip-btn" type="button">خرید و سفارش</button>
        <button class="chip-btn" type="button">ارسال و تحویل</button>
        <button class="chip-btn" type="button">ضمانت و خدمات</button>
      </div>
      {faq_list()}
    </div>
    <aside class="faq-side">
      <div class="card side-help">
        <span class="svc-icon">{icon("chat")}</span>
        <h3>پاسخ سؤال خود را نیافتید؟</h3>
        <p>کارشناسان فنی عصرجدید آماده پاسخ‌گویی به پرسش‌های تخصصی شما هستند.</p>
        <a class="btn btn-primary btn-block" href="contact.html">ارسال پرسش</a>
        <a class="btn btn-outline btn-block" href="tel:{SITE['phone_link']}">{icon("phone")} تماس تلفنی</a>
      </div>
      <div class="card">
        <h3 class="card-title">{icon("help")} راهنمای سریع</h3>
        <ul class="side-nav">
          <li><a href="services.html">خدمات اجرایی<span>{icon("arrow-left")}</span></a></li>
          <li><a href="price-list.html">لیست قیمت ۱۴۰۴<span>{icon("arrow-left")}</span></a></li>
          <li><a href="terms.html">قوانین خرید<span>{icon("arrow-left")}</span></a></li>
          <li><a href="blog.html">راهنمای خرید<span>{icon("arrow-left")}</span></a></li>
        </ul>
      </div>
      <div class="card side-cta">{icon("download")}<h3>دانلود کاتالوگ محصولات</h3>
        <p>کاتالوگ کامل ۱۴۰۴ شامل مشخصات فنی، طرح‌ها و جدول قیمت.</p>
        <a class="btn btn-dark btn-block" href="price-list.html">{icon("download")} دانلود PDF</a></div>
    </aside>
  </div>
</section>
{cta_band()}
<section class="section section-soft">
  <div class="container">
    {section_head("مقالات آموزشی", "بیشتر بدانید: راهنمای خرید و نگهداری", align="center", more="blog.html")}
    <div class="grid grid-3">{blog_cards(3)}</div>
  </div>
</section>'''


def careers(t):
    jobs = "".join(f'''<article class="card job-card">
      <div class="job-head">
        <div><h3 class="card-title"><a href="job.html">{j['title']}</a></h3>
          <div class="card-meta"><span>{icon("building")} {j['dept']}</span><span>{icon("pin")} {j['location']}</span></div></div>
        <span class="badge badge-soft">{j['type']}</span>
      </div>
      <p class="card-text">{j['text'][:130]}…</p>
      <ul class="job-tags">
        <li>{icon("user")} {j['exp']}</li><li>{icon("wallet")} {j['salary']}</li><li>{icon("clock")} تمام‌وقت</li>
      </ul>
      <a class="btn btn-outline" href="job.html">مشاهده جزئیات و ارسال رزومه {icon("arrow-left")}</a>
    </article>''' for j in JOBS)
    return f'''
{page_hero("فرصت‌های شغلی", "به تیم ۶۸ نفره عصرجدید بپیوندید و آینده صنعت مصالح نوین را بسازید", [("صفحه اصلی", "index.html"), ("فرصت‌های شغلی", "")], bg="cat-5.jpg")}
<section class="section">
  <div class="container">
    {section_head("چرا عصرجدید؟", "چیزهایی که تجربه کاری ما را متفاوت می‌کند", "ما روی مهارت‌آموزی، ایمنی کار و پیشرفت شغلی اعضای تیم سرمایه‌گذاری می‌کنیم.")}
    <div class="grid grid-3">
      <article class="card value-card"><span class="svc-icon">{icon("trend-up")}</span><h3 class="card-title">مسیر رشد شفاف</h3><p class="card-text">برای هر نقش، مسیر ارتقای مهارتی و شغلی مشخص داریم و آموزش‌های دوره‌ای برگزار می‌شود.</p></article>
      <article class="card value-card"><span class="svc-icon">{icon("shield")}</span><h3 class="card-title">بیمه و ایمنی کامل</h3><p class="card-text">بیمه تأمین اجتماعی از روز اول، بیمه تکمیلی و تجهیزات ایمنی استاندارد در کارخانه و کارگاه‌ها.</p></article>
      <article class="card value-card"><span class="svc-icon">{icon("gift")}</span><h3 class="card-title">مزایا و پاداش عملکرد</h3><p class="card-text">پاداش فصلی بر اساس عملکرد، وام قرض‌الحسنه، سرویس رفت‌وآمد و تخفیف خرید محصولات شرکت.</p></article>
    </div>
  </div>
</section>
<section class="section section-soft">
  <div class="container">
    {section_head("موقعیت‌های باز", f"{fa_num(len(JOBS))} فرصت شغلی فعال", "برای ارسال رزومه، روی هر موقعیت کلیک کنید یا رزومه خود را به ایمیل منابع انسانی بفرستید.")}
    <div class="grid grid-2">{jobs}</div>
    <div class="card hr-card">
      {icon("mail")}
      <div><h3>رزومه خود را ارسال کنید</h3>
        <p>اگر موقعیت مناسبی برای شما در فهرست نیست، رزومه خود را به ایمیل <strong>hr@asrjadid.com</strong> ارسال کنید تا در بانک اطلاعاتی ما نگهداری شود.</p></div>
      <a class="btn btn-primary" href="mailto:hr@asrjadid.com">{icon("upload")} ارسال رزومه</a>
    </div>
  </div>
</section>'''


def job(t):
    j = JOBS[1]
    return f'''
{page_hero(j['title'], f"{j['dept']} — {j['location']} — {j['type']}", [("صفحه اصلی", "index.html"), ("فرصت‌های شغلی", "careers.html"), (j['title'][:30] + "…", "")])}
<section class="section">
  <div class="container job-layout">
    <div class="job-main">
      <div class="card job-summary">
        <ul>
          <li>{icon("building")}<span>دپارتمان</span><strong>{j['dept']}</strong></li>
          <li>{icon("pin")}<span>محل کار</span><strong>{j['location']}</strong></li>
          <li>{icon("user")}<span>سابقه مورد نیاز</span><strong>{j['exp']}</strong></li>
          <li>{icon("wallet")}<span>حقوق</span><strong>{j['salary']}</strong></li>
          <li>{icon("clock")}<span>نوع همکاری</span><strong>{j['type']}</strong></li>
        </ul>
      </div>
      <div class="prose">
        <h2>شرح موقعیت شغلی</h2>
        <p>{j['text']}</p>
        <h3>وظایف اصلی</h3>
        <ul>{''.join(f'<li>{d}</li>' for d in j['duties'])}</ul>
        <h3>شرایط مورد نیاز</h3>
        <ul>{''.join(f'<li>{r}</li>' for r in j['reqs'])}</ul>
        <h3>مزایای این موقعیت</h3>
        <ul>
          <li>بیمه تأمین اجتماعی از روز اول و بیمه تکمیلی</li>
          <li>محیط کاری فنی و آموزش مستمر نرم‌افزاری و تخصصی</li>
          <li>امکان رشد به موقعیت سرپرست دفتر فنی در ۲۴ ماه</li>
          <li>سرویس رفت‌وآمد و ناهار در محل کارخانه</li>
        </ul>
        <div class="info-box">{icon("alert")}<p><strong>فرآیند جذب:</strong> بررسی رزومه (۳ روز کاری) ← تماس تلفنی ← مصاحبه فنی ← مصاحبه منابع انسانی ← پیشنهاد همکاری. نتیجه همه مراحل به ایمیل شما اطلاع داده می‌شود.</p></div>
      </div>
      <form class="card form-card js-form" novalidate>
        <h3 class="card-title">{icon("upload")} ارسال رزومه</h3>
        <div class="form-grid">
          <div class="field"><label>نام و نام خانوادگی</label><input type="text" required></div>
          <div class="field"><label>شماره همراه</label><input type="tel" required></div>
          <div class="field"><label>ایمیل</label><input type="email" required></div>
          <div class="field"><label>سال‌های سابقه کار</label><select><option>۱ تا ۲ سال</option><option>۲ تا ۴ سال</option><option>۴ تا ۷ سال</option><option>بیش از ۷ سال</option></select></div>
          <div class="field full"><label>فایل رزومه (PDF، حداکثر ۵ مگابایت)</label>
            <div class="file-drop js-file-drop">{icon("upload")}<span>فایل رزومه خود را انتخاب کنید</span><input type="file" hidden></div></div>
          <div class="field full"><label>معرفی کوتاه و انگیزه شما برای این موقعیت</label><textarea rows="4"></textarea></div>
        </div>
        <div class="form-actions"><button class="btn btn-primary btn-lg" type="submit">{icon("save")} ارسال رزومه</button></div>
      </form>
    </div>
    <aside class="job-side">
      <div class="card side-help">
        <span class="svc-icon">{icon("phone")}</span>
        <h3>سؤالی دارید؟</h3>
        <p>واحد منابع انسانی عصرجدید، شنبه تا چهارشنبه ۹ تا ۱۶ پاسخ‌گوی شماست.</p>
        <a class="btn btn-outline btn-block" href="tel:{SITE['phone_link']}">{icon("phone")} تماس با منابع انسانی</a>
      </div>
      <div class="card">
        <h3 class="card-title">{icon("file")} موقعیت‌های دیگر</h3>
        <ul class="side-nav">{''.join(f'<li><a class="{"active" if x["slug"] == j["slug"] else ""}" href="job.html">{x["title"]}<span>{x["type"]}</span></a></li>' for x in JOBS)}</ul>
      </div>
      <div class="card">
        <h3 class="card-title">{icon("users")} تیم ما در یک نگاه</h3>
        <ul class="stats-mini">
          <li><strong>۶۸</strong><span>نفر پرسنل</span></li>
          <li><strong>۱۲</strong><span>سال میانگین سابقه سرپرستان</span></li>
          <li><strong>۹۴٪</strong><span>رضایت کارکنان از محیط کار</span></li>
        </ul>
      </div>
    </aside>
  </div>
</section>'''


def price_list(t):
    rows = ""
    for s in STONES:
        rows += f'''<tr data-cat="{s['cat']}">
      <td class="pl-prod"><img src="assets/images/{s['image']}" alt="{s['name']}"><span>{s['name']}<small>کد {s['code']}</small></span></td>
      <td>{cat_name(s['cat'])}</td><td>{s['size']}</td><td>{s['unit']}</td>
      <td class="pl-price">{fa_num(s['price'])}</td>
      <td>{'<span class="chip chip-ok">موجود</span>' if s['stock'] > 0 else '<span class="chip chip-warn">استعلامی</span>'}</td>
    </tr>'''
    return f'''
{page_hero("لیست قیمت ۱۴۰۴", "قیمت‌های به‌روز محصولات عصرجدید، بدون احتساب مالیات و هزینه حمل", [("صفحه اصلی", "index.html"), ("لیست قیمت", "")])}
<section class="section">
  <div class="container">
    <div class="notice-bar">{icon("alert")}
      <p>قیمت‌های این جدول آخرین بار در <strong>۱۴۰۴/۰۷/۰۱</strong> به‌روزرسانی شده و تا ۴۸ ساعت اعتبار دارد. برای قیمت قطعی، پیش‌فاکتور رسمی دریافت کنید.</p>
      <a class="btn btn-outline sm" href="contact.html">دریافت پیش‌فاکتور</a></div>
    <div class="table-wrap card">
      <div class="table-tools">
        <div class="filter-chips">{''.join(f'<button class="chip-btn{" active" if i == 0 else ""}" type="button" data-pfilter="{"all" if i == 0 else c["slug"]}">{c["name"]}</button>' for i, c in enumerate([{"slug": "all", "name": "همه"} ] + CATEGORIES))}</div>
        <div class="table-tools-left">
          <button class="btn btn-outline sm js-print" type="button">{icon("print")} چاپ</button>
          <button class="btn btn-primary sm" type="button">{icon("download")} دانلود Excel</button>
        </div>
      </div>
      <table class="table price-table" id="priceTable">
        <thead><tr><th>محصول</th><th>دسته‌بندی</th><th>ابعاد</th><th>واحد فروش</th><th>قیمت واحد (تومان)</th><th>وضعیت</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <div class="price-terms">
      <div class="card info-card"><span class="svc-icon">{icon("percent")}</span><h3 class="card-title">تخفیف پلکانی خرید</h3>
        <ul class="check-list">
          <li>{icon("check-circle")} ۵۰ تا ۲۰۰ مترمربع: ۲٪ تخفیف</li>
          <li>{icon("check-circle")} ۲۰۰ تا ۵۰۰ مترمربع: ۴٪ تخفیف</li>
          <li>{icon("check-circle")} بیش از ۵۰۰ مترمربع: تا ۸٪ تخفیف + مشاوره اختصاصی</li>
        </ul></div>
      <div class="card info-card"><span class="svc-icon">{icon("truck")}</span><h3 class="card-title">شرایط حمل و پرداخت</h3>
        <ul class="check-list">
          <li>{icon("check-circle")} ارسال رایگان در تهران و کرج برای سفارش بالای ۵۰ مترمربع</li>
          <li>{icon("check-circle")} حمل شهرستان با باربری، مطابق تعرفه و به عهده خریدار</li>
          <li>{icon("check-circle")} ۳۰٪ پیش‌پرداخت، مانده پس از آماده‌سازی بار</li>
        </ul></div>
    </div>
  </div>
</section>
{cta_band()}
<section class="section section-soft">
  <div class="container">{section_head("پرسش‌های قیمتی", "سوالات متداول درباره قیمت و پرداخت", align="center", more="faq.html")}
    {faq_list()}</div>
</section>'''
