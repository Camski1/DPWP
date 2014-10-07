'''
Cameron Kozinski
oct 7th 2014
Design Patterns for Web Programming
simple form
'''
import webapp2 #use webapp2 library
from pages import Page #importing Page class from pages.py

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(Page().print_page())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
