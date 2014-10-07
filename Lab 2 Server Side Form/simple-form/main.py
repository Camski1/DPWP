'''
Cameron Kozinski
oct 7th 2014
Design Patterns for Web Programming
simple form
'''
import webapp2 #use webapp2 library

class MainHandler(webapp2.RequestHandler):
    def get(self):
       pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
