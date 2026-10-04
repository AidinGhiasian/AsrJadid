using AccountManagment.Application.Contracts.AccountModels;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Services.Application;
using Services.Models;
using StoneManagement.Application.Contracts.Stone;

namespace AsrJadid.Pages
{
    public class CheckoutModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;
        private readonly IAuthHelper _authHelper;
        private readonly IAccountApplication _accountApplication;

        private const decimal TaxRate = 0.09m;
        private const decimal ShippingCost = 1850000m;
        private const decimal FreeShippingLimit = 50000000m;

        public CheckoutModel(IStoneApplication stoneApplication, IAuthHelper authHelper, IAccountApplication accountApplication)
        {
            _stoneApplication = stoneApplication;
            _authHelper = authHelper;
            _accountApplication = accountApplication;
        }

        [BindProperty]
        public CheckoutInput Input { get; set; } = new();

        public string? ErrorMessage { get; set; }

        public void OnGet()
        {
            if (!_authHelper.IsAuthenticated())
                return;

            var account = _accountApplication.GetById(_authHelper.CurrentAccountId());
            if (account == null)
                return;

            Input.Name = account.Name;
            Input.Family = account.Family;
            Input.PhoneNumber = account.PhoneNumber;
            Input.Email = account.Email;
            Input.Address = account.Address;
            Input.Receiver = (account.Name + " " + account.Family).Trim();
        }

        public IActionResult OnPost()
        {
            if (!Input.AcceptTerms)
            {
                ErrorMessage = "برای ثبت سفارش باید قوانین و مقررات فروش را بپذیرید.";
                return Page();
            }

            if (string.IsNullOrWhiteSpace(Input.Name) || string.IsNullOrWhiteSpace(Input.Family) ||
                string.IsNullOrWhiteSpace(Input.PhoneNumber) || string.IsNullOrWhiteSpace(Input.City) ||
                string.IsNullOrWhiteSpace(Input.Address))
            {
                ErrorMessage = "تکمیل نام، نام خانوادگی، شماره همراه، شهر و نشانی الزامی است.";
                return Page();
            }

            // اعتبارسنجی سبد خرید در سمت سرور و محاسبه مجدد مبلغ بر اساس قیمت‌های پایگاه داده
            var items = ParseItems(Input.ItemsJson);
            if (items.Count == 0)
            {
                ErrorMessage = "سبد خرید شما خالی است یا اطلاعات آن قابل خواندن نیست. لطفاً دوباره تلاش کنید.";
                return Page();
            }

            var all = _stoneApplication.GetList();
            var subtotal = 0m;

            foreach (var item in items)
            {
                var stone = all.FirstOrDefault(x => x.Id == item.Key);
                if (stone == null)
                    continue;

                subtotal += stone.Price * item.Value;
            }

            if (subtotal <= 0)
            {
                ErrorMessage = "محصولات سبد خرید در پایگاه داده یافت نشدند. لطفاً سبد خرید را بازبینی کنید.";
                return Page();
            }

            var tax = Math.Round(subtotal * TaxRate);
            var shipping = subtotal >= FreeShippingLimit ? 0m : ShippingCost;
            var total = subtotal + tax + shipping;

            var code = string.IsNullOrWhiteSpace(Input.TrackingCode)
                ? "ASR-" + DateTime.Now.ToString("yyMMdd-HHmmss")
                : Input.TrackingCode.Trim();

            TempData["OrderCode"] = code;
            TempData["OrderTotal"] = total.ToMoney();
            TempData["OrderMessage"] = "سفارش شما با کد " + code + " ثبت شد. کارشناسان فروش برای تأیید نهایی با شما تماس می‌گیرند.";

            return RedirectToPage("/Order", new { code = code });
        }

        private static List<KeyValuePair<long, int>> ParseItems(string? json)
        {
            var result = new List<KeyValuePair<long, int>>();

            if (string.IsNullOrWhiteSpace(json))
                return result;

            try
            {
                using var document = System.Text.Json.JsonDocument.Parse(json);

                if (document.RootElement.ValueKind != System.Text.Json.JsonValueKind.Array)
                    return result;

                foreach (var element in document.RootElement.EnumerateArray())
                {
                    if (!element.TryGetProperty("id", out var idProp))
                        continue;

                    long id = 0;
                    if (idProp.ValueKind == System.Text.Json.JsonValueKind.Number)
                        id = idProp.GetInt64();
                    else if (!long.TryParse(idProp.ToString().ToEnglishNumber(), out id))
                        continue;

                    var qty = 1;
                    if (element.TryGetProperty("qty", out var qtyProp))
                    {
                        if (qtyProp.ValueKind == System.Text.Json.JsonValueKind.Number)
                            qty = qtyProp.GetInt32();
                        else
                            int.TryParse(qtyProp.ToString().ToEnglishNumber(), out qty);
                    }

                    if (id <= 0)
                        continue;

                    result.Add(new KeyValuePair<long, int>(id, qty < 1 ? 1 : qty));
                }
            }
            catch (System.Text.Json.JsonException)
            {
                return new List<KeyValuePair<long, int>>();
            }

            return result;
        }

        public class CheckoutInput
        {
            public string Name { get; set; } = string.Empty;
            public string Family { get; set; } = string.Empty;
            public string PhoneNumber { get; set; } = string.Empty;
            public string? Email { get; set; }
            public string Province { get; set; } = "تهران";
            public string City { get; set; } = string.Empty;
            public string Address { get; set; } = string.Empty;
            public string? PostalCode { get; set; }
            public string? Receiver { get; set; }
            public string? Description { get; set; }
            public string ShippingMethod { get; set; } = "باربری";
            public string PaymentMethod { get; set; } = "آنلاین";
            public bool AcceptTerms { get; set; }
            public string? TrackingCode { get; set; }
            public string? ItemsJson { get; set; }
        }
    }
}
