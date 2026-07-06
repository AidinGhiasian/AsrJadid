using System;
using System.Collections.Generic;
using System.Text;

namespace Services.Models
{
    public class EntityBase
    {
        public long Id { get; protected set; }
        public DateTime CreateDateTime { get; protected set; }
    }
}
