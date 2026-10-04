using AccountManagment.Application.Contracts.AccountModels;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Services.Application;
using Services.Models;

namespace AsrJadid.Pages
{
    public class LoginModel : PageModel
    {
        private readonly IAccountApplication _accountApplication;

        public LoginModel(IAccountApplication accountApplication)
        {
            _accountApplication = accountApplication;
        }

        [BindProperty]
        public LoginInput Input { get; set; } = new();

        [BindProperty(SupportsGet = true)]
        public string? ReturnUrl { get; set; }

        public string? ErrorMessage { get; set; }

        public void OnGet()
        {
        }

        public IActionResult OnPost()
        {
            if (!ModelState.IsValid)
            {
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

            if (!string.IsNullOrWhiteSpace(ReturnUrl) && Url.IsLocalUrl(ReturnUrl))
            {
                return Redirect(ReturnUrl);
            }

            // مدیر به پنل مدیریت و کاربر عادی به پنل کاربری هدایت می‌شود
            var phone = Input.PhoneNumber.ToEnglishNumber().Trim();
            var account = _accountApplication.GetList(true).FirstOrDefault(x => x.PhoneNumber == phone);

            if (account != null && account.RoleId.ToString() == RolesCode.Admin)
            {
                return RedirectToPage("/Admin/Index");
            }

            return RedirectToPage("/Dashboard");
        }

        public class LoginInput
        {
            public string PhoneNumber { get; set; } = string.Empty;
            public string Password { get; set; } = string.Empty;
            public bool RememberMe { get; set; }
        }
    }
}
