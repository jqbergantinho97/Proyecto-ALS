from google.appengine.ext import ndb

from usuario import Usuario
from imagen import Imagen

class Like(ndb.Model):
    fecha = ndb.DateTimeProperty(auto_now_add = True)
    usuario = ndb.KeyProperty(kind = Usuario)
    imagen = ndb.KeyProperty(kind = Imagen)