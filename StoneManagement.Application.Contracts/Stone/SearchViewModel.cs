namespace StoneManagement.Application.Contracts.Stone
{
    public class SearchViewModel
    {
        public long Id { get; set; }
        public string Picture { get; set; }
        public string StoneName { get; set; }
        public double Length { get; set; }
        public double Width { get; set; }
        public double Weight { get; set; }
        public decimal Price { get; set; }
        public string Color { get; set; }
        public int Stock { get; set; }
        public long CategoryId { get; set; }
        public string Description { get; set; }
    }
}