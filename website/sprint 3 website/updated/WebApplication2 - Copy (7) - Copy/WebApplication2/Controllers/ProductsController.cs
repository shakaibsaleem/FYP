using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using System.Web.Http;
using System.Web.Http.Description;
using WebApplication2.Models;
using System.IO;

namespace WebApplication2.Controllers
{
    public class ProductsController : ApiController
    {
        private fypEntities db = new fypEntities();

        public object messagebox { get; private set; }

        public List<Class1> Get()
        {
            List<Class1> result = new List<Class1>();
            using (fypEntities entities = new fypEntities())
            {
                IEnumerable<Product> x = entities.Products.ToList();
                Class1 temp = new Class1();
                temp.name = "";
                List<string> list = new List<string>(new string[] {"yr19103-blue-2pc","mr19113-orange-2pc", "mr19116-green-2pc", "rr19102-yellow-3pc",
                    "rr19103-green-3pc", "rr19104-black-3pc", "rr19104-black-3pc", "yr19101-blue-2pc", "yr19103-blue-2pc", "mr19110-grey-2pc", "mr19109-yellow-2pc",
                    "rr19103-black-3pc","rr19102-yellow-3pc","rr19102-pink-3pc","mr19116-green-2pc","mr19116-brown-2pc","mr19113-orange-2pc","mr19112-mustard-2pc","mr19112-grey-2pc","mr19111-blue-2pc","mr19111-beige-2pc","mr19110-grey-2pc","mr19109-yellow-2pc","mr19109-orange-2pc",
                    "mr19108-yellow-2pc","mr19108-beige-2pc","mr19107-purple-2pc","mr19107-black-2pc","mr19106-beige-2pc","mr19105-beige-2pc","mr19104-yellow-2pc","mr19104-orange-2pc","mr19103-yellow-2pc","mr19103-pink-2pc","mr19102-orange-2pc","mr19102-blue-2pc","mr19101-green-2pc","jf19112-off-white-2pc",
                    "lf19104-green-2pc","lf19103-yellow-2pc","lf19102-blue-2pc","lf19104-blue-2pc","lf19103-green-2pc","jf19112-off-white-2pc","jf19107-blue-2pc","ar19119-red-3pc","ar19118-red-3pc","ar19115-yellow-3pc","br19108-blue-3pc","br19106-pink-3pc","br19102-yellow-3pc","br19101-beige-3pc","nr19107-orange-2pc"});
                foreach (Product d in x)
                {
                    if (d.PName == temp.name)
                    {
                        continue;
                    }
                    else
                    {
                        if (list.Contains(d.PCode)) { continue; }
                        else
                        {
                            DirectoryInfo y = new DirectoryInfo(@"C:\Users\sh01703\Desktop\naeema\WebApplication2 - Copy (7) - Copy\WebApplication2\Content\Content\images\" + d.PCode);
                            FileInfo[] Files = y.GetFiles("*.JPG");
                            //string str = "";
                            //foreach (FileInfo file in Files)
                            //{
                            //    str = str + ", " + file.Name;
                            //}

                            Class1 class1 = new Class1();
                            class1.code = d.PCode;
                            class1.name = d.PName;
                            class1.price = d.PPrice.Value;
                            class1.pAddress = d.PAddress;
                            class1.displayPic = Files[0].Name;
                            class1.description = d.PDescription;

                            String t = d.PCode + "," + d.PPrice + "," + d.PName + "," + d.PAddress;
                            result.Add(class1);
                            temp.name = class1.name;
                        }
                    }
                }
                return result;
            }
        }
        /*
        [Route("api/products/{pc}")]
        [ResponseType(typeof(Product))]
        public List<string> GetMaterial(string pc)
        {
            DirectoryInfo y = new DirectoryInfo(@"D:\fyp\asp\sprint 3\finale\WebApplication2 - Copy (7) - Copy\WebApplication2\Content\Content\images\clusters\" + pc);
            FileInfo[] Files = y.GetFiles("*.JPG");
            List<string> files1 = new List<string>();
            foreach (FileInfo file in Files)
            {
                files1.Add(file.ToString());
            }
            return files1;
        }*/

        public List<Class1> PostFiltered(searchCriteriaDTO sc)
        {
            List<Class1> result = new List<Class1>();
            using (fypEntities entities = new fypEntities())
            {
                IEnumerable<Product> x = entities.Products.ToList();
                foreach (Product d in x)
                {
                    bool isValid = true;
                    if (sc.idMaterial.Count != 0 && sc.idMaterial.Contains(d.idMaterial) == false) { isValid = false; }
                    if (sc.idColor.Count != 0 && sc.idColor.Contains(d.idColor) == false) { isValid = false; }
                    if (sc.idWebsite.Count != 0 && sc.idWebsite.Contains(d.idWebsite) == false) { isValid = false; }
                    if (sc.idCategory.Count != 0 && sc.idCategory.Contains(d.idCategory) == false) { isValid = false; }
                    if (sc.PName != null && sc.PName == d.PName) { isValid = false; }
                    if (sc.PDescription != null && sc.PDescription == d.PDescription) { isValid = false; }
                    if (sc.PCode != null && sc.PCode == d.PCode) { isValid = false; }
                    if (sc.PisAvaialble != null && sc.PisAvaialble == d.PisAvaialble) { isValid = false; }
                    if (sc.minPrice != 0 && sc.maxPrice != 0 && (d.PPrice < sc.minPrice)) { isValid = false; }
                    if (sc.minPrice != 0 && sc.maxPrice != 0 && (d.PPrice > sc.maxPrice)) { isValid = false; }
                    //if (sc.minPrice != null && sc.maxPrice != null && (d.PPrice >= sc.minPrice) && (d.PPrice <= sc.maxPrice)) { isValid = false; }
                    if (isValid == true)
                    {
                        DirectoryInfo y = new DirectoryInfo(@"C:\Users\sh01703\Desktop\naeema\WebApplication2 - Copy (7) - Copy\WebApplication2\Content\Content\images\" + d.PCode);
                        FileInfo[] Files = y.GetFiles("*.JPG");
                        Class1 class1 = new Class1();
                        class1.code = d.PCode;
                        class1.name = d.PName;
                        class1.price = d.PPrice.Value;
                        class1.pAddress = d.PAddress;
                        class1.description = d.PDescription;
                        class1.displayPic = Files[0].Name;
                        String t = d.PCode + "," + d.PPrice + "," + d.PName + "," + d.PAddress;
                        result.Add(class1);
                    }
                }
                return result;
            }
        }

        public List<Class1> PostSim(string sc)
        {
            List<Class1> result = new List<Class1>();
            using (fypEntities entities = new fypEntities())
            {

                /* bool isValid = true;
                 if (sc.idMaterial.Count != 0 && sc.idMaterial.Contains(d.idMaterial) == false) { isValid = false; }
                 if (sc.idColor.Count != 0 && sc.idColor.Contains(d.idColor) == false) { isValid = false; }
                 if (sc.idWebsite.Count != 0 && sc.idWebsite.Contains(d.idWebsite) == false) { isValid = false; }
                 if (sc.idCategory.Count != 0 && sc.idCategory.Contains(d.idCategory) == false) { isValid = false; }
                 if (sc.PName != null && sc.PName == d.PName) { isValid = false; }
                 if (sc.PDescription != null && sc.PDescription == d.PDescription) { isValid = false; }
                 if (sc.PCode != null && sc.PCode == d.PCode) { isValid = false; }
                 if (sc.PisAvaialble != null && sc.PisAvaialble == d.PisAvaialble) { isValid = false; }
                 if (sc.minPrice != 0 && sc.maxPrice != 0 && (d.PPrice < sc.minPrice)) { isValid = false; }
                 if (sc.minPrice != 0 && sc.maxPrice != 0 && (d.PPrice > sc.maxPrice)) { isValid = false; }
                 //if (sc.minPrice != null && sc.maxPrice != null && (d.PPrice >= sc.minPrice) && (d.PPrice <= sc.maxPrice)) { isValid = false; }
                 if (isValid == true)*/

                DirectoryInfo y = new DirectoryInfo(@"C:\Users\sh01703\Desktop\naeema\WebApplication2 - Copy (7) - Copy\WebApplication2\Content\Content\images\clusters\" + sc);
                FileInfo[] Files = y.GetFiles("*.JPG");
                foreach (FileInfo r in Files)
                {
                    Class1 class1 = new Class1();
                    class1.code = null;
                    class1.name = null;
                    class1.price = 0;
                    class1.pAddress = null;
                    class1.description = null;
                    class1.displayPic = Files[0].Name;
                            
                    result.Add(class1);
                }
                    
                
                return result;
            }
        }

    }

    public class ProductDTO
    {
        public int idProduct { get; set; }
        public int idCategory { get; set; }
        public int idMaterial { get; set; }
        public int idColor { get; set; }
        public int idWebsite { get; set; }
        public string PName { get; set; }
        public Nullable<double> PPrice { get; set; }
        public string PAddress { get; set; }
        public Nullable<bool> PisAvaialble { get; set; }
        public string PCode { get; set; }
        public string PDescription { get; set; }
    }


    public class searchCriteriaDTO
    {
        public List<int> idCategory = new List<int>();
        public List<int> idMaterial = new List<int>();
        public List<int> idColor = new List<int>();
        public List<int> idWebsite = new List<int>();
        public string PName { get; set; }
        public double minPrice { get; set; }
        public double maxPrice { get; set; }
        public bool PisAvaialble { get; set; }
        public string PCode { get; set; }
        public string PDescription { get; set; }
    }
    public class Class1
    {
        public String code;
        public Double price;
        public String name;
        public String pAddress;
        public string displayPic;
        public string description;
        //public Double material; 
    }

}
