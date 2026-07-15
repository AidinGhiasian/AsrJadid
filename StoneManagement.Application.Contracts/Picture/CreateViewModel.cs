using Microsoft.AspNetCore.Http;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StoneManagement.Application.Contracts.Picture
{
    public class CreateViewModel
    {
        public IFormFile PictureFile { get; set; }
        public long StoneId { get; set; }
    }
}
