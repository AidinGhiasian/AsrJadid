using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages
{
    public class PriceListModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;
        private readonly IStoneCategoryApplication _stoneCategoryApplication;

        public PriceListModel(IStoneApplication stoneApplication, IStoneCategoryApplication stoneCategoryApplication)
        {
            _stoneApplication = stoneApplication;
            _stoneCategoryApplication = stoneCategoryApplication;
        }

        public List<StoneViewModel> Stones { get; set; } = new();
        public List<StoneCategoryViewModel> Categories { get; set; } = new();

        public void OnGet()
        {
            Stones = _stoneApplication.GetList();
            Categories = _stoneCategoryApplication.GetAll();
        }
    }
}
