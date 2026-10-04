using AccountManagment.Application;
using AccountManagment.Application.Contracts.AccountModels;
using AccountManagment.Application.Contracts.RoleModels;
using AccountManagment.Domain.Domain.Account.Agg;
using AccountManagment.Domain.Domain.Roles.Agg;
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

            // سرویس‌های لایه Application
            services.AddScoped<IAccountApplication, AccountApplication>();
            services.AddScoped<IRoleApplication, RoleApplication>();


            services.AddDbContext<AccountDbContext>(options => options.UseSqlServer(connectionString));
        }
    }
}
