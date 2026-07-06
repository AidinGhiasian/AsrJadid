using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Services.Application
{
    public interface IRepositoryBase<T> where T : class
    {
        void Add(T entity);
        T GetByLongId(long id);
        T GetById(int id);
        public List<T> GetAll();
        void SaveChanges();
    }
}
//در واقعrepositorybase
// یک کلاس و یک مرجع برای تکرار نشدن کد ها و برای جلوگیری از 
//مشکل های اساسی است و کاربرد اصلی ان در راحت تر کد زدن وسریع پیش رفتن کار است....