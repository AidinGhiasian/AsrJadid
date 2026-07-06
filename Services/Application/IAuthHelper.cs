using Services.Models;

namespace Services.Application
{
    public interface IAuthHelper
    {
        public bool IsAuthenticated();
        public void SignOut();
        public void SignIn(AuthViewModel account);
        public AuthViewModel CurrentAccountInfo();
        public string CurrentAccountRole();
        public string? CurrentAccountMobile();
        public long CurrentAccountId();


    }
}
