using AccountManagment.Application.Contracts.AccountModels;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Services.Application;
using StoneManagement.Application.Contracts.Stone;

namespace AsrJadid.Pages
{
    public class DashboardModel : PageModel
    {
        private readonly IAuthHelper _authHelper;
        private readonly IAccountApplication _accountApplication;
        private readonly IStoneApplication _stoneApplication;

        public DashboardModel(IAuthHelper authHelper, IAccountApplication accountApplication, IStoneApplication stoneApplication)
        {
            _authHelper = authHelper;
            _accountApplication = accountApplication;
            _stoneApplication = stoneApplication;
        }

        public AccountViewModel? Account { get; set; }

        public List<StoneViewModel> Suggested { get; set; } = new();

        public string DisplayName
        {
            get
            {
                if (Account == null)
                    return "کاربر عصرجدید";

                var name = (Account.Name + " " + Account.Family).Trim();
                return string.IsNullOrWhiteSpace(name) ? "کاربر عصرجدید" : name;
            }
        }

        public void OnGet()
        {
            Account = _accountApplication.GetById(_authHelper.CurrentAccountId());

            if (Account == null)
                return;

            // پیشنهاد بر اساس دسته‌بندی آخرین علاقه‌مندی‌ها امکان‌پذیر است؛ در نبود آن، جدیدترین محصولات نمایش داده می‌شود.
            Suggested = _stoneApplication.GetList().TakeLast(3).ToList();
        }
    }
}
