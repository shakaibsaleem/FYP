using System;
using System.Text;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Data.Entity.Infrastructure;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using System.Web.Http.Description;
using WebApplication2;
using WebApplication2.Models;
namespace WebApplication2.Controllers
{
    public class Products1Controller : ApiController
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


                    String t = d.PCode + "," + d.PPrice + "," + d.PName + "," + d.PAddress;
                    result.Add(class1);
                }
                return result;
            }
        }
        [Route("api/products/{minPrice}/{maxPrice}/{colorOne}/{colorTwo}/{colorThree}/{colorFour}")]
        [ResponseType(typeof(Product))]
        public List<Class1> GetMaterial(string minPrice, string maxPrice, string colorOne, string colorTwo, string colorThree, string colorFour)
        {
            Dictionary<string, int> mapping = new Dictionary<string, int>();
            {
                mapping.Add("Red", 1);
                mapping.Add("Blue", 2);
                mapping.Add("Yellow", 3);
                mapping.Add("Green", 4);
            }
            List<Class1> result = new List<Class1>();
            using (fypEntities entities = new fypEntities())
            {
                IEnumerable<Product> x = entities.Products.ToList();
                if (Int32.Parse(minPrice) == 0 && Int32.Parse(maxPrice) == 0)
                {
                    foreach (Product d in x)
                    {
                        if (d.idColor == mapping[colorOne] || d.idColor == mapping[colorTwo] || d.idColor == mapping[colorThree] || d.idColor == mapping[colorFour])
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
                else
                {
                    foreach (Product d in x)
                    {
                        if ((Convert.ToInt32(d.PPrice) >= Int32.Parse(minPrice) && Convert.ToInt32(d.PPrice) <= Int32.Parse(maxPrice)) && (d.idColor == mapping[colorOne] || d.idColor == mapping[colorTwo] || d.idColor == mapping[colorThree] || d.idColor == mapping[colorFour]))
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

        [Route("api/products/{minPrice}/{maxPrice}/{colorOne}/{colorTwo}/{colorThree}")]
        [ResponseType(typeof(Product))]
        public List<Class1> GetMaterial(string minPrice, string maxPrice, string colorOne, string colorTwo, string colorThree)
        {
            Dictionary<string, int> mapping = new Dictionary<string, int>();
            {
                mapping.Add("Red", 1);
                mapping.Add("Blue", 2);
                mapping.Add("Yellow", 3);
                mapping.Add("Green", 4);
            }
            List<Class1> result = new List<Class1>();
            using (fypEntities entities = new fypEntities())
            {
                IEnumerable<Product> x = entities.Products.ToList();
                if (Int32.Parse(minPrice) == 0 && Int32.Parse(maxPrice) == 0)
                {
                    foreach (Product d in x)
                    {
                        if (d.idColor == mapping[colorOne] || d.idColor == mapping[colorTwo] || d.idColor == mapping[colorThree])
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
                else
                {
                    foreach (Product d in x)
                    {
                        if ((Convert.ToInt32(d.PPrice) >= Int32.Parse(minPrice) && Convert.ToInt32(d.PPrice) <= Int32.Parse(maxPrice)) && (d.idColor == mapping[colorOne] || d.idColor == mapping[colorTwo] || d.idColor == mapping[colorThree]))
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

        [Route("api/products/{minPrice}/{maxPrice}/{colorOne}/{colorTwo}")]
        [ResponseType(typeof(Product))]
        public List<Class1> GetMaterial(string minPrice, string maxPrice, string colorOne, string colorTwo)
        {
            Dictionary<string, int> mapping = new Dictionary<string, int>();
            {
                mapping.Add("Red", 1);
                mapping.Add("Blue", 2);
                mapping.Add("Yellow", 3);
                mapping.Add("Green", 4);
            }
            List<Class1> result = new List<Class1>();
            using (fypEntities entities = new fypEntities())
            {
                IEnumerable<Product> x = entities.Products.ToList();
                if (Int32.Parse(minPrice) == 0 && Int32.Parse(maxPrice) == 0)
                {
                    foreach (Product d in x)
                    {
                        if (d.idColor == mapping[colorOne] || d.idColor == mapping[colorTwo])
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
                else
                {
                    foreach (Product d in x)
                    {
                        if ((Convert.ToInt32(d.PPrice) >= Int32.Parse(minPrice) && Convert.ToInt32(d.PPrice) <= Int32.Parse(maxPrice)) && (d.idColor == mapping[colorOne] || d.idColor == mapping[colorTwo]))
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

        [Route("api/products/{minPrice}/{maxPrice}/{colorOne}")]
        [ResponseType(typeof(Product))]
        public List<Class1> GetMaterial(string minPrice, string maxPrice, string colorOne)
        {
            Dictionary<string, int> mapping = new Dictionary<string, int>();
            {
                mapping.Add("Red", 1);
                mapping.Add("Blue", 2);
                mapping.Add("Yellow", 3);
                mapping.Add("Green", 4);
            }
            List<Class1> result = new List<Class1>();
            using (fypEntities entities = new fypEntities())
            {
                IEnumerable<Product> x = entities.Products.ToList();
                if (Int32.Parse(minPrice) == 0 && Int32.Parse(maxPrice) == 0)
                {
                    foreach (Product d in x)
                    {
                        if (d.idColor == mapping[colorOne])
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
                else
                {
                    foreach (Product d in x)
                    {
                        if ((Convert.ToInt32(d.PPrice) >= Int32.Parse(minPrice) && Convert.ToInt32(d.PPrice) <= Int32.Parse(maxPrice)) && (d.idColor == mapping[colorOne]))
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
    }
}