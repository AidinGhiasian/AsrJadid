using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages
{
    public class CategoriesModel : PageModel
    {
        private readonly IStoneCategoryApplication _categoryApplication;

        public CategoriesModel(IStoneCategoryApplication categoryApplication)
        {
            _categoryApplication = categoryApplication;
        }

        public List<StoneCategoryViewModel> Categories { get; set; } = new();

        public void OnGet()
        {
            Categories = _categoryApplication.GetAll();
        }
    }
}
