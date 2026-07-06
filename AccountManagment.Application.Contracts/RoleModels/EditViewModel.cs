using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AccountManagment.Application.Contracts.RoleModels
{
    public class EditViewModel:CreateViewModel
    {
        public long Id { get; set; }
        public  DateTime CreateDateTime { get; set; }
    }
}
