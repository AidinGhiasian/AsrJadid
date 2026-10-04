using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Http;
using Newtonsoft.Json;
using Services.Models;
using System.Security.Claims;

namespace Services.Application.AuthHelper
{
    public class AuthHelper : IAuthHelper
    {
        private readonly IHttpContextAccessor _contextAccessor;

        public AuthHelper(IHttpContextAccessor contextAccessor)
        {
            _contextAccessor = contextAccessor;
        }

        private ClaimsPrincipal? User => _contextAccessor.HttpContext?.User;

        public AuthViewModel CurrentAccountInfo()
        {
            var result = new AuthViewModel();
            if (!IsAuthenticated())
                return result;

            var claims = User!.Claims.ToList();

            result.Id = long.TryParse(claims.FirstOrDefault(x => x.Type == "AccountId")?.Value, out var id) ? id : 0;
            result.RoleId = long.TryParse(claims.FirstOrDefault(x => x.Type == ClaimTypes.Role)?.Value, out var roleId) ? roleId : 0;
            result.PhoneNumber = claims.FirstOrDefault(x => x.Type == "PhoneNumber")?.Value ?? string.Empty;
            result.Name = claims.FirstOrDefault(x => x.Type == ClaimTypes.Name)?.Value ?? string.Empty;
            result.Family = claims.FirstOrDefault(x => x.Type == "Family")?.Value ?? string.Empty;
            result.Picture = claims.FirstOrDefault(x => x.Type == "ProfilePicture")?.Value ?? string.Empty;
            return result;
        }

        public List<int> GetPermissions()
        {
            if (!IsAuthenticated())
                return new List<int>();

            var permissions = User!.Claims.FirstOrDefault(x => x.Type == "permissions")?.Value;
            if (string.IsNullOrWhiteSpace(permissions))
                return new List<int>();

            return JsonConvert.DeserializeObject<List<int>>(permissions) ?? new List<int>();
        }

        public long CurrentAccountId()
        {
            if (!IsAuthenticated())
                return 0;

            return long.TryParse(User!.Claims.FirstOrDefault(x => x.Type == "AccountId")?.Value, out var id) ? id : 0;
        }

        public string? CurrentAccountMobile()
        {
            if (!IsAuthenticated())
                return string.Empty;

            return User!.Claims.FirstOrDefault(x => x.Type == "PhoneNumber")?.Value ?? string.Empty;
        }

        public string? CurrentAccountRole()
        {
            if (!IsAuthenticated())
                return null;

            return User!.Claims.FirstOrDefault(x => x.Type == ClaimTypes.Role)?.Value;
        }

        public bool IsAuthenticated()
        {
            return User?.Identity?.IsAuthenticated == true;
        }

        public void SignIn(AuthViewModel account)
        {
            var claims = new List<Claim>
            {
                new Claim("AccountId", account.Id.ToString()),
                new Claim(ClaimTypes.NameIdentifier, account.Id.ToString()),
                new Claim(ClaimTypes.Name, account.Name ?? string.Empty),
                new Claim(ClaimTypes.Role, account.RoleId.ToString()),
                new Claim("Family", account.Family ?? string.Empty),
                new Claim("PhoneNumber", account.PhoneNumber ?? string.Empty),
                new Claim("ProfilePicture", account.Picture ?? string.Empty),
            };

            var claimsIdentity = new ClaimsIdentity(claims, CookieAuthenticationDefaults.AuthenticationScheme);

            var authProperties = new AuthenticationProperties
            {
                IsPersistent = true,
                ExpiresUtc = DateTimeOffset.UtcNow.AddDays(30)
            };

            // این متد در لایه Application (بدون async) صدا زده می‌شود؛
            // بنابراین تا کامل شدن عملیات احراز هویت منتظر می‌مانیم.
            _contextAccessor.HttpContext!
                .SignInAsync(CookieAuthenticationDefaults.AuthenticationScheme,
                    new ClaimsPrincipal(claimsIdentity),
                    authProperties)
                .GetAwaiter().GetResult();
        }

        public void SignOut()
        {
            _contextAccessor.HttpContext!
                .SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme)
                .GetAwaiter().GetResult();
        }
    }
}
