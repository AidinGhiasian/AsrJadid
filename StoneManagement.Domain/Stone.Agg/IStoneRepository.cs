using Services.Application;

namespace StoneManagement.Domain.Stone.Agg
{
    public interface IStoneRepository:IRepositoryBase<Stones>
    {
        public OperationResult Delete(long id);
        public List<Stones> Search(string search);
        public List<Stones> GetByCategory(long categoryId);
    }
}
