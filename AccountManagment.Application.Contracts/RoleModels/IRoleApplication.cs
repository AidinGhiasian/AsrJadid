using Services.Application;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AccountManagment.Application.Contracts.RoleModels
{
    public interface IRoleApplication
    {
        public List<RoleViewModel> RoleList();
        public EditViewModel GetDetails(long Id);
        public OperationResult Create(CreateViewModel command);
        public OperationResult Edit(EditViewModel command);
    }
}
