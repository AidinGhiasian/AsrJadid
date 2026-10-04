using AccountManagment.Application.Contracts.AccountModels;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Services.Application;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages.Admin
{
    public class IndexModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;
        private readonly IStoneCategoryApplication _stoneCategoryApplication;
        private readonly IAccountApplication _accountApplication;

        public IndexModel(IStoneApplication stoneApplication, IStoneCategoryApplication stoneCategoryApplication, IAccountApplication accountApplication)
        {
            _stoneApplication = stoneApplication;
            _stoneCategoryApplication = stoneCategoryApplication;
            _accountApplication = accountApplication;
        }

        public List<StoneViewModel> Stones { get; set; } = new();
        public List<StoneCategoryViewModel> Categories { get; set; } = new();
        public List<AccountViewModel> Accounts { get; set; } = new();
        public List<StoneViewModel> Latest { get; set; } = new();
        public decimal InventoryValue { get; set; }

        public void OnGet()
        {
            Stones = _stoneApplication.GetList();
            Categories = _stoneCategoryApplication.GetAll();
            Accounts = _accountApplication.GetList(true);
            Latest = Stones.TakeLast(6).Reverse().ToList();
            InventoryValue = Stones.Sum(x => x.Price * x.Stock);
        }
    }
}
