
using Services.Application;
//using System.Drawing;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Processing;

namespace Services.Model
{
    public class FileUploader : IFileUploader
    {
        private readonly IWebHostEnvironment _webHostEnvironment;

        public FileUploader(IWebHostEnvironment webHostEnvironment)
        {
            _webHostEnvironment = webHostEnvironment;
        }
        public string Upload(IFormFile file, string Path)
        {
            if (file == null)
                return "";
            var DirectoryPath = $"{_webHostEnvironment.WebRootPath}//Pictures//{Path}";

            if (!Directory.Exists(DirectoryPath))
                Directory.CreateDirectory(DirectoryPath);

            var fileName = $"{DateTime.Now.ToFileName()}-{file.FileName}";
            var filepath = $"{DirectoryPath}//{fileName}";

            using var output = File.Create(filepath);
            file.CopyTo(output);

            return $"{Path}/{fileName}";

        }

        public string UploadNewSize(IFormFile file, string Path, int wight)
        {
            if (file == null)
                return "";
            var size = wight;
            var DirectoryPath = $"{_webHostEnvironment.WebRootPath}//Pictures//{Path}//{size}";
            if (!Directory.Exists(DirectoryPath))
                Directory.CreateDirectory(DirectoryPath);

            var fileName = $"{DateTime.Now.ToFileName()}-{file.FileName}";
            var filepath = $"{DirectoryPath}//{fileName}";

            System.Drawing.Bitmap source_Bitmap = new System.Drawing.Bitmap(file.OpenReadStream());



            double dblWidth_origial = source_Bitmap.Width;

            double dblHeigth_origial = source_Bitmap.Height;

            double relation_heigth_width = dblHeigth_origial / dblWidth_origial;

            int Height = (int)(wight * relation_heigth_width);





            using (Image img = Image.Load(file.OpenReadStream()))
            {
                img.Mutate(r => r.Resize(wight, Height));
                img.Save(filepath);
            }

            return $"{Path}/{size}/{fileName}";


        }

        public string UploadNewSizeFromWightAndHeight(IFormFile file, string Path, int wight, int Height)
        {
            if (file == null)
                return "";
            var size = wight;
            var DirectoryPath = $"{_webHostEnvironment.WebRootPath}//Pictures//{Path}//{size}";
            if (!Directory.Exists(DirectoryPath))
                Directory.CreateDirectory(DirectoryPath);

            var fileName = $"{DateTime.Now.ToFileName()}-{file.FileName}";
            var filepath = $"{DirectoryPath}//{fileName}";

            using (Image img = Image.Load(file.OpenReadStream()))
            {
                img.Mutate(r => r.Resize(wight, Height));
                img.Save(filepath);
            }

            return $"{Path}/{size}/{fileName}";


        }
        public void Delete(string pictureName)
        {
            if (string.IsNullOrWhiteSpace(pictureName))
            {
                return;
            }
            var DirectoryPath = $"{_webHostEnvironment.WebRootPath}//Pictures//{pictureName}";

            if (File.Exists(DirectoryPath))
                File.Delete(DirectoryPath);
        }

        public int GetFileCount(List<IFormFile> files)
        {
            throw new NotImplementedException();
        }
    }
}





