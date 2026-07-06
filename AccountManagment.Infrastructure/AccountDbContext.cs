
using AccountManagment.Domain.Domain.Account.Agg;
using AccountManagment.Domain.Domain.Roles.Agg;
using Microsoft.EntityFrameworkCore;

namespace AccountManagment.Infrastructure
{
    public  class AccountDbContext:DbContext
    {
        public DbSet<Accounts> Accounts { get; set; }
        public DbSet<Roles> Roles { get; set; }
        public AccountDbContext(DbContextOptions<AccountDbContext> options):base(options)
        {
        }
    }
}
