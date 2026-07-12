using Services.Application;

namespace StoneManagement.Domain.PicturesAgg
{
    public interface IPictureRepository:IRepositoryBase<Pictures>
    { 
        public OperationResult Delete(long id);

    }
}
