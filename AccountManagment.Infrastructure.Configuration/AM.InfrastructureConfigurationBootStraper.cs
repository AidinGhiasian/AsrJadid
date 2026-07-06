using AccountManagment.Domain.Domain.Account.Agg;
using AccountManagment.Domain.Domain.Roles.Agg;
using AccountManagment.Infrastructure.EFCore.Repository;
using AccountManagment.Infrastructure.Repository;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;


namespace AccountManagment.Infrastructure.Configuration
{
    public class AMInfrastructureConfigurationBootStraper
    {
        public static void Configure(IServiceCollection services, string connectionString)
        {


            services.AddScoped<IAccountRepository, AccountRepository>();
            services.AddScoped<IRoleRepository, RoleRepository>();


            services.AddDbContext<AccountDbContext>(options => options.UseSqlServer(connectionString));
        }
    }
}
