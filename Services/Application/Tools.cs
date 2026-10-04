using System;
using System.Globalization;
using System.IO;

namespace Services.Application
{
    public static class Tools
    {
        public static string[] MonthNames =
            {"فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"};

        public static string[] DayNames = {"شنبه", "یکشنبه", "دو شنبه", "سه شنبه", "چهار شنبه", "پنج شنبه", "جمعه"};

        private static readonly string[] Pn = {"۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"};
        private static readonly string[] En = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

        // ایندکس این آرایه بر اساس مقدار DayOfWeek است (Sunday = 0)
        private static readonly string[] FaWeek = {"یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه", "جمعه", "شنبه"};

        public static string ToFarsi(this DateTime? date)
        {
            try
            {
                if (date != null) return date.Value.ToFarsi();
            }
            catch (Exception)
            {
                return "";
            }

            return "";
        }

        public static string ToFarsi(this DateTime date)
        {
            if (date == new DateTime()) return "";
            var pc = new PersianCalendar();
            return $"{pc.GetYear(date)}/{pc.GetMonth(date):00}/{pc.GetDayOfMonth(date):00}";
        }

        public static string ToWeekEnglishToFarsi(this DateTime date)
        {
            return FaWeek[(int)date.DayOfWeek];
        }

        public static string ToDiscountFormat(this DateTime date)
        {
            if (date == new DateTime()) return "";
            return $"{date.Year}/{date.Month}/{date.Day}";
        }

        public static string GetTime(this DateTime date)
        {
            return $"_{date.Hour:00}_{date.Minute:00}_{date.Second:00}";
        }

        public static string ToFarsiFull(this DateTime date)
        {
            var pc = new PersianCalendar();
            return
                $"{pc.GetYear(date)}/{pc.GetMonth(date):00}/{pc.GetDayOfMonth(date):00} - {date.Hour:00}:{date.Minute:00}:{date.Second:00}";
        }

        public static string ToEnglishNumber(this string strNum)
        {
            if (string.IsNullOrEmpty(strNum)) return strNum;

            var cash = strNum;
            for (var i = 0; i < 10; i++)
                cash = cash.Replace(Pn[i], En[i]);
            return cash;
        }

        public static string ToPersianNumber(this int intNum)
        {
            return intNum.ToString().ToPersianNumber();
        }

        public static string ToPersianNumber(this long longNum)
        {
            return longNum.ToString().ToPersianNumber();
        }

        public static string ToPersianNumber(this decimal decimalNum)
        {
            return decimalNum.ToString(CultureInfo.InvariantCulture).ToPersianNumber();
        }

        public static string ToPersianNumber(this double doubleNum)
        {
            return doubleNum.ToString(CultureInfo.InvariantCulture).ToPersianNumber();
        }

        public static string ToPersianNumber(this string strNum)
        {
            if (string.IsNullOrEmpty(strNum)) return strNum ?? string.Empty;

            var chash = strNum;
            for (var i = 0; i < 10; i++)
                chash = chash.Replace(En[i], Pn[i]);
            return chash;
        }

        public static DateTime? FromFarsiDate(this string InDate)
        {
            if (string.IsNullOrEmpty(InDate))
                return null;

            var spited = InDate.Split('/');
            if (spited.Length < 3)
                return null;

            if (!int.TryParse(spited[0].ToEnglishNumber(), out var year))
                return null;

            if (!int.TryParse(spited[1].ToEnglishNumber(), out var month))
                return null;

            if (!int.TryParse(spited[2].ToEnglishNumber(), out var day))
                return null;
            var c = new PersianCalendar();
            return c.ToDateTime(year, month, day, 0, 0, 0, 0);
        }

        public static DateTime ToGeorgianDateTime(this string persianDate)
        {
            persianDate = persianDate.ToEnglishNumber();
            var year = Convert.ToInt32(persianDate.Substring(0, 4));
            var month = Convert.ToInt32(persianDate.Substring(5, 2));
            var day = Convert.ToInt32(persianDate.Substring(8, 2));
            return new DateTime(year, month, day, new PersianCalendar());
        }

        public static string ToMoney(this double myMoney)
        {
            return myMoney.ToString("N0", CultureInfo.CreateSpecificCulture("fa-ir"));
        }

        public static string ToMoney(this decimal myMoney)
        {
            return myMoney.ToString("N0", CultureInfo.CreateSpecificCulture("fa-ir"));
        }

        public static string ToFileName(this DateTime date)
        {
            return $"{date.Year:0000}-{date.Month:00}-{date.Day:00}-{date.Hour:00}-{date.Minute:00}-{date.Second:00}";
        }

        /// <summary>
        /// آدرس تصویر را بر اساس نوع مسیر ذخیره‌شده برمی‌گرداند؛
        /// تصاویر پیش‌فرض قالب داخل assets و تصاویر آپلودشده داخل Pictures هستند.
        /// </summary>
        public static string ImageUrl(this string? picture)
        {
            if (string.IsNullOrWhiteSpace(picture))
                return "/assets/images/placeholder.jpg";

            var path = picture.Replace("\\", "/").TrimStart('/');

            if (path.StartsWith("assets/", StringComparison.OrdinalIgnoreCase))
                return "/" + path;

            if (path.StartsWith("Pictures/", StringComparison.OrdinalIgnoreCase))
                return "/" + path;

            return "/Pictures/" + path;
        }
    }
}
