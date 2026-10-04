using Services.Application;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Domain.Stone.Agg;
using StoneManagement.Domain.StoneCategory.Agg;

namespace StoneManagement.Application
{
    public class StoneApplication : IStoneApplication
    {
        private readonly IStoneRepository _stoneRepository;
        private readonly IStoneCategoryRepository _stoneCategoryRepository;
        private readonly IFileUploader _fileUploader;

        public StoneApplication(IStoneRepository stoneRepository, IStoneCategoryRepository stoneCategoryRepository, IFileUploader fileUploader)
        {
            _stoneRepository = stoneRepository;
            _stoneCategoryRepository = stoneCategoryRepository;
            _fileUploader = fileUploader;
        }

        public OperationResult Create(CreateViewModel command)
        {
            OperationResult operation = new OperationResult();

            if (command == null || string.IsNullOrWhiteSpace(command.StoneName))
            {
                return operation.Failed("نام محصول را وارد کنید.");
            }

            var path = "Stone";
            var picture = _fileUploader.UploadNewSize(command.PictureFile, path, 720);

            var createdStone = new Stones(picture, command.StoneName, command.Length, command.Width, command.Weight, command.Price,
                command.Stock, command.Color, command.Description, command.CategoryId);

            _stoneRepository.Add(createdStone);
            _stoneRepository.SaveChanges();

            return operation.IsSuccess("محصول با موفقیت ثبت شد.");
        }

        public OperationResult Delete(long id)
        {
            return _stoneRepository.Delete(id);
        }

        public OperationResult Edit(EditViewModel model)
        {
            OperationResult operation = new OperationResult();

            var stone = _stoneRepository.GetByLongId(model.Id);
            if (stone == null)
            {
                return operation.Failed(ApplicationMessage.NotFound);
            }

            if (model.PictureFile != null)
            {
                if (!string.IsNullOrWhiteSpace(stone.Picture))
                {
                    _fileUploader.Delete(stone.Picture);
                }
                var path = "Stone";
                model.Picture = _fileUploader.UploadNewSize(model.PictureFile, path, 720);
            }
            else if (string.IsNullOrWhiteSpace(model.Picture))
            {
                model.Picture = stone.Picture;
            }

            stone.Edit(model.Picture, model.StoneName, model.Length, model.Width, model.Weight, model.Price,
                model.Stock, model.Color, model.Description, model.CategoryId);

            _stoneRepository.SaveChanges();
            return operation.IsSuccess("محصول با موفقیت ویرایش شد.");
        }

        public EditViewModel? GetDetails(long id)
        {
            var stone = _stoneRepository.GetByLongId(id);
            return stone == null ? null : EditingMap(stone);
        }

        public StoneViewModel? GetInfo(long id)
        {
            var stone = _stoneRepository.GetByLongId(id);
            return stone == null ? null : Map(stone);
        }

        public List<StoneViewModel> GetList()
        {
            var stoneList = _stoneRepository.GetAll();
            return Maps(stoneList);
        }

        public List<StoneViewModel> GetByCategory(long categoryId)
        {
            var stoneList = _stoneRepository.GetByCategory(categoryId);
            return Maps(stoneList);
        }

        public List<SearchViewModel> Search(string search)
        {
            var searchString = _stoneRepository.Search(search);
            return SearchMaps(searchString);
        }

        //Map 
        public StoneViewModel Map(Stones map)
        {
            var category = map.CategoryId > 0 ? _stoneCategoryRepository.GetByLongId(map.CategoryId) : null;

            return new StoneViewModel
            {
                Id = map.Id,
                Picture = map.Picture,
                StoneName = map.StoneName,
                Length = map.Length,
                Width = map.Width,
                Weight = map.Weight,
                Price = map.Price,
                Stock = map.Stock,
                Color = map.Color,
                CategoryId = map.CategoryId,
                CategoryName = category?.Name,
                CategorySlug = category?.Slug,
                Description = map.Description,
                CreateDateTime = map.CreateDateTime,
                Pictures = map.Pictures?.Where(x => !string.IsNullOrWhiteSpace(x.Picture)).Select(x => x.Picture).ToList() ?? new List<string>()
            };
        }

        public EditViewModel EditingMap(Stones map)
        {
            return new EditViewModel
            {
                Id = map.Id,
                Picture = map.Picture,
                StoneName = map.StoneName,
                Length = map.Length,
                Width = map.Width,
                Weight = map.Weight,
                Price = map.Price,
                Stock = map.Stock,
                Color = map.Color,
                CategoryId = map.CategoryId,
                Description = map.Description
            };
        }

        public List<StoneViewModel> Maps(List<Stones> maps)
        {
            var result = new List<StoneViewModel>();
            foreach (var item in maps)
            {
                result.Add(Map(item));
            }
            return result;
        }

        public SearchViewModel SearchMap(Stones stone)
        {
            return new SearchViewModel
            {
                Id = stone.Id,
                Picture = stone.Picture,
                StoneName = stone.StoneName,
                Length = stone.Length,
                Width = stone.Width,
                Weight = stone.Weight,
                Price = stone.Price,
                Stock = stone.Stock,
                Color = stone.Color,
                Description = stone.Description,
                CategoryId = stone.CategoryId,
            };
        }

        public List<SearchViewModel> SearchMaps(List<Stones> stones)
        {
            var result = new List<SearchViewModel>();
            foreach (var item in stones)
            {
                result.Add(SearchMap(item));
            }
            return result;
        }
    }
}
