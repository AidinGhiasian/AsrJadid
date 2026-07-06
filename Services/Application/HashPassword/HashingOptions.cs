namespace Services.Application.HashPassword
{
    public sealed class HashingOptions
    {
        public int Iterations { get; set; } = 10000;
    }
}