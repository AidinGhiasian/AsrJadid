using Services.Application;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Domain.Stone.Agg;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StoneManagement.Application
{
    public class StoneApplication : IStoneApplication
    {
        public OperationResult Create(CreateViewModel model)
        {
            throw new NotImplementedException();
        }

        public OperationResult Delete(long id)
        {
            throw new NotImplementedException();
        }

        public OperationResult Edit(EditViewModel model)
        {
            throw new NotImplementedException();
        }

        public StoneViewModel GetById(long id)
        {
            throw new NotImplementedException();
        }

        public EditViewModel GetDetails(long id)
        {
            throw new NotImplementedException();
        }

        public StoneViewModel GetInfo(long id)
        {
            throw new NotImplementedException();
        }

        public List<StoneViewModel> GetList()
        {
            throw new NotImplementedException();
        }

        public List<SearchViewModel> Search(string search)
        {
            throw new NotImplementedException();
        }
    }
}
