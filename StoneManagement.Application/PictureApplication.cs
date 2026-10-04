using Services.Application;
using StoneManagement.Application.Contracts.Picture;
using StoneManagement.Domain.PicturesAgg;
using StoneManagement.Domain.Stone.Agg;

namespace StoneManagement.Application
{
    public class PictureApplication : IPictureApplication
    {
        private readonly IStoneRepository _stoneRepository;
        private readonly IPictureRepository _pictureRepository;
        private readonly IFileUploader _fileUploader;

        private const string Path = "ProductPicture";

        public PictureApplication(IStoneRepository stoneRepository, IFileUploader fileUploader, IPictureRepository pictureRepository)
        {
            _stoneRepository = stoneRepository;
            _fileUploader = fileUploader;
            _pictureRepository = pictureRepository;
        }

        public OperationResult Create(CreateViewModel command)
        {
            var result = new OperationResult();

            var stone = _stoneRepository.GetByLongId(command.StoneId);
            if (stone == null)
            {
                return result.Failed(ApplicationMessage.NotFound);
            }

            if (command.PictureFile != null && command.PictureFile.Length > 0)
            {
                var mainPicture = _fileUploader.UploadNewSize(command.PictureFile, Path, 720);
                stone.Pictures.Add(new Pictures(mainPicture, command.StoneId));
            }

            if (command.Files != null)
            {
                foreach (var file in command.Files)
                {
                    if (file == null || file.Length == 0) continue;

                    var picture = _fileUploader.UploadNewSize(file, Path, 720);
                    stone.Pictures.Add(new Pictures(picture, command.StoneId));
                }
            }

            _stoneRepository.SaveChanges();
            return result.IsSuccess("تصاویر محصول ثبت شدند.");
        }

        public OperationResult Delete(long id)
        {
            var picture = _pictureRepository.GetByLongId(id);
            if (picture == null)
            {
                return new OperationResult().Failed(ApplicationMessage.NotFound);
            }

            _fileUploader.Delete(picture.Picture);
            var result = _pictureRepository.Delete(id);
            _pictureRepository.SaveChanges();
            return result;
        }

        public OperationResult Edit(EditViewModel command)
        {
            OperationResult result = new OperationResult();

            var picture = _pictureRepository.GetByLongId(command.Id);
            if (picture == null)
            {
                return result.Failed(ApplicationMessage.NotFound);
            }

            if (command.PictureFile == null || command.PictureFile.Length == 0)
            {
                return result.Failed("تصویر جدیدی انتخاب نشده است.");
            }

            _fileUploader.Delete(picture.Picture);
            var newPicture = _fileUploader.UploadNewSize(command.PictureFile, Path, 720);
            picture.Edit(newPicture);
            _pictureRepository.SaveChanges();

            return result.IsSuccess("تصویر با موفقیت ویرایش شد.");
        }
    }
}
