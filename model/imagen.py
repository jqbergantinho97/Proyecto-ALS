from google.appengine.ext import ndb


class Imagen(ndb.Model):
    id = ndb.IntegerProperty(indexed = True)
    enlace = ndb.StringProperty(required = True)
    fecha = ndb.DateTimeProperty(auto_now_add = True)