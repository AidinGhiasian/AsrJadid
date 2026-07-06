using AccountManagment.Domain.Domain.Roles.Agg;
using Services.Application;

namespace AccountManagment.Infrastructure.EFCore.Repository
{
    public class RoleRepository : RepositoryBase<Roles>, IRoleRepository
    {
        private readonly AccountDbContext _dbContext;
        public RoleRepository(AccountDbContext dbContext) : base(dbContext)
        {
            _dbContext = dbContext;
        }
        public Roles GetById(long id)
        {
            return _dbContext.Roles.FirstOrDefault(x => x.Id == id);
        }

        public List<Roles> GetRoles()
        {
            return _dbContext.Roles.ToList();
        }
    }
}
