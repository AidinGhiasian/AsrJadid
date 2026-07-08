using Services.Application;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StoneManagement.Domain.Stone.Agg
{
    public interface IStoneRepository:IRepositoryBase<Stones>
    {
        public OperationResult Delete(long id);
        public List<Stones> Search(string search);
    }
}
