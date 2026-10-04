using Microsoft.AspNetCore.Mvc.RazorPages;
using Services.Application;
using StoneManagement.Application.Contracts.Stone;
using StoneManagement.Application.Contracts.StoneCategory;

namespace AsrJadid.Pages
{
    public class GalleryModel : PageModel
    {
        private readonly IStoneApplication _stoneApplication;
        private readonly IStoneCategoryApplication _stoneCategoryApplication;

        public GalleryModel(IStoneApplication stoneApplication, IStoneCategoryApplication stoneCategoryApplication)
        {
            _stoneApplication = stoneApplication;
            _stoneCategoryApplication = stoneCategoryApplication;
        }

        public List<GalleryItem> Items { get; set; } = new();
        public List<StoneCategoryViewModel> Categories { get; set; } = new();

        public void OnGet()
        {
            Categories = _stoneCategoryApplication.GetAll();

            // هر تصویر محصول (تصویر اصلی و تصاویر تکمیلی) به‌عنوان یک قاب گالری نمایش داده می‌شود
            foreach (var stone in _stoneApplication.GetList())
            {
                Items.Add(new GalleryItem
                {
                    Title = stone.StoneName,
                    CategoryName = string.IsNullOrWhiteSpace(stone.CategoryName) ? "عصرجدید" : stone.CategoryName,
                    Image = stone.Picture.ImageUrl()
                });

                foreach (var picture in stone.Pictures)
                {
                    if (string.IsNullOrWhiteSpace(picture))
                        continue;

                    Items.Add(new GalleryItem
                    {
                        Title = stone.StoneName,
                        CategoryName = string.IsNullOrWhiteSpace(stone.CategoryName) ? "عصرجدید" : stone.CategoryName,
                        Image = picture.ImageUrl()
                    });
                }
            }
        }

        public class GalleryItem
        {
            public string Title { get; set; } = string.Empty;
            public string CategoryName { get; set; } = string.Empty;
            public string Image { get; set; } = string.Empty;
        }
    }
}
