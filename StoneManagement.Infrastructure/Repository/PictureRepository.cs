using Services.Application;
using StoneManagement.Domain.PicturesAgg;

namespace StoneManagement.Infrastructure.EFCore.Repository
{
    public class PictureRepository : RepositoryBase<Pictures>, IPictureRepository
    {
        private readonly StoneDbContext _stoneDbContext;
        public PictureRepository(StoneDbContext stoneDbContext):base(stoneDbContext) 
        {
            _stoneDbContext = stoneDbContext;
        }
        public OperationResult Delete(long id)
        {
            OperationResult result = new OperationResult();
            var picture = _stoneDbContext.Pictures.FirstOrDefault(x => x.Id == id);
            if (picture == null)
            {
                result.Failed(ApplicationMessage.NotFound);
            }
            _stoneDbContext.Pictures.Remove(picture);
            return result.IsSuccess();
        }
    }
}
