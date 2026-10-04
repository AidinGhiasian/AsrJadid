using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages
{
    public class IndexModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;
        private readonly IStoneCategoryApplication _categoryApplication;

        public IndexModel(IStoneApplication stoneApplication, IStoneCategoryApplication categoryApplication)
        {
            _stoneApplication = stoneApplication;
            _categoryApplication = categoryApplication;
        }

        public List<StoneCategoryViewModel> Categories { get; set; } = new();
        public List<StoneViewModel> Featured { get; set; } = new();
        public List<StoneViewModel> Newest { get; set; } = new();
        public List<StoneViewModel> Special { get; set; } = new();

        public void OnGet()
        {
            Categories = _categoryApplication.GetAll();

            var all = _stoneApplication.GetList();

            Featured = all.Where(x => x.Stock > 0).OrderByDescending(x => x.Price).Take(4).ToList();
            Newest = all.OrderByDescending(x => x.CreateDateTime).Take(4).ToList();
            Special = all.OrderBy(x => x.Price).Take(4).ToList();
        }
    }
}
