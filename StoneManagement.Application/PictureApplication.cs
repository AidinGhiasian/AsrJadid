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
        public PictureApplication(IStoneRepository stoneRepository, IFileUploader fileUploader,IPictureRepository pictureRepository)
        {
            _stoneRepository = stoneRepository;
            _fileUploader = fileUploader;
            _pictureRepository = pictureRepository;
        }
        public OperationResult Create(CreateViewModel command)
        {
            var result = new OperationResult();
            var path = "pruductPicture";

            var stone = _stoneRepository.GetByLongId(command.StoneId);

            var mainPicture = _fileUploader.UploadNewSize(command.PictureFile, path, 360);
            stone.Pictures.Add(new Pictures(mainPicture, command.StoneId));
            if (command.Files != null)
            {
                foreach (var file in command.Files)
                {
                    var picture = _fileUploader.UploadNewSize(file, path, 360);
                    stone.Pictures.Add(new Pictures(picture, command.StoneId));
                }
            }
            _stoneRepository.SaveChanges();
            return result.IsSuccess();
        }

        public OperationResult Delete(long id)
        {
            OperationResult result = new OperationResult();
            _pictureRepository.Delete(id);
            _pictureRepository.SaveChanges();
            return result.IsSuccess();
        }

        public OperationResult Edit(EditViewModel command)
        {
            OperationResult result = new OperationResult();
            var path = "prudoctPicture";
            var picture = _pictureRepository.GetByLongId(command.Id);
            var newPicture = _fileUploader.UploadNewSize(command.PictureFile, path, 360);
            picture.Edit(newPicture);
            _stoneRepository.SaveChanges();
            return result.IsSuccess();
        }
    }
}
