using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.Stone;

namespace AsrJadid.Pages
{
    public class SearchModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;

        public SearchModel(IStoneApplication stoneApplication)
        {
            _stoneApplication = stoneApplication;
        }

        public List<StoneViewModel> Results { get; set; } = new();
        public string? Query { get; set; }

        public void OnGet(string? q = null)
        {
            Query = q;

            if (string.IsNullOrWhiteSpace(q))
            {
                Results = _stoneApplication.GetList();
                return;
            }

            Results = _stoneApplication.Search(q.Trim()).Select(Map).ToList();
        }

        private static StoneViewModel Map(SearchViewModel search)
        {
            return new StoneViewModel
            {
                Id = search.Id,
                Picture = search.Picture,
                StoneName = search.StoneName,
                Length = search.Length,
                Width = search.Width,
                Weight = search.Weight,
                Price = search.Price,
                Stock = search.Stock,
                Color = search.Color,
                Description = search.Description,
                CategoryId = search.CategoryId
            };
        }
    }
}
