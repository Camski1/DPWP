
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #movie
        #year
        #director
        pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
