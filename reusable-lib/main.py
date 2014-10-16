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
        if self.request.GET:
            user_name = self.request.GET['user_name']
            user_quest = self.request.GET['user_quest']
            user_color = self.request.GET['user_color']
            user_location = self.request.GET['user_location']
            sex = self.request.GET['sex']
            user_test = self.request.GET['user_test']
            all = rp.page_head
            all = all.format(**locals())
            self.response.write(all)
        else:
            self.response.write(fp.form_page_head + fp.page_form)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
