using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace WebApplication2.Controllers
{
    [Authorize]
    public class UsersController : ApiController
    {
        public IEnumerable<User> Get()
        {
            using (fypEntities entities = new fypEntities())
            {
                return entities.Users.ToList();
            }
        }

        public HttpResponseMessage Post([FromBody] User users)
        {
            try
            {
                using (fypEntities entities = new fypEntities())
                {
                    entities.Users.Add(users);
                    entities.SaveChanges();
                    var message = Request.CreateResponse(HttpStatusCode.Created, users);
                    message.Headers.Location = new Uri(Request.RequestUri +
                        users.idUser.ToString());

                    return message;
                }
            }
            catch (Exception ex)
            {
                return Request.CreateErrorResponse(HttpStatusCode.BadRequest, ex);
            }
        }


    }
}
