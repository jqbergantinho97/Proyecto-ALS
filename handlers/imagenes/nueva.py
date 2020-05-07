# coding: utf-8
# Nueva imagen

import webapp2

from webapp2_extras import jinja2
from model.imagen import Imagen
import time


class NuevaImagenHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
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