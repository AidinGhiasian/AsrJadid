using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages
{
    public class ProductsModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;
        private readonly IStoneCategoryApplication _categoryApplication;

        public ProductsModel(IStoneApplication stoneApplication, IStoneCategoryApplication categoryApplication)
        {
            _stoneApplication = stoneApplication;
            _categoryApplication = categoryApplication;
        }

        public List<StoneViewModel> Products { get; set; } = new();
        public List<StoneCategoryViewModel> Categories { get; set; } = new();
        public List<string> Colors { get; set; } = new();
        public string? Query { get; set; }
        public string? CategorySlug { get; set; }

        public void OnGet(string? q = null, string? cat = null)
        {
            Query = q;
            CategorySlug = cat;

            Categories = _categoryApplication.GetAll();

            if (!string.IsNullOrWhiteSpace(q))
            {
                Products = _stoneApplication.Search(q.Trim()).Select(Map).ToList();
            }
            else
            {
                Products = _stoneApplication.GetList();
            }

            if (!string.IsNullOrWhiteSpace(cat))
            {
                Products = Products.Where(x => string.Equals(x.CategorySlug, cat, StringComparison.OrdinalIgnoreCase)).ToList();
            }

            Colors = Products
                .Select(x => x.Color)
                .Where(x => !string.IsNullOrWhiteSpace(x))
                .Distinct()
                .ToList();
        }

        private static StoneViewModel Map(SearchViewModel search)
        {
            return new StoneViewModel
            {
                Id = search.Id,
                Picture = search.Picture,
                StoneName = search.StoneName,
                Length = search.Length,
                Width = search.Width,
                Weight = search.Weight,
                Price = search.Price,
                Stock = search.Stock,
                Color = search.Color,
                Description = search.Description,
                CategoryId = search.CategoryId
            };
        }
    }
}
