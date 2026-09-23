using Services.Application;
using StoneManagement.Application.Contracts.StoneCategory;
using StoneManagement.Domain.Stone.Agg;
using StoneManagement.Domain.StoneCategory.Agg;

namespace StoneManagement.Application
{
    public class StoneCategoryApplication : IStoneCategoryApplication
    {
        private readonly IStoneCategoryRepository _stoneCategoryRepository;
        private readonly IFileUploader _fileUploader;
        public StoneCategoryApplication(IStoneCategoryRepository stoneCategoryRepository, IFileUploader fileUploader)
        {
            _stoneCategoryRepository = stoneCategoryRepository;
            _fileUploader = fileUploader;
        }
        public OperationResult Create(CreateViewModel command)
        {
            OperationResult result = new OperationResult();
            var path = "Stone";
            var picture = _fileUploader.UploadNewSize(command.PictureFile, path, 720);
            var stoneCategory = new StoneCategory(picture, command.Name, command.Description);
            _stoneCategoryRepository.Add(stoneCategory);
            _stoneCategoryRepository.SaveChanges();
            return result.IsSuccess();
        }

        public OperationResult Delete(long id)
        {
            return _stoneCategoryRepository.Delete(id);
        }

        public OperationResult Edit(EditViewModel command)
        {
            OperationResult result = new OperationResult();
            var stone = _stoneCategoryRepository.GetByLongId(command.Id);
            if (stone != null)
            {
                if (stone.Picture != null)
                {
                    _fileUploader.Delete(stone.Picture);
                    var path = "Stone";
                    command.Picture = _fileUploader.UploadNewSize(command.PictureFile, path, 720);
                }
            }
            stone.Edit(command.Picture, command.Name, command.Description);
            _stoneCategoryRepository.SaveChanges();
            return result.IsSuccess();
        }

        public List<StoneCategoryViewModel> GetAll()
        {
            var list = _stoneCategoryRepository.GetAll();
            return Maps(list);
        }
        //Maps
        private List<StoneCategoryViewModel> Maps(List<StoneCategory> stones)
        {
            var result = new List<StoneCategoryViewModel>();
            foreach (var stone in stones)
            {
                result.Add(Map(stone));
            }
            return result;
        }
        private StoneCategoryViewModel Map(StoneCategory stone)
        {
            return new StoneCategoryViewModel
            {
                Name = stone.Name,
                Description = stone.Description,
                Stones = stone.Stones,
                Slug = stone.Slug,
            };
        }
    }
}
