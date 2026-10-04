using Microsoft.AspNetCore.Mvc.RazorPages;
using AccountManagment.Application.Contracts.AccountModels;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages.Admin
{
    public class SettingsModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;
        private readonly IStoneCategoryApplication _stoneCategoryApplication;
        private readonly IAccountApplication _accountApplication;

        public SettingsModel(IStoneApplication stoneApplication, IStoneCategoryApplication stoneCategoryApplication, IAccountApplication accountApplication)
        {
            _stoneApplication = stoneApplication;
            _stoneCategoryApplication = stoneCategoryApplication;
            _accountApplication = accountApplication;
        }

        public int StoneCount { get; set; }
        public int CategoryCount { get; set; }
        public int AccountCount { get; set; }

        public void OnGet()
        {
            StoneCount = _stoneApplication.GetList().Count;
            CategoryCount = _stoneCategoryApplication.GetAll().Count;
            AccountCount = _accountApplication.GetList(true).Count;
        }
    }
}
