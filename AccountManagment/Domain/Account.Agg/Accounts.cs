using AccountManagment.Domain.Domain.Roles.Agg;
using Services.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AccountManagment.Domain.Domain.Account.Agg
{
    public class Accounts : EntityBase
    {
        public string? Picture { get; private set; }
        public string Name { get; private set; }
        public string Family { get; private set; }
        public string PhoneNumber { get; private set; }
        public string? Email { get; private set; }
        public string? Address { get; private set; }
        public string Password { get; private set; }
        public bool IsActive { get; private set; }
        public long RoleId { get; private set; }

        //Affiliations


        //

        public Accounts(string picture, string name, string family, string phoneNumber, string address, string password)
        {
            Picture = picture;
            Name = name;
            Family = family;
            PhoneNumber = phoneNumber;
            Address = address;
            Password = password;
            IsActive = true;
            RoleId = 1;//user
        }
        public void Edit(string name, string family, string phoneNumber, string email, DateTime birthDate, string address, string picture)
        {
            if (!string.IsNullOrWhiteSpace(picture))
            {
                Picture = picture;
            }
            Name = name;
            Family = family;
            PhoneNumber = phoneNumber;
            Address = address;
            IsActive = true;
        }

        public void ChangePassword(string password)
        {
            Password = password;
        }

        public void ChangeRole(long roleId)
        {
            RoleId = roleId;
        }

        public void ChangeStatus(bool isActive)
        {
            IsActive = isActive;
        }
}}
