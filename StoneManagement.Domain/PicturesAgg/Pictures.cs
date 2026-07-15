using Services.Models;

namespace StoneManagement.Domain.PicturesAgg
{
    public class Pictures:EntityBase
    {
        //public long Id { get; set; }
        public long StoneId { get;private set; }
        public string Picture { get;private set; }
        public Pictures(string picture,long stoneId)
        {
            Picture = picture;
            StoneId = stoneId; 
        }
    }
}
