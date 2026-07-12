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
        public string Name { get; private set; }
        public string Slug { get; private set; }
        public string Description { get; private set; }
        public List<Stones> Stones { get; private set; }
    }
}
