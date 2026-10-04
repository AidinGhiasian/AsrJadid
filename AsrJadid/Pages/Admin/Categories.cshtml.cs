using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages.Admin
{
    public class CategoriesModel : PageModel
    {
        private readonly IStoneCategoryApplication _stoneCategoryApplication;

        public CategoriesModel(IStoneCategoryApplication stoneCategoryApplication)
        {
            _stoneCategoryApplication = stoneCategoryApplication;
        }

        [BindProperty]
        public EditViewModel Input { get; set; } = new();

        public List<StoneCategoryViewModel> Categories { get; set; } = new();

        public string? SuccessMessage { get; set; }
        public string? ErrorMessage { get; set; }

        public void OnGet(long? edit)
        {
            Categories = _stoneCategoryApplication.GetAll();

            if (edit.HasValue && edit.Value > 0)
            {
                var details = _stoneCategoryApplication.GetDetails(edit.Value);
                if (details != null)
                {
                    Input = details;
                }
            }

            SuccessMessage = TempData["Success"] as string;
            ErrorMessage = TempData["Error"] as string;
        }

        public IActionResult OnPost()
        {
            if (string.IsNullOrWhiteSpace(Input.Name))
            {
                ErrorMessage = "نام دسته‌بندی را وارد کنید.";
                Categories = _stoneCategoryApplication.GetAll();
                return Page();
            }

            var result = Input.Id > 0
                ? _stoneCategoryApplication.Edit(Input)
                : _stoneCategoryApplication.Create(Input);

            if (!result.Success)
            {
                ErrorMessage = result.Message;
                Categories = _stoneCategoryApplication.GetAll();
                return Page();
            }

            TempData["Success"] = result.Message;
            return RedirectToPage("/Admin/Categories");
        }

        public IActionResult OnPostDelete(long id)
        {
            var result = _stoneCategoryApplication.Delete(id);

            if (result.Success)
                TempData["Success"] = "دسته‌بندی حذف شد.";
            else
                TempData["Error"] = result.Message;

            return RedirectToPage("/Admin/Categories");
        }
    }
}
