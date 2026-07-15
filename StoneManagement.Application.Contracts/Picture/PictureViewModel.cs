using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StoneManagement.Application.Contracts.Picture
{
    public class PictureViewModel
    {
        public long Id { get; set; }
        public long StoneId { get; set; }
        public string Picture { get; set; }
    }
}