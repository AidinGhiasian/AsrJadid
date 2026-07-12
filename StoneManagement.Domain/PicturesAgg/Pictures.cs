using Services.Models;

namespace StoneManagement.Domain.PicturesAgg
{
    public class Pictures:EntityBase
    {
        public long StoneId { get; set; }
        public string Picture { get; set; }
        public Pictures(string picture)
        {
            Picture = picture;
        }
    }
}
