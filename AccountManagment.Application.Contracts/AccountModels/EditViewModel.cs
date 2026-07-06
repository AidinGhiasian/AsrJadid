using Microsoft.AspNetCore.Http;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AccountManagment.Application.Contracts.AccountModels
{
    public class EditViewModel:CreateViewModel
    {
        public long Id { get; set; }
        public DateTime BirthDate { get; set; }
        public string Picture { get; set; }
        public IFormFile PictureFile { get; set; }
    }
}
