using AccountManagment.Application.Contracts.AccountModels;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace AsrJadid.Pages
{
    public class RegisterModel : PageModel
    {
        private readonly IAccountApplication _accountApplication;

        public RegisterModel(IAccountApplication accountApplication)
        {
            _accountApplication = accountApplication;
        }

        [BindProperty]
        public RegisterInput Input { get; set; } = new();

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

            if (Input.Password != Input.RePassword)
            {
                ErrorMessage = "رمز عبور و تکرار آن یکسان نیستند.";
                return Page();
            }

            var result = _accountApplication.Create(new CreateViewModel
            {
                Name = Input.Name,
                Family = Input.Family,
                PhoneNumber = Input.PhoneNumber,
                Email = Input.Email,
                Password = Input.Password
            });

            if (!result.Success)
            {
                ErrorMessage = result.Message;
                return Page();
            }

            // ورود خودکار پس از ثبت‌نام
            var login = _accountApplication.login(new LoginViewModel
            {
                PhoneNumber = Input.PhoneNumber,
                Password = Input.Password
            });

            if (login.Success)
            {
                return RedirectToPage("/Dashboard");
            }

            return RedirectToPage("/Login");
        }

        public class RegisterInput
        {
            public string Name { get; set; } = string.Empty;
            public string Family { get; set; } = string.Empty;
            public string PhoneNumber { get; set; } = string.Empty;
            public string? Email { get; set; }
            public string Password { get; set; } = string.Empty;
            public string RePassword { get; set; } = string.Empty;
            public bool AcceptTerms { get; set; }
        }
    }
}
