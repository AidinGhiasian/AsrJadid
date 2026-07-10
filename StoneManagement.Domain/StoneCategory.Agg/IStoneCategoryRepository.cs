using Services.Application;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StoneManagement.Domain.StoneCategory.Agg
{
    public interface IStoneCategoryRepository:IRepositoryBase<StoneCategory>
    {
        public OperationResult Delete(long id);
    }
}
