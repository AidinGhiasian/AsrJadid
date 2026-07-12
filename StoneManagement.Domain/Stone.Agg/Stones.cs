using Services.Models;
using StoneManagement.Domain.PicturesAgg;
namespace StoneManagement.Domain.Stone.Agg
{
    public class Stones : EntityBase
    {

        public string Picture { get; set; }//تصویر اولیه
        public string StoneName { get; private set; }
        public double Length { get; private set; }//12.5 طول
        public double Width { get; private set; }//3.56 عرض
        public double Weight { get; private set; }//3.56 وزن
        public decimal Price { get; private set; }//بدون خطای گرد کردن برای قیمت
        public int Stock { get; private set; }//موجودی انبار|
        public string Color { get; private set; }
        public long CategoryId { get; private set; }//دسته بندی
        public string Description { get; private set; }
        public List<Pictures> Pictures { get; set; }//تصاویر اضافی
        public Stones(string picture, string stoneName, double length, double width, double weight, decimal price, int stock, string color, string description)
        {
            Picture = picture;
            StoneName = stoneName;
            Length = length;
            Width = width;
            Weight = weight;
            Price = price;
            Stock = stock;
            Color = color;
            Description = description;
        }
        public void Edit(string picture, string stoneName, double length, double width, double weight, decimal price, int stock, string color, string description)
        {
            Picture = picture;
            StoneName = stoneName;
            Length = length;
            Width = width;
            Weight = weight;
            Price = price;
            Stock = stock;
            Color = color;
            Description = description;
        }
    }
}