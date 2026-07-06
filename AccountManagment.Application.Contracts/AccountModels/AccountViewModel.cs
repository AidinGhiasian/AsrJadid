using Microsoft.AspNetCore.Http;

namespace AccountManagment.Application.Contracts.AccountModels
{
    public class AccountViewModel
    {
        public long Id { get; set; }
        public string? Picture { get; set; }
        public IFormFile PictureFile { get; set; }
        public string Name { get; set; }
        public string Family { get; set; }
        public string PhoneNumber { get; set; }
        public string? Email { get; set; }
        public string Address { get; set; }
        public bool IsActive { get; set; }
        public long RoleId { get; set; }
        public string Role { get; set; }
        public DateTime CreateDateTime { get; set; }

    }
}
