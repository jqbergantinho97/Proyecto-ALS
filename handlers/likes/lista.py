import webapp2
from webapp2_extras import jinja2
from model.like import Like


class ListaLikesHandler(webapp2.RequestHandler):
    def get(self):
        imagen, likes = Like.recupera_para(self.request)
        usuarios = []
        for like in likes:
            clave_usr = like.usuario
            usuarios.append(clave_usr.get())

        valores_plantilla = {
            "likes": likes,
            "usuarios": usuarios,
            "imagen": imagen,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("lista_likes.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/likes/list', ListaLikesHandler)
], debug=True)