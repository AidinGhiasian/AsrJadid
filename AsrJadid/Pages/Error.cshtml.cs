using Microsoft.AspNetCore.Mvc.RazorPages;

namespace AsrJadid.Pages
{
    public class ErrorModel : PageModel
    {
        public string? RequestId { get; set; }

        public int StatusCode { get; set; } = 500;

        public bool ShowRequestId => !string.IsNullOrEmpty(RequestId);

        public void OnGet(int? code)
        {
            StatusCode = code ?? 500;
            RequestId = HttpContext.TraceIdentifier;

            // در حالت توسعه، کد وضعیت واقعی پاسخ جایگزین می‌شود
            if (HttpContext.Response.StatusCode >= 400)
            {
                StatusCode = HttpContext.Response.StatusCode;
            }
        }
    }
}
