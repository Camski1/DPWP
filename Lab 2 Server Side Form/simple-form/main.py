'''
Cameron Kozinski
oct 7th 2014
Design Patterns for Web Programming
simple form
'''
import webapp2 #use webapp2 library
from pages import Page#importing Page class from pages.py

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        if self.request.GET:
            user_name = self.request.GET['user_name']
            user_email = self.request.GET['user_email']
            all = p.page_head + p.page_form + p.page_review + p.page_close
            all = all.format(**locals())
            self.response.write(all) #print info to page
        else:
            self.response.write(p.page_head + p.page_form + p.page_close) #print info to page


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
