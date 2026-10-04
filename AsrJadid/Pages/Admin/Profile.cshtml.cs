using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using AccountManagment.Application.Contracts.AccountModels;
using Services.Application;

namespace AsrJadid.Pages.Admin
{
    public class ProfileModel : PageModel
    {
        private readonly IAccountApplication _accountApplication;
        private readonly IAuthHelper _authHelper;

        public ProfileModel(IAccountApplication accountApplication, IAuthHelper authHelper)
        {
            _accountApplication = accountApplication;
            _authHelper = authHelper;
        }

        [BindProperty]
        public EditViewModel Input { get; set; } = new();

        [BindProperty]
        public PasswordInputModel PasswordInput { get; set; } = new();

        public string? SuccessMessage { get; set; }
        public string? ErrorMessage { get; set; }

        public void OnGet()
        {
            Load();
        }

        public IActionResult OnPost()
        {
            var details = _accountApplication.GetDetails(_authHelper.CurrentAccountId());
            if (details == null)
            {
                return RedirectToPage("/Admin/Login");
            }

            Input.Id = details.Id;
            Input.Picture = details.Picture;
            Input.BirthDate = details.BirthDate;

            var result = _accountApplication.Edit(Input);

            if (!result.Success)
            {
                ErrorMessage = result.Message;
                Load();
                return Page();
            }

            SuccessMessage = "اطلاعات مدیر ذخیره شد.";
            Load();
            return Page();
        }

        public IActionResult OnPostPassword()
        {
            if (string.IsNullOrWhiteSpace(PasswordInput.Password) || PasswordInput.Password != PasswordInput.RePassword)
            {
                ErrorMessage = "رمز عبور و تکرار آن باید یکسان و غیرخالی باشند.";
                Load();
                return Page();
            }

            var result = _accountApplication.ChangePassword(new AccountManagment.Application.Contracts.AccountModels.ChangePassword
            {
                Id = _authHelper.CurrentAccountId(),
                Password = PasswordInput.Password,
                RePassword = PasswordInput.RePassword
            });

            if (!result.Success)
            {
                ErrorMessage = result.Message;
                Load();
                return Page();
            }

            SuccessMessage = "رمز عبور مدیر تغییر کرد.";
            Load();
            return Page();
        }

        private void Load()
        {
            var details = _accountApplication.GetDetails(_authHelper.CurrentAccountId());
            if (details == null)
                return;

            Input.Name = details.Name;
            Input.Family = details.Family;
            Input.PhoneNumber = details.PhoneNumber;
            Input.Email = details.Email;
            Input.Address = details.Address;
            Input.Picture = details.Picture;
            Input.BirthDate = details.BirthDate;
        }

        public class PasswordInputModel
        {
            public string Password { get; set; } = string.Empty;
            public string RePassword { get; set; } = string.Empty;
        }
    }
}
