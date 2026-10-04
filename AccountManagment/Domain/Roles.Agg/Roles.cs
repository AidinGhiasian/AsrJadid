using AccountManagment.Domain.Domain.Account.Agg;
using Services.Models;

namespace AccountManagment.Domain.Domain.Roles.Agg
{
    public class Roles:EntityBase
    {
        public string Name { get; set; }
        public List<Accounts> Accounts { get; set; } = new();

        public Roles(string name)
        {
            Name = name;
        }

        public void Edit(string name)
        {
            Name = name;
        }
    }
}
