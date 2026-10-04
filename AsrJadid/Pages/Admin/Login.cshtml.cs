using AccountManagment.Application.Contracts.AccountModels;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Services.Application;
using Services.Models;

namespace AsrJadid.Pages.Admin
{
    public class LoginModel : PageModel
    {
        private readonly IAccountApplication _accountApplication;
        private readonly IAuthHelper _authHelper;

        public LoginModel(IAccountApplication accountApplication, IAuthHelper authHelper)
        {
            _accountApplication = accountApplication;
            _authHelper = authHelper;
        }

        [BindProperty]
        public AdminLoginInput Input { get; set; } = new();

        public string? ErrorMessage { get; set; }

        public IActionResult OnGet()
        {
            if (_authHelper.IsAuthenticated() && _authHelper.CurrentAccountRole() == RolesCode.Admin)
            {
                return RedirectToPage("/Admin/Index");
            }

            return Page();
        }

        public IActionResult OnPost()
        {
            if (string.IsNullOrWhiteSpace(Input.PhoneNumber) || string.IsNullOrWhiteSpace(Input.Password))
            {
                ErrorMessage = "شماره همراه و رمز عبور را وارد کنید.";
                return Page();
            }

            var result = _accountApplication.login(new LoginViewModel
            {
                PhoneNumber = Input.PhoneNumber,
                Password = Input.Password
            });

            if (!result.Success)
            {
                ErrorMessage = result.Message;
                return Page();
            }

            // فقط کاربران با نقش مدیر اجازه ورود به پنل دارند
            if (_authHelper.CurrentAccountRole() != RolesCode.Admin)
            {
                _accountApplication.logout();
                ErrorMessage = "این حساب کاربری دسترسی مدیریتی ندارد.";
                return Page();
            }

            return RedirectToPage("/Admin/Index");
        }

        public class AdminLoginInput
        {
            public string PhoneNumber { get; set; } = string.Empty;
            public string Password { get; set; } = string.Empty;
            public bool RememberMe { get; set; }
        }
    }
}
