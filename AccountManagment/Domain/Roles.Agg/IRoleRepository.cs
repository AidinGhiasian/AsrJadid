using Services.Application;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AccountManagment.Domain.Domain.Roles.Agg
{
    public interface IRoleRepository:IRepositoryBase<Roles>
    {
        public Roles GetById(long id);

    }
}
