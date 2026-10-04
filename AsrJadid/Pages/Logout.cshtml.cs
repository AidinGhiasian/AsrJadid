using AccountManagment.Application.Contracts.AccountModels;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace AsrJadid.Pages
{
    public class LogoutModel : PageModel
    {
        private readonly IAccountApplication _accountApplication;

        public LogoutModel(IAccountApplication accountApplication)
        {
            _accountApplication = accountApplication;
        }

        public IActionResult OnGet()
        {
            _accountApplication.logout();
            return RedirectToPage("/Index");
        }
    }
}
