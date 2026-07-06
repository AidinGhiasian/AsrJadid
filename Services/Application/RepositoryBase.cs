using Microsoft.EntityFrameworkCore;

namespace Services.Application;

public class RepositoryBase<T> : IRepositoryBase<T> where T : class
    //در اینجا ما معلوم میکنیم که متغیر T
    //معلوم میکند که منظور ما کدام کلاس است و او باید از کدام
   // کلاس برای خود استفاده کند که ما این را در هر ریپازیتوری و اینتر فیس معلئم میکنیم.....
{

    private readonly DbContext _context;
    public RepositoryBase(DbContext context)
    {
        _context = context;
    }

    public void Add(T entity)
    {
        _context.Set<T>().Add(entity);
    }

    public T GetByLongId(long id)
    {
        return _context.Set<T>().Find(id);
    }
    public T GetById(int id)
    {
        return _context.Set<T>().Find(id);
    }
    public List<T> GetAll()
    {
        return _context.Set<T>().ToList();
    }
    public void SaveChanges()
    {
        _context.SaveChanges();
    }
}
//این کار ها معمولا کار هایی هستند که در تمام ریپازیتوری های موجود در پروژه استفاده میشوند
//و یا باید به طور منطقی در هر ریپازیتوری وجود داشته باشند ....