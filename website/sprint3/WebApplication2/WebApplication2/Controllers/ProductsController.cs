using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using System.Web.Http.Description;
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
                    class1.pAddress = d.PAddress;
                

                   String t= d.PCode + "," + d.PPrice + "," + d.PName + "," + d.PAddress;
                    result.Add(class1);
                }
                return result;
            }
        }
        
        [Route("api/products/{material}")]
        [ResponseType(typeof(Product))]
        public List<Class1> GetMaterial(string material)
        {
            Dictionary<string, int> mapping = new Dictionary<string, int>();
            {
                mapping.Add("Lawn", 1); 
                mapping.Add("Cotton", 2);
                mapping.Add("Washing Wear", 3);
            }
            List<Class1> result = new List<Class1>();
            using (fypEntities entities = new fypEntities())
            {
                IEnumerable<Product> x = entities.Products.ToList();
                foreach (Product d in x)
                {
                    if (d.idMaterial == mapping[material])
                    {
                        Class1 class1 = new Class1();
                        class1.code = d.PCode;
                        class1.name = d.PName;
                        class1.price = d.PPrice.Value;
                        class1.pAddress = d.PAddress;
                        result.Add(class1);
                    }
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
        public String pAddress;
        //public Double material; 
    }

}
