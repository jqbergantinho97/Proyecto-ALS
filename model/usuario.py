from google.appengine.ext import ndb


class Usuario(ndb.Model):
    nombre = ndb.StringProperty(required=True)
    apellidos = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    fecha_nacimiento = ndb.DateProperty(required=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()