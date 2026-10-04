using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages.Admin
{
    public class StoneFormModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;
        private readonly IStoneCategoryApplication _stoneCategoryApplication;

        public StoneFormModel(IStoneApplication stoneApplication, IStoneCategoryApplication stoneCategoryApplication)
        {
            _stoneApplication = stoneApplication;
            _stoneCategoryApplication = stoneCategoryApplication;
        }

        [BindProperty]
        public EditViewModel Input { get; set; } = new();

        public List<StoneCategoryViewModel> Categories { get; set; } = new();
        public string? ErrorMessage { get; set; }

        public IActionResult OnGet(long? id)
        {
            Categories = _stoneCategoryApplication.GetAll();

            if (id.HasValue && id.Value > 0)
            {
                var details = _stoneApplication.GetDetails(id.Value);
                if (details == null)
                {
                    return RedirectToPage("/Admin/Stones");
                }

                Input = details;
            }

            return Page();
        }

        public IActionResult OnPost()
        {
            Categories = _stoneCategoryApplication.GetAll();

            if (string.IsNullOrWhiteSpace(Input.StoneName) || Input.CategoryId <= 0)
            {
                ErrorMessage = "نام محصول و دسته‌بندی الزامی است.";
                return Page();
            }

            var result = Input.Id > 0
                ? _stoneApplication.Edit(Input)
                : _stoneApplication.Create(Input);

            if (!result.Success)
            {
                ErrorMessage = result.Message;
                return Page();
            }

            TempData["Success"] = result.Message;
            return RedirectToPage("/Admin/Stones");
        }
    }
}
