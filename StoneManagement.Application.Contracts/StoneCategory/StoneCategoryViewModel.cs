using StoneManagement.Domain.Stone.Agg;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StoneManagement.Application.Contracts.StoneCategory
{
    public class StoneCategoryViewModel
    {
        public string Name { get;  set; }
        public string Slug { get;  set; }
        public string Description { get;  set; }
        public List<Stones>? Stones { get;  set; }
    }
}
