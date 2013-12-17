from __future__ import division
import webapp2, jinja2, os, urllib, myFunctions #, scipy
from math import *
from google.appengine.api import users
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

DEFAULT_NAMESPACE_NAME = 'default_namespace'

def namespace_key(namespace_name=DEFAULT_NAMESPACE_NAME):
    return ndb.Key('Namespace', namespace_name)

class Variable(ndb.Model):
    name = ndb.StringProperty('name', indexed=True)
    value = ndb.GenericProperty('value', indexed=False)


def calculator(expression, user_nickname):
    try:
        return eval(expression)
    except SyntaxError:
        if "=" in expression:
            curr_variable_query = Variable.query(Variable.name == expression[:expression.index("=")].strip(), ancestor=namespace_key("namespace_of_" + user_nickname))
            try:
                curr_variable = curr_variable_query.fetch(1)[0]
                curr_variable.value = calculator(expression[expression.index("=") + 1:].strip(), user_nickname)
                curr_variable.put()
                return curr_variable.value
            except IndexError, e:
                curr_variable = Variable(parent=namespace_key("namespace_of_" + user_nickname))
                if calculator(expression[expression.index("=") + 1:], user_nickname) != "Undefined Variable Found":
                    temp_expression = expression[:expression.index("=")].strip()
                    if " " in temp_expression or "   " in temp_expression:
                        return "Unexpected White Space Found"
                    else:
                        curr_variable.name = expression[:expression.index("=")].strip()
                        curr_variable.value = calculator(expression[expression.index("=") + 1:], user_nickname)
                        curr_variable.put()
                        return curr_variable.value
                else:
                    return "Undefined Variable Found"
        else:
            return "Invalid Expression"
    except NameError, error:
        error = str(error)
        curr_variable_query = Variable.query(Variable.name == error.split("'")[1], ancestor=namespace_key("namespace_of_" + user_nickname))
        try:
            curr_variable = curr_variable_query.fetch(1)[0]
            expression = expression.replace(error.split("'")[1], "(" + str(curr_variable.value) + ")")
            return calculator(expression, user_nickname)
        except IndexError, e:
            return "Undefined Variable Found"

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
    	   template_values = {
    	       'name': user.nickname(),
               'logout':users.create_logout_url(self.request.uri)
            }
    	   template = JINJA_ENVIRONMENT.get_template('index.html')
           self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def post(self):
        user = users.get_current_user()
    	expression = self.request.get('expression')
        results = calculator(urllib.unquote(expression), user.nickname())
        self.response.write(results)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)