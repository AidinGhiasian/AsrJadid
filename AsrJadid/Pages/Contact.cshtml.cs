using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using AccountManagment.Application.Contracts.AccountModels;
using Services.Application;

namespace AsrJadid.Pages
{
    public class ContactModel : PageModel
    {
        private readonly IAuthHelper _authHelper;
        private readonly IAccountApplication _accountApplication;
        private readonly ILogger<ContactModel> _logger;

        public ContactModel(IAuthHelper authHelper, IAccountApplication accountApplication, ILogger<ContactModel> logger)
        {
            _authHelper = authHelper;
            _accountApplication = accountApplication;
            _logger = logger;
        }

        [BindProperty]
        public ContactInput Input { get; set; } = new();

        public string? SuccessMessage { get; set; }

        public void OnGet()
        {
            if (!_authHelper.IsAuthenticated())
                return;

            var account = _accountApplication.GetById(_authHelper.CurrentAccountId());
            if (account == null)
                return;

            Input.FullName = (account.Name + " " + account.Family).Trim();
            Input.PhoneNumber = account.PhoneNumber;
            Input.Email = account.Email;
        }

        public IActionResult OnPost()
        {
            if (string.IsNullOrWhiteSpace(Input.FullName) ||
                string.IsNullOrWhiteSpace(Input.PhoneNumber) ||
                string.IsNullOrWhiteSpace(Input.Message))
            {
                ModelState.AddModelError(string.Empty, "تکمیل نام، شماره همراه و توضیحات الزامی است.");
                return Page();
            }

            if (!Input.AcceptContact)
            {
                ModelState.AddModelError(string.Empty, "برای ارسال درخواست باید با تماس کارشناسان موافقت کنید.");
                return Page();
            }

            // ماژول پیام‌های تماس در پروژه جدول اختصاصی ندارد؛ درخواست در گزارش سرور ثبت می‌شود.
            TempData["ContactSuccess"] = "درخواست شما با موفقیت ثبت شد. کارشناسان عصرجدید در اولین فرصت با شما تماس می‌گیرند.";
            return RedirectToPage("/Contact");
        }

        // ثبت ایمیل خبرنامه (بدون جدول اختصاصی؛ اعتبارسنجی و ثبت در گزارش سرور)
        public IActionResult OnPostNewsletter(string? email)
        {
            var isAjax = Request.Headers["X-Requested-With"].ToString()
                .Equals("XMLHttpRequest", StringComparison.OrdinalIgnoreCase);
            var value = (email ?? string.Empty).Trim();

            var at = value.IndexOf('@');
            var valid = value.Length >= 6
                        && at > 0
                        && at == value.LastIndexOf('@')
                        && value.IndexOf('.', at) > at + 1
                        && value.LastIndexOf('.') < value.Length - 1
                        && !value.Contains(' ')
                        && !value.Contains('=')
                        && !value.Contains('<');

            if (!valid)
            {
                var bad = "ایمیل وارد‌شده معتبر نیست. نمونه درست: name@example.com";
                if (isAjax) return new JsonResult(new { ok = false, message = bad });
                TempData["ContactSuccess"] = bad;
                return RedirectToPage("/Contact");
            }

            _logger.LogInformation("ثبت ایمیل خبرنامه: {Email}", value);
            var ok = "ایمیل شما در خبرنامه عصرجدید ثبت شد. تخفیف‌ها و طرح‌های تازه را اول از همه دریافت می‌کنید.";
            if (isAjax) return new JsonResult(new { ok = true, message = ok });
            TempData["ContactSuccess"] = ok;
            return RedirectToPage("/Contact");
        }

        public class ContactInput
        {
            public string FullName { get; set; } = string.Empty;
            public string PhoneNumber { get; set; } = string.Empty;
            public string? Email { get; set; }
            public string Subject { get; set; } = "استعلام قیمت محصول";
            public string ProjectType { get; set; } = "مسکونی";
            public string? Area { get; set; }
            public string Message { get; set; } = string.Empty;
            public bool AcceptContact { get; set; }
        }
    }
}
