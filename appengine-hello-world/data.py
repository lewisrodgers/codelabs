import webapp2

from google.appengine.ext import ndb
# from google.appengine.api import users


class User(ndb.Model):
    firstname = ndb.StringProperty()
    lastname = ndb.StringProperty()
    role = ndb.StringProperty()


class PutData(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        user = User(firstname='Lewis',lastname='Rodgers',role='Admin')
        user.put()


put = webapp2.WSGIApplication([
    ('/data', PutData),
], debug=True)
