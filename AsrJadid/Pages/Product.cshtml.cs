using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.Stone;

namespace AsrJadid.Pages
{
    public class ProductModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;

        public ProductModel(IStoneApplication stoneApplication)
        {
            _stoneApplication = stoneApplication;
        }

        public StoneViewModel? Product { get; set; }
        public List<string> Gallery { get; set; } = new();
        public List<string> Colors { get; set; } = new();
        public List<StoneViewModel> Related { get; set; } = new();
        public bool InStock => Product != null && Product.Stock > 0;

        public IActionResult OnGet(long? id)
        {
            var all = _stoneApplication.GetList();

            Product = id.HasValue ? all.FirstOrDefault(x => x.Id == id.Value) : all.FirstOrDefault();

            if (Product == null)
            {
                return RedirectToPage("/Products");
            }

            Gallery = new List<string> { Product.Picture };
            Gallery.AddRange(Product.Pictures.Where(x => !string.IsNullOrWhiteSpace(x)));
            Gallery = Gallery.Select(x => x.ImageUrl()).Distinct().ToList();

            Related = all
                .Where(x => x.CategoryId == Product.CategoryId && x.Id != Product.Id)
                .Take(4)
                .ToList();

            if (Related.Count == 0)
            {
                Related = all.Where(x => x.Id != Product.Id).Take(4).ToList();
            }

            Colors = all
                .Where(x => x.CategoryId == Product.CategoryId)
                .Select(x => x.Color)
                .Where(x => !string.IsNullOrWhiteSpace(x))
                .Distinct()
                .ToList();

            if (Colors.Count == 0)
            {
                Colors.Add(Product.Color);
            }

            return Page();
        }
    }
}
