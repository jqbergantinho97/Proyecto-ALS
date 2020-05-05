from google.appengine.ext import ndb


class Usuario(ndb.Model):
    nombre = ndb.StringProperty()
    apellidos = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    fecha_nacimiento = ndb.DateProperty(required = True)