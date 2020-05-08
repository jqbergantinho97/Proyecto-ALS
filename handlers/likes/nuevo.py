# coding: utf-8
# Nueva imagen

import webapp2

from webapp2_extras import jinja2
from model.imagen import Imagen
import model.user as mgt_usr
from model.like import Like
from datetime import datetime
from google.appengine.ext import ndb
from google.appengine.api import users
import time


class NuevoLikeHandler(webapp2.RequestHandler):
    def get(self):
        imagen = Imagen.recupera(self.request)

        usr = users.get_current_user()
        url_usr = users.create_logout_url("/")
        usr_info = mgt_usr.retrieve(usr)

        valores_plantilla = {
            "imagen": imagen,
            "usr_info": usr_info,
            "usr": usr,
            "url_usr": url_usr
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nuevo_like.html", **valores_plantilla))

    def post(self):
        imagen = self.request.GET["id"]
        nombre = self.request.get("edNombre", "")
        email = self.request.get("edEmail", "")

        if len(nombre) < 0 or not(nombre) or len(email) < 0 or not(email):
            return self.redirect("/")
        else:
            usr = users.get_current_user()
            user = mgt_usr.retrieve(usr)
            print("EL PRINT ESTA AQUI!!!!!", user.key)

            like = Like(usuario=user.key, imagen=ndb.Key(urlsafe=imagen))
            like.put()
            time.sleep(1)

            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/likes/new_like', NuevoLikeHandler)
], debug=True)