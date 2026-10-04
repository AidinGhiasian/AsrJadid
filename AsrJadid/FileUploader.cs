using Services.Application;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Formats.Jpeg;
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

        private string RootPath => string.IsNullOrWhiteSpace(_webHostEnvironment.WebRootPath)
            ? System.IO.Path.Combine(_webHostEnvironment.ContentRootPath, "wwwroot")
            : _webHostEnvironment.WebRootPath;

        private static string SafeFolder(string path)
        {
            if (string.IsNullOrWhiteSpace(path)) return string.Empty;
            return path.Replace("\\", "/").Trim('/', ' ').Replace("..", string.Empty);
        }

        private static string SafeFileName(string fileName)
        {
            var name = System.IO.Path.GetFileNameWithoutExtension(fileName ?? string.Empty);
            if (string.IsNullOrWhiteSpace(name)) name = "image";

            foreach (var invalid in System.IO.Path.GetInvalidFileNameChars())
                name = name.Replace(invalid, '-');

            return name.Replace(" ", "-");
        }

        public string Upload(IFormFile file, string Path)
        {
            if (file == null || file.Length == 0)
                return string.Empty;

            var folder = SafeFolder(Path);
            var directoryPath = System.IO.Path.Combine(RootPath, "Pictures", folder);
            if (!Directory.Exists(directoryPath))
                Directory.CreateDirectory(directoryPath);

            var extension = System.IO.Path.GetExtension(file.FileName);
            if (string.IsNullOrWhiteSpace(extension)) extension = ".jpg";

            var fileName = $"{DateTime.Now.ToFileName()}-{SafeFileName(file.FileName)}{extension}";
            var filePath = System.IO.Path.Combine(directoryPath, fileName);

            using (var output = File.Create(filePath))
            {
                file.CopyTo(output);
            }

            return $"{folder}/{fileName}";
        }

        public string UploadNewSize(IFormFile file, string Path, int wight)
        {
            if (file == null || file.Length == 0)
                return string.Empty;

            var folder = SafeFolder(Path);
            var size = wight.ToString();
            var directoryPath = System.IO.Path.Combine(RootPath, "Pictures", folder, size);
            if (!Directory.Exists(directoryPath))
                Directory.CreateDirectory(directoryPath);

            var fileName = $"{DateTime.Now.ToFileName()}-{SafeFileName(file.FileName)}.jpg";
            var filePath = System.IO.Path.Combine(directoryPath, fileName);

            using var stream = file.OpenReadStream();
            using var image = Image.Load(stream);

            var height = (int)Math.Round(image.Height * (wight / (double)image.Width));
            if (height < 1) height = 1;

            image.Mutate(x => x.Resize(wight, height));
            image.Save(filePath, new JpegEncoder { Quality = 85 });

            return $"{folder}/{size}/{fileName}";
        }

        public string UploadNewSizeFromWightAndHeight(IFormFile file, string Path, int wight, int Height)
        {
            if (file == null || file.Length == 0)
                return string.Empty;

            var folder = SafeFolder(Path);
            var size = wight.ToString();
            var directoryPath = System.IO.Path.Combine(RootPath, "Pictures", folder, size);
            if (!Directory.Exists(directoryPath))
                Directory.CreateDirectory(directoryPath);

            var fileName = $"{DateTime.Now.ToFileName()}-{SafeFileName(file.FileName)}.jpg";
            var filePath = System.IO.Path.Combine(directoryPath, fileName);

            using var stream = file.OpenReadStream();
            using var image = Image.Load(stream);

            image.Mutate(x => x.Resize(wight, Height));
            image.Save(filePath, new JpegEncoder { Quality = 85 });

            return $"{folder}/{size}/{fileName}";
        }

        public void Delete(string pictureName)
        {
            if (string.IsNullOrWhiteSpace(pictureName))
                return;

            var safeName = SafeFolder(pictureName);
            if (string.IsNullOrWhiteSpace(safeName))
                return;

            var directoryPath = System.IO.Path.Combine(RootPath, "Pictures", safeName);
            if (File.Exists(directoryPath))
                File.Delete(directoryPath);
        }

        public int GetFileCount(List<IFormFile> files)
        {
            return files?.Count ?? 0;
        }
    }
}
