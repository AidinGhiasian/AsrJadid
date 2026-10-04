using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Services.Application;
using StoneManagement.Application.Contracts.Stone;

namespace AsrJadid.Pages.Api
{
    /// <summary>
    /// نقطه اتصال سبک سمت کلاینت به داده‌های واقعی محصولات.
    /// سبد خرید، علاقه‌مندی‌ها و مقایسه در مرورگر نگهداری می‌شوند و این صفحه
    /// فقط شناسه‌ها را می‌گیرد و اطلاعات کامل محصولات را برمی‌گرداند.
    /// </summary>
    public class BasketModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;

        public BasketModel(IStoneApplication stoneApplication)
        {
            _stoneApplication = stoneApplication;
        }

        public IActionResult OnGetItems(string? ids)
        {
            var list = new List<object>();

            if (string.IsNullOrWhiteSpace(ids))
            {
                return new JsonResult(list);
            }

            var keys = ids
                .ToEnglishNumber()
                .Split(new[] { ',', ';', '|' }, StringSplitOptions.RemoveEmptyEntries)
                .Select(x => long.TryParse(x.Trim(), out var id) ? id : 0)
                .Where(x => x > 0)
                .Distinct()
                .ToList();

            if (keys.Count == 0)
            {
                return new JsonResult(list);
            }

            var all = _stoneApplication.GetList();

            foreach (var id in keys)
            {
                var stone = all.FirstOrDefault(x => x.Id == id);

                if (stone == null)
                    continue;

                list.Add(new
                {
                    id = stone.Id,
                    name = stone.StoneName,
                    slug = stone.Id,
                    category = stone.CategoryName,
                    categorySlug = stone.CategorySlug,
                    color = stone.Color,
                    code = stone.Id,
                    price = stone.Price,
                    priceText = stone.Price.ToMoney(),
                    image = stone.Picture.ImageUrl(),
                    stock = stone.Stock,
                    size = stone.Length.ToPersianNumber() + " × " + stone.Width.ToPersianNumber(),
                    weight = stone.Weight.ToPersianNumber(),
                    url = "/Product/" + stone.Id
                });
            }

            return new JsonResult(list);
        }

        /// <summary>پیشنهاد محصولات برای تکمیل سبد؛ بر اساس دسته‌بندی محصولات موجود در سبد.</summary>
        public IActionResult OnGetSuggest(string? ids, int take = 3)
        {
            var all = _stoneApplication.GetList();

            if (all.Count == 0 || take <= 0)
            {
                return new JsonResult(new List<object>());
            }

            var keys = (ids ?? string.Empty)
                .ToEnglishNumber()
                .Split(new[] { ',', ';', '|' }, StringSplitOptions.RemoveEmptyEntries)
                .Select(x => long.TryParse(x.Trim(), out var id) ? id : 0)
                .Where(x => x > 0)
                .ToList();

            var inBasket = all.Where(x => keys.Contains(x.Id)).ToList();
            var categories = inBasket.Select(x => x.CategoryId).Distinct().ToList();

            var suggestions = all
                .Where(x => !keys.Contains(x.Id))
                .OrderByDescending(x => categories.Contains(x.CategoryId))
                .ThenByDescending(x => x.Id)
                .Take(take)
                .ToList();

            return new JsonResult(suggestions);
        }

        /// <summary>جستجوی سریع برای نوار جستجوی هدر.</summary>
        public IActionResult OnGetSearch(string? q, int take = 6)
        {
            if (string.IsNullOrWhiteSpace(q) || take <= 0)
            {
                return new JsonResult(new List<object>());
            }

            var results = _stoneApplication
                .Search(q.Trim())
                .Take(take)
                .Select(x => new { id = x.Id, name = x.StoneName, priceText = x.Price.ToMoney(), url = "/Product/" + x.Id })
                .ToList();

            return new JsonResult(results);
        }
    }
}
