using Services.Application;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AccountManagment.Application.Contracts.AccountModels
{
    public interface IAccountApplication
    {
        public OperationResult Create(CreateViewModel command);
        public OperationResult Edit(EditViewModel command);
        public OperationResult Delete(long Id);
        public OperationResult Restore(long Id);
        public List<AccountViewModel> GetList(bool status);
        public AccountViewModel? GetById(long id);
        public AccountSearchModel Search(string search);
        public EditViewModel GetDetails(long Id);
        public AccountViewModel GetInfo(long Id);
        public OperationResult login(LoginViewModel command);
        public OperationResult logout();

    }
}
