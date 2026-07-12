using Microsoft.EntityFrameworkCore;
using StoneManagement.Domain.PicturesAgg;
using StoneManagement.Domain.Stone.Agg;
using StoneManagement.Domain.StoneCategory.Agg;

namespace StoneManagement.Infrastructure
{
    public class StoneDbContext:DbContext
    {
        public DbSet<Stones> Stones { get; set; }
        public DbSet<StoneCategory> Categories { get; set; }
        public DbSet<Pictures> Pictures { get; set; }
        public StoneDbContext(DbContextOptions<StoneDbContext>options):base(options)
        {
        }
    }
}
