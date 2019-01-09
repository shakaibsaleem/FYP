using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using WebApplication2.Models;
namespace WebApplication2.Controllers
{
    public class ProductsController : ApiController
    {
        public List<Class1> Get()
        {
            List<Class1> result = new List<Class1>();
            using (fypEntities entities = new fypEntities())
            {
                IEnumerable<Product> x = entities.Products.ToList();
                foreach (Product d in x)
                {
                    //d.ToString()
                    Class1 class1 = new Class1();
                    class1.code = d.PCode;
                    class1.name = d.PName;
                    class1.price = d.PPrice.Value;
                

                   String t= d.PCode + "," + d.PPrice + "," + d.PName;
                    result.Add(class1);
                }
                return result;
            }
        }
       
    }

    public class Class1
    {
        public String code;
        public Double price;
        public String name;
    }
}
