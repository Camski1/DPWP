
import webapp2
from lib import MovieData
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #movie
        #year
        #director
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.director = "Rob Reiner"
        md1.year = 1989


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
