using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using StoneManagement.Application;
using StoneManagement.Application.Contracts.Picture;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Application.Contracts.StoneCategory;
using StoneManagement.Domain.PicturesAgg;
using StoneManagement.Domain.Stone.Agg;
using StoneManagement.Domain.StoneCategory.Agg;
using StoneManagement.Infrastructure.Repository;

namespace StoneManagement.Infrastructure.Configuration
{
    public class SMInfrastructureConfigurationBootStraper
    {
        public static void Configure(IServiceCollection services, string connectionString)
        {
            //Stone
            services.AddScoped<IStoneRepository, StoneRepository>();
            services.AddScoped<IStoneApplication, StoneApplication>();
            //StoneCategory
            services.AddScoped<IStoneCategoryRepository, StoneCategoryRepository>();
            services.AddScoped<IStoneCategoryApplication, StoneCategoryApplication>();
            //Picture
            services.AddScoped<IPictureRepository, PictureRepository>();
            services.AddScoped<IPictureApplication,PictureApplication>();

            services.AddDbContext<StoneDbContext>(options => options.UseSqlServer(connectionString));
        }
    }
}
