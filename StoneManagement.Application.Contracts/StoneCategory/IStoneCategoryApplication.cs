using Services.Application;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StoneManagement.Application.Contracts.StoneCategory
{
    public interface IStoneCategoryApplication
    {
        public OperationResult Create(CreateViewModel command);
        public OperationResult Edit(EditViewModel command);
        public OperationResult Delete(long id);
        public List<StoneCategoryViewModel> GetAll();
    }
}
