using Microsoft.AspNetCore.Http;
using Services.Models;
using StoneManagement.Domain.Stone.Agg;

namespace StoneManagement.Domain.StoneCategory.Agg
{
    public class StoneCategory : EntityBase
    {
        public string Picture { get; set; }
        public string Name { get;private set; }
        public string Slug { get;private set; }
        public string Description { get;private set; }
        public List<Stones>? Stones { get;private set; }

        public StoneCategory(string name,string description,string picture) 
        {
            Name = name;
            Slug = Slugify(name);
            Description = description;
            Picture = picture;
        }

        public void Edit(string name,string description,string picture)
        {
            Name = name;
            Slug = Slugify(name);
            Description = description;
            Picture = picture;
        }

        private string Slugify(string text)
        {
            return text.Trim().ToLower().Replace(" ", "_");
        }
    }
}
