using Services.Application;

namespace StoneManagement.Application.Contracts.Stone
{
    public interface IStoneApplication
    {
        public OperationResult Create(CreateViewModel model);
        public OperationResult Edit(EditViewModel model);
        public OperationResult Delete(long id);
        public List<StoneViewModel> GetList();
        public StoneViewModel GetById(long id);
        public List<SearchViewModel> Search(string search);
        public EditViewModel GetDetails(long id);
        public StoneViewModel GetInfo(long id);
    }
}
