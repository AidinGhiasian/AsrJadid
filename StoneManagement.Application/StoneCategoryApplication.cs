using Services.Application;
using StoneManagement.Application.Contracts.StoneCategory;
using StoneManagement.Domain.Stone.Agg;
using StoneManagement.Domain.StoneCategory.Agg;

namespace StoneManagement.Application
{
    public class StoneCategoryApplication : IStoneCategoryApplication
    {
        private readonly IStoneCategoryRepository _stoneCategoryRepository;
        private readonly IStoneRepository _stoneRepository;
        private readonly IFileUploader _fileUploader;

        public StoneCategoryApplication(IStoneCategoryRepository stoneCategoryRepository, IStoneRepository stoneRepository, IFileUploader fileUploader)
        {
            _stoneCategoryRepository = stoneCategoryRepository;
            _stoneRepository = stoneRepository;
            _fileUploader = fileUploader;
        }

        public OperationResult Create(CreateViewModel command)
        {
            OperationResult result = new OperationResult();

            if (command == null || string.IsNullOrWhiteSpace(command.Name))
            {
                return result.Failed("نام دسته‌بندی را وارد کنید.");
            }

            var path = "Category";
            var picture = _fileUploader.UploadNewSize(command.PictureFile, path, 720);

            // ترتیب پارامترها: (نام، توضیحات، تصویر)
            var stoneCategory = new StoneCategory(command.Name, command.Description, picture);

            _stoneCategoryRepository.Add(stoneCategory);
            _stoneCategoryRepository.SaveChanges();
            return result.IsSuccess("دسته‌بندی با موفقیت ثبت شد.");
        }

        public OperationResult Delete(long id)
        {
            var category = _stoneCategoryRepository.GetByLongId(id);
            if (category == null)
            {
                return new OperationResult().Failed(ApplicationMessage.NotFound);
            }

            if (_stoneRepository.GetByCategory(id).Any())
            {
                return new OperationResult().Failed("ابتدا محصولات این دسته‌بندی را جابه‌جا یا حذف کنید.");
            }

            return _stoneCategoryRepository.Delete(id);
        }

        public OperationResult Edit(EditViewModel command)
        {
            OperationResult result = new OperationResult();
            var category = _stoneCategoryRepository.GetByLongId(command.Id);
            if (category == null)
            {
                return result.Failed(ApplicationMessage.NotFound);
            }

            if (command.PictureFile != null)
            {
                if (!string.IsNullOrWhiteSpace(category.Picture))
                {
                    _fileUploader.Delete(category.Picture);
                }
                var path = "Category";
                command.Picture = _fileUploader.UploadNewSize(command.PictureFile, path, 720);
            }
            else if (string.IsNullOrWhiteSpace(command.Picture))
            {
                command.Picture = category.Picture;
            }

            // ترتیب پارامترها: (نام، توضیحات، تصویر)
            category.Edit(command.Name, command.Description, command.Picture);
            _stoneCategoryRepository.SaveChanges();
            return result.IsSuccess("دسته‌بندی با موفقیت ویرایش شد.");
        }

        public List<StoneCategoryViewModel> GetAll()
        {
            var list = _stoneCategoryRepository.GetAll();
            return Maps(list);
        }

        public EditViewModel? GetDetails(long id)
        {
            var category = _stoneCategoryRepository.GetByLongId(id);
            if (category == null) return null;

            return new EditViewModel
            {
                Id = category.Id,
                Name = category.Name,
                Description = category.Description,
                Picture = category.Picture
            };
        }

        public StoneCategoryViewModel? GetInfo(long id)
        {
            var category = _stoneCategoryRepository.GetByLongId(id);
            return category == null ? null : Map(category);
        }

        public StoneCategoryViewModel? GetBySlug(string slug)
        {
            var category = _stoneCategoryRepository.GetBySlug(slug);
            return category == null ? null : Map(category);
        }

        //Maps
        private List<StoneCategoryViewModel> Maps(List<StoneCategory> categories)
        {
            var result = new List<StoneCategoryViewModel>();
            foreach (var category in categories)
            {
                result.Add(Map(category));
            }
            return result;
        }

        private StoneCategoryViewModel Map(StoneCategory category)
        {
            // تعداد محصولات هر دسته از مخزن خوانده می‌شود (لیست Stones در حالت عادی بارگذاری نشده است)
            var count = _stoneRepository.GetByCategory(category.Id).Count;

            return new StoneCategoryViewModel
            {
                Id = category.Id,
                Name = category.Name,
                Description = category.Description,
                Picture = category.Picture,
                Slug = category.Slug,
                StoneCount = count
            };
        }
    }
}
