using Microsoft.EntityFrameworkCore;
using Services.Application;
using StoneManagement.Domain.StoneCategory.Agg;

namespace StoneManagement.Infrastructure.Repository
{
    public class StoneCategoryRepository : RepositoryBase<StoneCategory>, IStoneCategoryRepository
    {
        private readonly StoneDbContext _dbcontext;
        public StoneCategoryRepository(StoneDbContext dbcontext) : base(dbcontext)
        {
            _dbcontext = dbcontext;
        }

        public OperationResult Delete(long id)
        {
            OperationResult result = new OperationResult();
            var categ = _dbcontext.Categories.FirstOrDefault(x=>x.Id == id);
            if (categ == null)
            {
                return result.Failed(ApplicationMessage.NotFound);
            }
            _dbcontext.Categories.Remove(categ);
            _dbcontext.SaveChanges();
            return result.IsSuccess();
        }

        public StoneCategory? GetBySlug(string slug)
        {
            if (string.IsNullOrWhiteSpace(slug))
                return null;

            var normalized = slug.Trim().ToLower();
            return _dbcontext.Categories.FirstOrDefault(x => x.Slug == normalized);
        }

        public override List<StoneCategory> GetAll()
        {
            return _dbcontext.Categories.Include(x => x.Stones).ToList();
        }
    }
}
