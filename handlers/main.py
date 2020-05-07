#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
from model.imagen import Imagen
from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            imagenes = Imagen.query().order(Imagen.fecha)

            valores_plantilla = {
                "imagenes": imagenes,
                "usuario": user
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("index.html", **valores_plantilla))
        else:
            login_url = users.create_login_url("/")
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
            self.response.write("<html><body>{}</body></html>".format(greeting))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
