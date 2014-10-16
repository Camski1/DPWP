'''
Cameron Kozinski
oct 15th 2014
Design Patterns for Web Programming
Reusable Library
'''
import webapp2
from pages import ResultsPage, FormPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        rp = ResultsPage()
        fp = FormPage()
        self.response.write(fp.form_page_head + fp.page_form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
