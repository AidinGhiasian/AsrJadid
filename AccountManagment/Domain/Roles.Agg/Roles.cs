using AccountManagment.Domain.Domain.Account.Agg;
using Services.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AccountManagment.Domain.Domain.Roles.Agg
{
    public class Roles:EntityBase
    {
        public string Name { get; set; }
        public List<Accounts> Accounts { get; set; }

        public Roles(string name)
        {
            Name = name;
        }
        public void Edit(string name) 
        {
           name = Name;
        }

    }
}

