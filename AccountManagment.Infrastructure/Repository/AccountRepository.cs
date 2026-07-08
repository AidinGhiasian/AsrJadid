using AccountManagment.Domain.Domain.Account.Agg;
using Services.Application;

namespace AccountManagment.Infrastructure.Repository
{
    public class AccountRepository : RepositoryBase<Accounts>, IAccountRepository
    {
        private readonly AccountDbContext _dbContext;
        public AccountRepository(AccountDbContext dbContext) : base(dbContext)
        {
            _dbContext = dbContext;
        }

        public OperationResult ChangeRole(long id, long roleId)
        {
            OperationResult result = new OperationResult();
            var account = _dbContext.Accounts.FirstOrDefault(x => x.Id == id);
            if (account == null)
            {
                return result.Failed(ApplicationMessage.NotFund);
            }
            account.ChangeRole(roleId);
            _dbContext.SaveChanges();
            return result.IsSuccess();
        }

        public OperationResult Delete(long id)
        {
            OperationResult op = new OperationResult();
            var da = _dbContext.Accounts.FirstOrDefault(x => x.Id == id);
            if (da == null)
            {
                return op.Failed(ApplicationMessage.NotFund);
            }
            da.ChangeStatus(false);
            return op.IsSuccess();
        }

        public List<Accounts> GetAccounts(bool status)
        {
            return _dbContext.Accounts.Where(x => x.IsActive == status).ToList();
        }

        public Accounts GetById(long id)
        {
            return _dbContext.Accounts.FirstOrDefault(x => x.Id == id);
        }

        public Accounts GetByPhone(string phoneNumber)
        {
            return _dbContext.Accounts.FirstOrDefault(x => x.PhoneNumber == phoneNumber);
        }

        public OperationResult Restore(long id)
        {
            OperationResult op = new OperationResult();
            var ra = _dbContext.Accounts.FirstOrDefault(x => x.Id == id);
            if (ra == null)
            {
                return op.Failed(ApplicationMessage.NotFund);
            }
            ra.ChangeStatus(true);
            return op.IsSuccess();
        }

        public List<Accounts> Search(string search)
        {
            var query = _dbContext.Accounts.AsQueryable();

            if (!string.IsNullOrWhiteSpace(search))
            {
                query = query.Where(x =>
                    x.Name.Contains(search) ||
                    x.Family.Contains(search) ||
                    x.PhoneNumber.Contains(search));
            }

            return query.ToList();

        }
      
    }
}


 