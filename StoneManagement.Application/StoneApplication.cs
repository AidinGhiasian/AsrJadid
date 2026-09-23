using Services.Application;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Domain.PicturesAgg;
using StoneManagement.Domain.Stone.Agg;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Security.Principal;
using System.Text;
using System.Threading.Tasks;
using static Microsoft.EntityFrameworkCore.DbLoggerCategory.Database;

namespace StoneManagement.Application
{
    public class StoneApplication : IStoneApplication
    {
        private readonly IStoneRepository _stoneRepository;
        private readonly IFileUploader _fileUploader;
        public StoneApplication(IStoneRepository stoneRepository, IFileUploader fileUploader)
        {
            _stoneRepository = stoneRepository;
            _fileUploader = fileUploader;
        }
        public OperationResult Create(CreateViewModel command)
        {
            OperationResult operation = new OperationResult();
            var path = "Stone";
            var picture = _fileUploader.UploadNewSize(command.PictureFile, path, 360);
            var createdStone = new Stones(picture, command.StoneName, command.Length, command.Width, command.Weight, command.Price,
                command.Stock, command.Color, command.Description);
            _stoneRepository.Add(createdStone);
            return operation.IsSuccess();
        }

        public OperationResult Delete(long id)
        {
            OperationResult result = new OperationResult();
            _stoneRepository.Delete(id);
            return result.IsSuccess();
        }

        public OperationResult Edit(EditViewModel model)
        {
            OperationResult operation = new OperationResult();
            var stone = _stoneRepository.GetByLongId(model.Id);
            if (stone != null)
            {
                if (model.Picture == null)
                {
                    return operation.Failed(ApplicationMessage.NotFound);
                }
                _fileUploader.Delete(model.Picture);
                var path = "Stone";
                model.Picture = _fileUploader.UploadNewSize(model.PictureFile, path, 360);
            }
            stone.Edit(model.Picture, model.StoneName, model.Length, model.Width, model.Weight, model.Price, model.Stock,
                model.Color, model.Description);
            return operation.IsSuccess();
        }


        public EditViewModel GetDetails(long id)
        {
            var stone = _stoneRepository.GetByLongId(id);
            return EditingMap(stone);
        }

        public StoneViewModel GetInfo(long id)
        {
            var stone = _stoneRepository.GetByLongId(id);
            return Map(stone);
        }

        public List<StoneViewModel> GetList()
        {
            var stoneList = _stoneRepository.GetAll();
            return Maps(stoneList);
        }

        public List<SearchViewModel> Search(string search)
        {
            var searchString = _stoneRepository.Search(search);
            var result = new List<SearchViewModel>();
            foreach (var item in searchString)
            {
                result.Add(SearchMap(item));
            }
            return result;
        }
        //Map 
        public StoneViewModel Map(Stones map)
        {
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
                Description = map.Description
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
        public SearchViewModel SearchMap(Stones stones)
        {
            return new SearchViewModel
            {
                Id = stones.Id,
                Picture = stones.Picture,
                StoneName = stones.StoneName,
                Length = stones.Length,
                Width = stones.Width,
                Weight = stones.Weight,
                Price = stones.Price,
                Stock = stones.Stock,
                Color = stones.Color,
                Description = stones.Description,
                CategoryId = stones.CategoryId,
            };
        }
    }
}
