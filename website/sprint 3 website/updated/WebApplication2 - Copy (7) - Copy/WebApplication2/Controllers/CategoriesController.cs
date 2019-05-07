using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace WebApplication2.Controllers
{
    
    public class CategoriesController : ApiController
    {
        public IEnumerable<Category> Get()
        {
            using (fypEntities entities = new fypEntities())
            {
                return entities.Categories.ToList();
            }
        }
    }
}
