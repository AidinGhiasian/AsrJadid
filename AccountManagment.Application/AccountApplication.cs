using AccountManagment.Application.Contracts.AccountModels;
using AccountManagment.Domain.Domain.Account.Agg;
using Services.Application;
using Services.Application.HashPassword;
using Services.Models;
using System.Reflection.Metadata.Ecma335;

namespace AccountManagment.Application
{
    public class AccountApplication : IAccountApplication
    {
        private readonly IAccountRepository _accountRepository;
        private readonly IPasswordHasher _passwordHasher;
        private readonly IFileUploader _fileUploader;
        private readonly IAuthHelper _authHelper;
        public AccountApplication(IAccountRepository accountRepository, IPasswordHasher passwordHasher, IFileUploader fileUploader, IAuthHelper authHelper)
        {
            _accountRepository = accountRepository;
            _passwordHasher = passwordHasher;
            _fileUploader = fileUploader;
            _authHelper = authHelper;
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
            _accountRepository.SaveChanges();
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
            var list = _accountRepository.GetAccounts(status);
            return Maps(list);
        }

        public OperationResult login(LoginViewModel command)
        {
            OperationResult operation = new OperationResult();
            var account = _accountRepository.GetByPhone(command.PhoneNumber);
            if (account == null)
            {
                return operation.Failed(ApplicationMessage.WrongPhoneNumber);
            }
            (bool Verified, bool needUpgrade)result = _passwordHasher.Check(account.Password, command.Password);
            if (!result.Verified)
            {
                return operation.Failed(ApplicationMessage.WrongPassword);
            }
            var auth = new AuthViewModel(account.Id, account.Name,account.Family,account.RoleId,account.PhoneNumber,account.Picture);
            _authHelper.SignIn(auth);
            return operation.IsSuccess();
        }

        public OperationResult logout()
        {
            OperationResult result = new OperationResult();
            _authHelper.SignOut();
            return result.IsSuccess();
        }

        public OperationResult Restore(long Id)
        {
            var opration = new OperationResult();
            _accountRepository.Restore(Id);
            return opration.IsSuccess();
        }

        public List<AccountSearchModel> Search(string search)
        {
            var accountList = _accountRepository.Search(search);
            var accounts = new List<AccountSearchModel>();
            foreach (var account in accountList)
            {
                accounts.Add(SearchMap(account));
            }
            return accounts;
        }
        public OperationResult ChangeRole(long id,long roleId)
        {
            return _accountRepository.ChangeRole(id,roleId);
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
        public List<AccountViewModel> Maps(List<Accounts> list)
        {
            var result = new List<AccountViewModel>();
            foreach (var item in list)
            {
                result.Add(Map(item));
            }
            return result;
        }
        private AccountSearchModel SearchMap(Accounts account)
        {
            return new AccountSearchModel
            {
                Id = account.Id,
                Name = account.Name,
                Family = account.Family,
                PhoneNumber = account.PhoneNumber,
            };
        }
    }
}
