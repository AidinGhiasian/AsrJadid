namespace Services.Application
{
    public class OperationResult
    {
        public bool Success { get; set; }
        public bool Failure { get; set; }

        public string Message { get; set; }

        public OperationResult()
        {
            Success = false;
        }

        public OperationResult IsSuccess(string message = "عملیات با موفقیت انجام شد.")
        {
            Success = true;
            Failure = false;
            return this;
        }

        public OperationResult Failed(string message)
        {
            Failure = true; 
            return this;
        }


    }
}
