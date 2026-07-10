using Microsoft.EntityFrameworkCore;
using StoneManagement.Domain.Stone.Agg;
using StoneManagement.Domain.StoneCategory.Agg;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StoneManagement.Infrastructure
{
    public class StoneDbContext:DbContext
    {
        public DbSet<Stones> Stones { get; set; }
        public DbSet<StoneCategory> Categories { get; set; }
        public StoneDbContext(DbContextOptions<StoneDbContext>options):base(options)
        {
        }
    }
}
