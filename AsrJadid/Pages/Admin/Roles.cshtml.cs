using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using AccountManagment.Application.Contracts.AccountModels;
using AccountManagment.Application.Contracts.RoleModels;

namespace AsrJadid.Pages.Admin
{
    public class RolesModel : PageModel
    {
        private readonly IRoleApplication _roleApplication;
        private readonly IAccountApplication _accountApplication;

        public RolesModel(IRoleApplication roleApplication, IAccountApplication accountApplication)
        {
            _roleApplication = roleApplication;
            _accountApplication = accountApplication;
        }

        [BindProperty]
        public EditViewModel Input { get; set; } = new();

        public List<RoleViewModel> Roles { get; set; } = new();
        public List<AccountViewModel> Accounts { get; set; } = new();

        public string? SuccessMessage { get; set; }
        public string? ErrorMessage { get; set; }

        public void OnGet(long? edit)
        {
            Roles = _roleApplication.RoleList();
            Accounts = _accountApplication.GetList(true);

            if (edit.HasValue && edit.Value > 0)
            {
                Input = _roleApplication.GetDetails(edit.Value) ?? new EditViewModel();
            }

            SuccessMessage = TempData["Success"] as string;
            ErrorMessage = TempData["Error"] as string;
        }

        public IActionResult OnPost()
        {
            if (string.IsNullOrWhiteSpace(Input.Name))
            {
                ErrorMessage = "نام نقش را وارد کنید.";
                Roles = _roleApplication.RoleList();
                Accounts = _accountApplication.GetList(true);
                return Page();
            }

            var result = Input.Id > 0
                ? _roleApplication.Edit(Input)
                : _roleApplication.Create(Input);

            if (!result.Success)
            {
                ErrorMessage = result.Message;
                Roles = _roleApplication.RoleList();
                Accounts = _accountApplication.GetList(true);
                return Page();
            }

            TempData["Success"] = Input.Id > 0 ? "نقش ویرایش شد." : "نقش جدید ثبت شد.";
            return RedirectToPage("/Admin/Roles");
        }
    }
}
