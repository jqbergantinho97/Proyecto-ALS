import webapp2
from webapp2_extras import jinja2
from model.like import Like
from google.appengine.api import users
import model.user as mgt_usr

class ListaLikesHandler(webapp2.RequestHandler):
    def get(self):
        imagen, likes = Like.recupera_para(self.request)
        usuarios = []

        usr = users.get_current_user()
        url_usr = users.create_logout_url("/")
        usr_info = mgt_usr.retrieve(usr)

        for like in likes:
            clave_usr = like.usuario
            print("EL PRINT ESTA AQUI!!!!!!", like)
            usuarios.append(clave_usr.get())

        valores_plantilla = {
            "likes": likes,
            "usuarios": usuarios,
            "imagen": imagen,
            "usr_info": usr_info,
            "usr": usr_info,
            "url_usr": url_usr
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("lista_likes.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/likes/list', ListaLikesHandler)
], debug=True)