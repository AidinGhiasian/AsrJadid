using AccountManagment.Application.Contracts.AccountModels;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages.Admin
{
    public class StonesModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;
        private readonly IStoneCategoryApplication _stoneCategoryApplication;

        public StonesModel(IStoneApplication stoneApplication, IStoneCategoryApplication stoneCategoryApplication)
        {
            _stoneApplication = stoneApplication;
            _stoneCategoryApplication = stoneCategoryApplication;
        }

        public List<StoneViewModel> Stones { get; set; } = new();
        public List<StoneCategoryViewModel> Categories { get; set; } = new();

        [BindProperty(SupportsGet = true)]
        public string? Query { get; set; }

        [BindProperty(SupportsGet = true, Name = "cat")]
        public long CategoryId { get; set; }

        public string? SuccessMessage { get; set; }
        public string? ErrorMessage { get; set; }

        public void OnGet()
        {
            Categories = _stoneCategoryApplication.GetAll();

            var all = _stoneApplication.GetList();

            if (CategoryId > 0)
                all = all.Where(x => x.CategoryId == CategoryId).ToList();

            if (!string.IsNullOrWhiteSpace(Query))
            {
                var q = Query.Trim();
                all = all.Where(x => x.StoneName.Contains(q) || x.Color.Contains(q) || x.Id.ToString() == q).ToList();
            }

            Stones = all;
            SuccessMessage = TempData["Success"] as string;
            ErrorMessage = TempData["Error"] as string;
        }

        public IActionResult OnPostDelete(long id)
        {
            var result = _stoneApplication.Delete(id);

            if (result.Success)
                TempData["Success"] = "محصول با موفقیت حذف شد.";
            else
                TempData["Error"] = result.Message;

            return RedirectToPage("/Admin/Stones");
        }
    }
}
