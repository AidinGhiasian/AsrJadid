using Services.Application;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AccountManagment.Domain.Domain.Account.Agg
{
    public interface IAccountRepository:IRepositoryBase<Accounts>
    {
        public List<Accounts> GetAccounts(bool status);
        public Accounts GetById(long id);
        public OperationResult Delete(long id);
        public OperationResult Restore(long id);
        public OperationResult ChangeRole(long id,long roleId);
        public List<Accounts> Search(string account);
        public Accounts GetByPhone(string phoneNumber);
    }
}