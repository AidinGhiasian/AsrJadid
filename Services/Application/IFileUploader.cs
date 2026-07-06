using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;

namespace Services.Application
{
    public interface IFileUploader
    {
        string Upload(IFormFile file, string Path);
        public string UploadNewSize(IFormFile file, string Path, int wight);
        public string UploadNewSizeFromWightAndHeight(IFormFile file, string Path, int wight, int Height);
        public void Delete(string pictureName);
    }
}
