using Services.Application;

namespace StoneManagement.Application.Contracts.Picture
{
    public interface IPictureApplication
    {
        public OperationResult Create(CreateViewModel command);
        public OperationResult Edit(EditViewModel command);
        public OperationResult Delete(long id);
    }
}
