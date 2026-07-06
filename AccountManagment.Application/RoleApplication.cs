using AccountManagment.Application.Contracts.RoleModels;
using Services.Application;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AccountManagment.Application
{
    public class RoleApplication : IRoleApplication
    {
        public OperationResult Create(CreateViewModel command)
        {
            throw new NotImplementedException();
        }

        public OperationResult Edit(EditViewModel command)
        {
            throw new NotImplementedException();
        }

        public EditViewModel GetDetails(long Id)
        {
            throw new NotImplementedException();
        }

        public List<RoleViewModel> RoleList()
        {
            throw new NotImplementedException();
        }
    }
}
