using Microsoft.EntityFrameworkCore;
using Services.Application;
using StoneManagement.Domain.Stone.Agg;

namespace StoneManagement.Infrastructure.Repository
{
    public class StoneRepository : RepositoryBase<Stones>, IStoneRepository
    {
        private readonly StoneDbContext _dbcontext;

        public StoneRepository(StoneDbContext dbcontext):base(dbcontext)
        {
            _dbcontext = dbcontext;
        }

        public OperationResult Delete(long id)
        {
            OperationResult operation = new OperationResult();
            var stone = _dbcontext.Stones.FirstOrDefault(x=>x.Id==id);
            if (stone == null)
            {
                return operation.Failed(ApplicationMessage.NotFound);
            }
            _dbcontext.Stones.Remove(stone);
            _dbcontext.SaveChanges();
            return operation.IsSuccess();
        }

        public List<Stones> Search(string search)
        {
            var query = _dbcontext.Stones.Include(x => x.Pictures).AsQueryable();
            if(!string.IsNullOrWhiteSpace(search))
            {
                query = query.Where(x => x.StoneName.Contains(search)
                                         || x.Color.Contains(search)
                                         || x.Description.Contains(search));
            }
            return query.ToList();
        }

        public List<Stones> GetByCategory(long categoryId)
        {
            return _dbcontext.Stones
                .Include(x => x.Pictures)
                .Where(x => x.CategoryId == categoryId)
                .ToList();
        }

        public override List<Stones> GetAll()
        {
            return _dbcontext.Stones.Include(x => x.Pictures).ToList();
        }
    }
}
