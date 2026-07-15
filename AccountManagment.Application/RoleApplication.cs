using AccountManagment.Application.Contracts.RoleModels;
using AccountManagment.Domain.Domain.Roles.Agg;
using Services.Application;

namespace AccountManagment.Application
{
    public class RoleApplication : IRoleApplication
    {
        private readonly IRoleRepository _roleRepository;
        public RoleApplication(IRoleRepository  roleRepository)
        {
            _roleRepository = roleRepository;
        }
        public OperationResult Create(CreateViewModel command)
        {
            OperationResult result = new OperationResult();
            var createdRole = new Roles(command.Name);
            _roleRepository.Add(createdRole);
            _roleRepository.SaveChanges();
            return result.IsSuccess();
        }
        
        public OperationResult Edit(EditViewModel command)
        {
            OperationResult result = new OperationResult();
            var role = _roleRepository.GetById(command.Id);
            if (role==null)
            {
                return result.Failed(ApplicationMessage.NotFound);
            }
            role.Edit(command.Name);
            _roleRepository.SaveChanges();
            return result.IsSuccess();
            

        }

        public EditViewModel GetDetails(long Id)
        {
            var role = _roleRepository.GetById(Id);
            return EditMaping(role);
        }

        public List<RoleViewModel> RoleList()
        {
            var roles = _roleRepository.GetAll();
            return Maps(roles);
        }
        //Maps
        public EditViewModel EditMaping(Roles map)
        {
            return new EditViewModel
            {
              Id = map.Id,
              Name = map.Name,
            };
        }
        public List<RoleViewModel>Maps(List<Roles> maps)
        {
            var result = new List<RoleViewModel>();
            foreach (var item in maps)
            {
                result.Add(Map(item));
            }
            return result;
        }
        public RoleViewModel Map(Roles map)
        {
            return new RoleViewModel
            {
                Id = map.Id,
                Name = map.Name,
            };
        }
    }
}
