using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using StoneManagement.Domain.Stone.Agg;
using StoneManagement.Domain.StoneCategory.Agg;
using StoneManagement.Infrastructure.EFCore.Repository;
using StoneManagement.Infrastructure.Repository;

namespace StoneManagement.Infrastructure.Configuration
{
    public class SMInfrastructureConfigurationBootStraper
    {
        public static void Configure(IServiceCollection services, string connectionString)
        {
            services.AddScoped<IStoneRepository, StoneRepository>();
            services.AddScoped<IStoneCategoryRepository, StoneCategoryRepository>();


            services.AddDbContext<StoneDbContext>(options => options.UseSqlServer(connectionString));
        }
    }
}
