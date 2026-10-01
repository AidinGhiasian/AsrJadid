
using Services.Models;

namespace StoneManagement.Domain.PicturesAgg
{
    public class Pictures : EntityBase
    {
        public long StoneId { get; private set; }
        public string Picture { get; private set; }

        public Pictures(string picture, long stoneId)
        {
            Picture = picture;
            StoneId = stoneId;
        }
        public void Edit(string picture)
        {
            Picture = picture;
        }
    }
}
