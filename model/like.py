from google.appengine.ext import ndb

from usuario import Usuario
from imagen import Imagen
from webapp2_extras.users import users

class Like(ndb.Model):
    fecha = ndb.DateTimeProperty(auto_now_add=True)
    usuario = ndb.KeyProperty(kind=users)
    imagen = ndb.KeyProperty(kind=Imagen)

    @staticmethod
    def recupera_para(req):
        try:
            id_img = req.GET["img"]
        except KeyError:
            id_img = ""

        if id_img:
            clave_img = ndb.Key(urlsafe = id_img)
            imagenes = Imagen.query(Like.imagen == clave_img)

            return clave_img.get(), imagenes
        else:
            print("ERROR: imagen no encontrada")