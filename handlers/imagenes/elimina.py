# coding: utf-8
# Borrar imagen

import webapp2

from model.imagen import Imagen
import time


class BorrarImagenHandler(webapp2.RequestHandler):
    def get(self):
        imagen = Imagen.recupera(self.request)
        imagen.key.delete()
        time.sleep(1)
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/imagen/delete', BorrarImagenHandler)
], debug=True)