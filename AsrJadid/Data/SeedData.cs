using AccountManagment.Domain.Domain.Account.Agg;
using AccountManagment.Domain.Domain.Roles.Agg;
using AccountManagment.Infrastructure;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Services.Application.HashPassword;
using Services.Models;
using StoneManagement.Domain.Stone.Agg;
using StoneManagement.Domain.StoneCategory.Agg;
using StoneManagement.Infrastructure;
using System.Data;

namespace AsrJadid.Data
{
    /// <summary>
    /// داده‌های اولیه پروژه؛ در اولین اجرا نقش‌ها، کاربر مدیر، دسته‌بندی‌ها و محصولات نمونه را می‌سازد.
    /// </summary>
    public static class SeedData
    {
        public static void Initialize(IServiceProvider services)
        {
            var stoneDb = services.GetRequiredService<StoneDbContext>();
            var accountDb = services.GetRequiredService<AccountDbContext>();

            // بدون Migration؛ اگر پایگاه داده نبود ساخته می‌شود
            stoneDb.Database.EnsureCreated();
            EnsureAccountTables(accountDb);

            SeedRoles(accountDb);
            SeedAccounts(accountDb, services.GetRequiredService<IPasswordHasher>());
            SeedStones(stoneDb);
        }

        private static void SeedRoles(AccountDbContext db)
        {
            if (db.Roles.Any()) return;

            db.Roles.Add(new Roles("مدیر سایت"));
            db.Roles.Add(new Roles("کاربر"));
            db.SaveChanges();
        }

        private static void SeedAccounts(AccountDbContext db, IPasswordHasher passwordHasher)
        {
            if (db.Accounts.Any()) return;

            // مدیر پیش‌فرض: 09159861216 / admin123
            const string adminPhone = "09159861216";
            const string legacyAdminPhone = "09121112233";

            if (!db.Accounts.Any(x => x.PhoneNumber == adminPhone))
            {
                var legacy = db.Accounts.FirstOrDefault(x => x.PhoneNumber == legacyAdminPhone);

                if (legacy != null)
                {
                    // انتقال شماره قدیمی مدیر به شماره جدید (برای پایگاه داده‌های قبلی)
                    legacy.Edit(legacy.Name, legacy.Family, adminPhone, legacy.Email ?? string.Empty, legacy.BirthDate ?? default, legacy.Address ?? string.Empty, legacy.Picture ?? string.Empty);
                }
                else
                {
                    db.Accounts.Add(new Accounts(string.Empty, "مدیر", "عصرجدید", adminPhone, "تهران", passwordHasher.Hash("admin123"), "admin@asrjadid.com"));
                }

                db.SaveChanges();
            }

            var admin = db.Accounts.First(x => x.PhoneNumber == adminPhone);
            admin.ChangeRole(long.Parse(RolesCode.Admin));
            db.SaveChanges();
        }

        private static void SeedStones(StoneDbContext db)
        {
            if (db.Categories.Any()) return;

            // دسته‌بندی‌ها
            var categories = new List<StoneCategory>
            {
                new StoneCategory("نما و فاساد", "نانوسنگ، تراورتن و پوشش‌های نمای ساختمان با مقاومت بالا در برابر رطوبت و اشعه UV.", "assets/images/cat-1.jpg"),
                new StoneCategory("کفپوش و دیوارپوش", "صفحات یکپارچه کف و دیوار با سطح ضدخش، لکه‌ناپذیر و قابل ترمیم.", "assets/images/cat-2.jpg"),
                new StoneCategory("پنل سه‌بعدی", "پنل‌های برجسته سه‌بعدی برای دیوارپوش داخلی، لابی و فضاهای تجاری.", "assets/images/cat-3.jpg"),
                new StoneCategory("کورین و صفحات یکپارچه", "صفحات یکپارچه کورین برای کانتر، کابینت، سینک و سطوح بدون درز.", "assets/images/cat-4.jpg"),
                new StoneCategory("آجر و سنگ آنتیک", "آجرنما و سنگ آنتیک مصنوعی با بافت طبیعی و رنگ‌بندی گرم.", "assets/images/cat-5.jpg"),
                new StoneCategory("صفحات کوارتز", "صفحات کوارتز درجه یک با سختی بالا، سطح غیرمتخلخل و گارانتی ۱۰ ساله.", "assets/images/cat-6.jpg"),
            };

            db.Categories.AddRange(categories);
            db.SaveChanges();

            var catId = categories.ToDictionary(x => x.Slug, x => x.Id);

            // محصولات نمونه
            var stones = new List<Stones>
            {
                new Stones("assets/images/p-1.jpg", "صفحه کوارتز سفید برفی", 320, 160, 31, 2850000m, 1240, "سفید", "کوارتز سفید برفی با سطح براق و لکه‌ناپذیر، انتخابی بی‌نقص برای صفحه کابینت آشپزخانه‌های روشن.", catId["quartz"]),
                new Stones("assets/images/p-3.jpg", "صفحه کوارتز آنتراسیت مات", 320, 160, 31, 3150000m, 860, "مشکی", "کوارتز آنتراسیت مات با بافت مخملی؛ ترکیبی مدرن از تیره‌ی آرام و سطح مات بدون اثر انگشت.", catId["quartz"]),
                new Stones("assets/images/p-2.jpg", "نانوسنگ نمای تراورتن کرم", 320, 160, 31, 680000m, 2400, "کرم", "نانوسنگ نمای تراورتن کرم با بافت طبیعی و جذب آب زیر ۱٪؛ پوشش نمای مقاوم و کم‌هزینه.", catId["facade"]),
                new Stones("assets/images/p-9.jpg", "کفپوش نانوسنگ لاین‌بورن گری", 320, 160, 31, 720000m, 3100, "طوسی", "کفپوش نانوسنگ با طرح لاین‌بورن گری و رگه‌های طبیعی؛ مقاوم به خط‌وخش و لغزش.", catId["floor"]),
                new Stones("assets/images/p-5.jpg", "پنل سه‌بعدی موج اطلس", 320, 160, 31, 450000m, 1900, "سفید صدفی", "پنل سه‌بعدی موج اطلس؛ برجستگی نرم و سایه‌پردازی طبیعی برای دیوار شاخص داخلی.", catId["three-d"]),
                new Stones("assets/images/p-4.jpg", "آجرنما نسوز تراکوتا", 320, 160, 31, 320000m, 5200, "آجری", "آجرنما نسوز تراکوتا با رنگ‌آمیزی دستی و بافت طبیعی؛ اقتصادی‌ترین راه رسیدن به نمای آجری.", catId["antique"]),
                new Stones("assets/images/p-6.jpg", "سنگ آنتیک کوهی مسی", 320, 160, 31, 395000m, 1700, "مسی", "سنگ آنتیک کوهی مسی با تنوع رنگی گرم و بافت کوهی؛ مناسب دیوار شاخص و نمای کافه.", catId["antique"]),
                new Stones("assets/images/p-10.jpg", "صفحه کورین یکپارچه سفید", 320, 160, 31, 3600000m, 620, "سفید", "صفحه کورین یکپارچه با اتصال نامرئی و قابلیت ترمیم موضعی؛ بدون درز، بدون درزگیر سیاه.", catId["corian"]),
                new Stones("assets/images/p-11.jpg", "سینک کورین یکپارچه", 320, 160, 31, 9500000m, 145, "سفید", "سینک کورین یکپارچه که بدون درز به صفحه کانتر متصل می‌شود؛ بهداشتی، عمیق و بی‌صدا.", catId["corian"]),
                new Stones("assets/images/p-7.jpg", "قرنیز و ابزاره نانو سنگ", 320, 160, 31, 185000m, 4100, "سفید", "قرنیز نانوسنگ در پروفیل‌های متنوع؛ جایگزین دائمی قرنیز MDF در فضاهای مرطوب.", catId["facade"]),
                new Stones("assets/images/p-8.jpg", "پله کوارتز آنتراسیت", 320, 160, 31, 1900000m, 380, "مشکی براق", "پله کوارتز با لبه گرد و سطح ضدلغزش؛ اجرای لوکس راه‌پله‌های داخلی و تجاری.", catId["quartz"]),
                new Stones("assets/images/p-2.jpg", "دیوارپوش تراورتن رگه‌ای", 320, 160, 31, 890000m, 1450, "شیری", "دیوارپوش تراورتن رگه‌ای با رگه‌های ممتد و اتصال بدون اپل؛ دیوارهای بلند یکپارچه.", catId["floor"]),
            };

            db.Stones.AddRange(stones);
            db.SaveChanges();
        }

        private static void EnsureAccountTables(AccountDbContext db)
        {
            if (TableExists(db, "Roles")) return;

            var creator = db.GetService<IRelationalDatabaseCreator>();
            creator.CreateTables();
        }

        private static bool TableExists(DbContext db, string tableName)
        {
            var connection = db.Database.GetDbConnection();
            var shouldClose = connection.State != ConnectionState.Open;
            if (shouldClose) connection.Open();

            try
            {
                using var command = connection.CreateCommand();
                command.CommandText = "SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = @name";
                var parameter = command.CreateParameter();
                parameter.ParameterName = "@name";
                parameter.Value = tableName;
                command.Parameters.Add(parameter);

                return Convert.ToInt32(command.ExecuteScalar()) > 0;
            }
            finally
            {
                if (shouldClose) connection.Close();
            }
        }
    }
}
