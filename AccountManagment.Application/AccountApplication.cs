using AccountManagment.Application.Contracts.AccountModels;
using AccountManagment.Domain.Domain.Account.Agg;
using Services.Application;
using Services.Application.HashPassword;

namespace AccountManagment.Application
{
    public class AccountApplication : IAccountApplication
    {
        private readonly IAccountRepository _accountRepository;
        private readonly IPasswordHasher _passwordHasher;
        private readonly IFileUploader _fileUploader;
        public AccountApplication(IAccountRepository accountRepository, IPasswordHasher passwordHasher, IFileUploader fileUploader)
        {
            _accountRepository = accountRepository;
            _passwordHasher = passwordHasher;
            _fileUploader = fileUploader;
        }
        public OperationResult Create(CreateViewModel command)
        {
            var result = new OperationResult();
            var password = _passwordHasher.Hash(command.Password);
            var path = "Account";
            var picture = _fileUploader.UploadNewSize(command.PictureFile, path, 360);
            var CreatedAccount = new Accounts(picture, command.Name, command.Family, command.PhoneNumber, command.Address, password);
            _accountRepository.Add(CreatedAccount);
            _accountRepository.SaveChanges();
            return result.IsSuccess();
        }

        public OperationResult Delete(long Id)
        {
            return _accountRepository.Delete(Id);
        }

        public OperationResult Edit(EditViewModel command)
        {
            var result = new OperationResult();
            var account = _accountRepository.GetById(command.Id);
            if (account != null)
            {
                if (account.Picture!=null)
                {
                    _fileUploader.Delete(command.Picture);
                    var path = "Account";
                    command.Picture = _fileUploader.UploadNewSize(command.PictureFile, path, 360);
                }
              
            }
            account.Edit(command.Name, command.Family, command.PhoneNumber, command.Email, command.BirthDate, command.Address, command.Picture);
            return result.IsSuccess();
        }

        public AccountViewModel? GetById(long id)
        {
            var account= _accountRepository.GetById(id);
            return Map(account);
        }

        public EditViewModel GetDetails(long Id)
        {
            var account = _accountRepository.GetById(Id);
            return EditingMap(account);
        }

        public AccountViewModel GetInfo(long Id)
        {
            var account = _accountRepository.GetById(Id);
            return Map(account);
        }

        public List<AccountViewModel> GetList(bool status)
        {
            throw new NotImplementedException();
        }

        public OperationResult login(LoginViewModel command)
        {
            throw new NotImplementedException();
        }

        public OperationResult logout()
        {
            throw new NotImplementedException();
        }

        public OperationResult Restore(long Id)
        {
            throw new NotImplementedException();
        }

        public AccountSearchModel Search(string search)
        {
            throw new NotImplementedException();
        }
        //Maps
        public EditViewModel EditingMap(Accounts edit)
        {
            return new EditViewModel
            {
                Name = edit.Name,
                Family = edit.Family,
                PhoneNumber = edit.PhoneNumber,
                Email = edit.Email,
                Address = edit.Address

            };
        }
        public AccountViewModel Map(Accounts map)
        {
            return new AccountViewModel
            {
                Id = map.Id,
                Name = map.Name,
                Family = map.Family,
                PhoneNumber = map.PhoneNumber,
                Email = map.Email,
                Address = map.Address,
                CreateDateTime = map.CreateDateTime,
                IsActive = map.IsActive,
                Picture=map.Picture,
                RoleId=map.RoleId

            };
        }
    }
}
