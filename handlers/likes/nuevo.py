# coding: utf-8
# Nueva imagen

import webapp2

from webapp2_extras import jinja2
from model.imagen import Imagen
from model.usuario import Usuario
from model.like import Like
from datetime import datetime
from google.appengine.ext import ndb
import time


class NuevoLikeHandler(webapp2.RequestHandler):
    def get(self):
        imagen = Imagen.recupera(self.request)
        valores_plantilla = {
            "imagen": imagen
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nuevo_like.html", **valores_plantilla))

    def post(self):
        imagen = self.request.GET["id"]
        nombre = self.request.get("edNombre", "")
        apellidos = self.request.get("edApellidos", "")
        email = self.request.get("edEmail", "")
        fecha_nacimiento = self.request.get("edFecha", "")

        if len(nombre) < 0 or not(nombre) or len(apellidos) < 0 or not(apellidos) or len(email) < 0 or not(email) or len(fecha_nacimiento) < 0 or not(fecha_nacimiento):
            return self.redirect("/")
        else:
            fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
            usuario = Usuario(nombre=nombre, apellidos=apellidos, email=email, fecha_nacimiento=fecha)
            usuario.put()
            like = Like(usuario=usuario.key, imagen=ndb.Key(urlsafe=imagen))
            like.put()
            time.sleep(1)

            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/likes/new_like', NuevoLikeHandler)
], debug=True)