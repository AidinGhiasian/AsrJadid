using Services.Application;
using StoneManagement.Application.Contracts.Picture;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StoneManagement.Application
{
    public class PictureApplication : IPictureApplication
    {
        public OperationResult Create(CreateViewModel command)
        {
            throw new NotImplementedException();
        }

        public OperationResult Delete(long id)
        {
            throw new NotImplementedException();
        }

        public OperationResult Edit(EditViewModel command)
        {
            throw new NotImplementedException();
        }
    }
}
