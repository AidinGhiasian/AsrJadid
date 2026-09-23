using Microsoft.AspNetCore.Http;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StoneManagement.Application.Contracts.StoneCategory
{
    public class CreateViewModel
    {
        public IFormFile PictureFile { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
    }
}
