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
                operation.Failed(ApplicationMessage.NotFund);
            }
            _dbcontext.Stones.Remove(stone);
            _dbcontext.SaveChanges();
            return operation;
        }

        public List<Stones> Search(string search)
        {
            var query = _dbcontext.Stones.AsQueryable();
            if(!string.IsNullOrWhiteSpace(search))
            {
                query = query.Where(x => x.StoneName.Contains(search));
            }
            return query.ToList();
        }
    }
}
