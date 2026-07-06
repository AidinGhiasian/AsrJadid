namespace Services.Models
{
    public class AuthViewModel
    {


        public long Id { get; set; }
        public string Name { get; set; }
        public string Family { get; set; }
        public long RoleId { get; set; }
        public string PhoneNumber { get; set; }
        public string Picture { get; set; }
        public AuthViewModel(){}
        public AuthViewModel(long id, string name, long roleId, string phoneNumber, string picture,string family)
        {
            Id = id;
            Name = name;
            Family = family;
            RoleId = roleId;
            PhoneNumber = phoneNumber;
            Picture = picture;
        }


    }
}
