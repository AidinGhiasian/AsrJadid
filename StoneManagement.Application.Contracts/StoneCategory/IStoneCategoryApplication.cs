using Services.Application;

namespace StoneManagement.Application.Contracts.StoneCategory
{
    public interface IStoneCategoryApplication
    {
        public OperationResult Create(CreateViewModel command);
        public OperationResult Edit(EditViewModel command);
        public OperationResult Delete(long id);
        public List<StoneCategoryViewModel> GetAll();
        public EditViewModel? GetDetails(long id);
        public StoneCategoryViewModel? GetInfo(long id);
        public StoneCategoryViewModel? GetBySlug(string slug);
    }
}
