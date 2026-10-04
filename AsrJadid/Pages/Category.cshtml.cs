using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages
{
    public class CategoryModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;
        private readonly IStoneCategoryApplication _categoryApplication;

        public CategoryModel(IStoneApplication stoneApplication, IStoneCategoryApplication categoryApplication)
        {
            _stoneApplication = stoneApplication;
            _categoryApplication = categoryApplication;
        }

        public StoneCategoryViewModel? Category { get; set; }
        public List<StoneViewModel> Products { get; set; } = new();
        public List<StoneCategoryViewModel> Categories { get; set; } = new();

        public void OnGet(string? slug = null)
        {
            Categories = _categoryApplication.GetAll();

            if (!string.IsNullOrWhiteSpace(slug))
            {
                // امکان ورود هم با شناسه و هم با نامک (slug)
                Category = long.TryParse(slug, out var id)
                    ? _categoryApplication.GetInfo(id)
                    : _categoryApplication.GetBySlug(slug);
            }

            if (Category != null)
            {
                Products = _stoneApplication.GetByCategory(Category.Id);
                ViewData["Title"] = Category.Name;
            }
            else
            {
                Products = _stoneApplication.GetList();
                ViewData["Title"] = "دسته‌بندی محصولات";
            }
        }
    }
}
