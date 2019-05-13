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
using System.IO;
namespace WebApplication2.Controllers
{
    public class Products1Controller : ApiController
    {
        /*public List<string> PostFileNames(string sc)
        {
            DirectoryInfo y = new DirectoryInfo(@"D:\fyp\asp\sprint 3\finale\WebApplication2 - Copy (7) - Copy\WebApplication2\Content\Content\images\clusters\" + sc);
            FileInfo[] Files = y.GetFiles("*.JPG");
            List<string> files1 = new List<string>();
            foreach (FileInfo file in Files)
            {
                files1.Add(file.ToString());
            }
            return files1;
        }*//*
        [Route("api/products1/{pc}")]
        [ResponseType(typeof(List<string>))]
        public List<string> Get(string pc)
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
    }
}