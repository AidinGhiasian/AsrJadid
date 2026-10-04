using Microsoft.AspNetCore.Mvc.RazorPages;
using StoneManagement.Application.Contracts.Stone;

namespace AsrJadid.Pages
{
    public class CartModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;

        public CartModel(IStoneApplication stoneApplication)
        {
            _stoneApplication = stoneApplication;
        }

        /// <summary>محصولات پیشنهادی برای تکمیل سفارش (سمت سرور، برای موتورهای جستجو و بارگذاری اولیه).</summary>
        public List<StoneViewModel> Suggested { get; set; } = new();

        public void OnGet()
        {
            Suggested = _stoneApplication.GetList().Take(3).ToList();
        }
    }
}
