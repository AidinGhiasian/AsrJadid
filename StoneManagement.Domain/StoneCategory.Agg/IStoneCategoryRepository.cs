using Services.Application;

namespace StoneManagement.Domain.StoneCategory.Agg
{
    public interface IStoneCategoryRepository:IRepositoryBase<StoneCategory>
    {
        public OperationResult Delete(long id);
        public StoneCategory? GetBySlug(string slug);
    }
}
