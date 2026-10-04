namespace StoneManagement.Application.Contracts.StoneCategory
{
    public class StoneCategoryViewModel
    {
        public long Id { get; set; }
        public string Name { get; set; }
        public string Slug { get; set; }
        public string Picture { get; set; }
        public string Description { get; set; }
        public int StoneCount { get; set; }
    }
}
