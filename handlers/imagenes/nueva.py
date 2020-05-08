# coding: utf-8
# Nueva imagen

import webapp2

from webapp2_extras import jinja2
from model.imagen import Imagen
import time
from google.appengine.api import users
#from model.user import User
import model.user as mgt_usr


class NuevaImagenHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        url_usr = users.create_logout_url("/")
        usr_info = mgt_usr.retrieve(usr)

        valores_plantilla = {
            "usr_info": usr_info,
            "usr": usr_info,
            "url_usr": url_usr
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nueva_imagen.html", **valores_plantilla))

    def post(self):
        str_enlace = self.request.get("edEnlace", "")
        str_titulo = self.request.get("edTitulo", "")

        if len(str_enlace) < 0 or not(str_enlace) and len(str_titulo) < 0 or not(str_titulo):
            return self.redirect("/")
        else:
            imagen = Imagen(enlace=str_enlace, titulo=str_titulo)
            imagen.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/imagenes/new', NuevaImagenHandler)
], debug=True)