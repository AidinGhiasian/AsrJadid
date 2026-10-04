using Microsoft.AspNetCore.Mvc.RazorPages;

namespace AsrJadid.Pages
{
    public class OrderModel : PageModel
    {
        public string? Code { get; set; }

        public void OnGet(string? code)
        {
            Code = code;
        }
    }
}
