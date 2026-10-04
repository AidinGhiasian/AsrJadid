using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using AccountManagment.Application.Contracts.AccountModels;
using AccountManagment.Application.Contracts.RoleModels;

namespace AsrJadid.Pages.Admin
{
    public class AccountsModel : PageModel
    {
        private readonly IAccountApplication _accountApplication;
        private readonly IRoleApplication _roleApplication;

        public AccountsModel(IAccountApplication accountApplication, IRoleApplication roleApplication)
        {
            _accountApplication = accountApplication;
            _roleApplication = roleApplication;
        }

        public List<AccountViewModel> Accounts { get; set; } = new();
        public List<RoleViewModel> Roles { get; set; } = new();

        [BindProperty(SupportsGet = true)]
        public string? Query { get; set; }

        public string? SuccessMessage { get; set; }
        public string? ErrorMessage { get; set; }

        public void OnGet()
        {
            Roles = _roleApplication.RoleList();

            if (string.IsNullOrWhiteSpace(Query))
            {
                Accounts = _accountApplication.GetList(true);
            }
            else
            {
                var q = Query.Trim();
                Accounts = _accountApplication.GetList(true)
                    .Where(x => (x.Name + " " + x.Family).Contains(q) || x.PhoneNumber.Contains(q.ToEnglishNumber()))
                    .ToList();
            }

            SuccessMessage = TempData["Success"] as string;
            ErrorMessage = TempData["Error"] as string;
        }

        public IActionResult OnPostChangeRole(long id, long roleId)
        {
            var result = _accountApplication.ChangeRole(id, roleId);
            SetMessage(result.Success, result.Success ? "نقش کاربر تغییر کرد." : result.Message);
            return RedirectToPage("/Admin/Accounts");
        }

        public IActionResult OnPostDeactivate(long id)
        {
            var result = _accountApplication.Delete(id);
            SetMessage(result.Success, result.Success ? "حساب کاربر غیرفعال شد." : result.Message);
            return RedirectToPage("/Admin/Accounts");
        }

        public IActionResult OnPostRestore(long id)
        {
            var result = _accountApplication.Restore(id);
            SetMessage(result.Success, result.Success ? "حساب کاربر فعال شد." : result.Message);
            return RedirectToPage("/Admin/Accounts");
        }

        private void SetMessage(bool success, string message)
        {
            if (success)
                TempData["Success"] = message;
            else
                TempData["Error"] = message;
        }
    }
}
