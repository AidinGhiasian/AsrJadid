using AccountManagment.Application.Contracts.AccountModels;
using AccountManagment.Domain.Domain.Account.Agg;
using AccountManagment.Domain.Domain.Roles.Agg;
using Services.Application;
using Services.Application.HashPassword;
using Services.Models;

namespace AccountManagment.Application
{
    public class AccountApplication : IAccountApplication
    {
        private readonly IAccountRepository _accountRepository;
        private readonly IRoleRepository _roleRepository;
        private readonly IPasswordHasher _passwordHasher;
        private readonly IFileUploader _fileUploader;
        private readonly IAuthHelper _authHelper;

        public AccountApplication(IAccountRepository accountRepository, IRoleRepository roleRepository, IPasswordHasher passwordHasher, IFileUploader fileUploader, IAuthHelper authHelper)
        {
            _accountRepository = accountRepository;
            _roleRepository = roleRepository;
            _passwordHasher = passwordHasher;
            _fileUploader = fileUploader;
            _authHelper = authHelper;
        }

        public OperationResult Create(CreateViewModel command)
        {
            var result = new OperationResult();

            if (command == null || string.IsNullOrWhiteSpace(command.PhoneNumber) || string.IsNullOrWhiteSpace(command.Password))
            {
                return result.Failed("شماره تلفن و رمز عبور الزامی است.");
            }

            var phone = command.PhoneNumber.ToEnglishNumber().Trim();
            if (_accountRepository.GetByPhone(phone) != null)
            {
                return result.Failed("قبلاً با این شماره تلفن ثبت‌نام شده است.");
            }

            var password = _passwordHasher.Hash(command.Password);
            var path = "Account";
            var picture = _fileUploader.UploadNewSize(command.PictureFile, path, 360);

            var createdAccount = new Accounts(picture, command.Name, command.Family, phone, command.Address ?? string.Empty, password, command.Email);

            _accountRepository.Add(createdAccount);
            _accountRepository.SaveChanges();
            return result.IsSuccess("ثبت‌نام با موفقیت انجام شد.");
        }

        public OperationResult Delete(long Id)
        {
            return _accountRepository.Delete(Id);
        }

        public OperationResult Edit(EditViewModel command)
        {
            var result = new OperationResult();
            var account = _accountRepository.GetById(command.Id);
            if (account == null)
            {
                return result.Failed(ApplicationMessage.NotFound);
            }

            if (command.PictureFile != null && command.PictureFile.Length > 0)
            {
                if (!string.IsNullOrWhiteSpace(account.Picture))
                {
                    _fileUploader.Delete(account.Picture);
                }
                var path = "Account";
                command.Picture = _fileUploader.UploadNewSize(command.PictureFile, path, 360);
            }
            else if (string.IsNullOrWhiteSpace(command.Picture))
            {
                command.Picture = account.Picture ?? string.Empty;
            }

            account.Edit(command.Name, command.Family, command.PhoneNumber, command.Email, command.BirthDate, command.Address, command.Picture);
            _accountRepository.SaveChanges();
            return result.IsSuccess("اطلاعات کاربر ویرایش شد.");
        }

        public AccountViewModel? GetById(long id)
        {
            var account = _accountRepository.GetById(id);
            return account == null ? null : Map(account);
        }

        public EditViewModel? GetDetails(long Id)
        {
            var account = _accountRepository.GetById(Id);
            return account == null ? null : EditingMap(account);
        }

        public AccountViewModel? GetInfo(long Id)
        {
            var account = _accountRepository.GetById(Id);
            return account == null ? null : Map(account);
        }

        public List<AccountViewModel> GetList(bool status)
        {
            var list = _accountRepository.GetAccounts(status);
            return Maps(list);
        }

        public OperationResult login(LoginViewModel command)
        {
            OperationResult operation = new OperationResult();

            if (command == null || string.IsNullOrWhiteSpace(command.PhoneNumber) || string.IsNullOrWhiteSpace(command.Password))
            {
                return operation.Failed("شماره تلفن و رمز عبور را وارد کنید.");
            }

            var phone = command.PhoneNumber.ToEnglishNumber().Trim();
            var account = _accountRepository.GetByPhone(phone);
            if (account == null)
            {
                return operation.Failed(ApplicationMessage.WrongPhoneNumber);
            }

            if (!account.IsActive)
            {
                return operation.Failed("حساب کاربری شما غیرفعال است.");
            }

            var result = _passwordHasher.Check(account.Password, command.Password);
            if (!result.Verified)
            {
                return operation.Failed(ApplicationMessage.WrongPassword);
            }

            var auth = new AuthViewModel(account.Id, account.Name, account.Family, account.RoleId, account.PhoneNumber, account.Picture ?? string.Empty);
            _authHelper.SignIn(auth);
            return operation.IsSuccess("ورود با موفقیت انجام شد.");
        }

        public OperationResult logout()
        {
            OperationResult result = new OperationResult();
            _authHelper.SignOut();
            return result.IsSuccess("با موفقیت خارج شدید.");
        }

        public OperationResult Restore(long Id)
        {
            return _accountRepository.Restore(Id);
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

        public OperationResult ChangeRole(long id, long roleId)
        {
            return _accountRepository.ChangeRole(id, roleId);
        }

        public OperationResult ChangePassword(AccountManagment.Application.Contracts.AccountModels.ChangePassword command)
        {
            var result = new OperationResult();
            var account = _accountRepository.GetById(command.Id);
            if (account == null)
            {
                return result.Failed(ApplicationMessage.NotFound);
            }

            if (command.Password != command.RePassword)
            {
                return result.Failed(ApplicationMessage.passwordIsNotMath);
            }

            account.ChangePassword(_passwordHasher.Hash(command.Password));
            _accountRepository.SaveChanges();
            return result.IsSuccess("رمز عبور تغییر کرد.");
        }

        //Maps
        public EditViewModel EditingMap(Accounts edit)
        {
            return new EditViewModel
            {
                Id = edit.Id,
                Name = edit.Name,
                Family = edit.Family,
                PhoneNumber = edit.PhoneNumber,
                Email = edit.Email,
                Address = edit.Address,
                BirthDate = edit.BirthDate ?? default,
                Picture = edit.Picture
            };
        }

        public AccountViewModel Map(Accounts map)
        {
            var role = _roleRepository.GetById(map.RoleId);

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
                Picture = map.Picture,
                RoleId = map.RoleId,
                Role = role?.Name
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
