using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace AsrJadid.Pages
{
    public class ForgotPasswordModel : PageModel
    {
        [BindProperty]
        public string PhoneNumber { get; set; } = string.Empty;

        public bool Submitted { get; set; }

        public void OnGet()
        {
        }

        public void OnPost()
        {
            Submitted = true;
        }
    }
}
