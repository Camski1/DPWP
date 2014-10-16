'''
Cameron Kozinski
oct 15th 2014
Design Patterns for Web Programming
Reusable Library
'''
import webapp2
from pages import ResultsPage, FormPage
from lib import UserInfo, UserInfoStr

class MainHandler(webapp2.RequestHandler):
    def get(self):
        uis = UserInfoStr()
        rp = ResultsPage()
        fp = FormPage()
        ui = UserInfo()
        if self.request.GET:
            ui.user_name = self.request.GET['user_name']
            ui.user_quest = self.request.GET['user_quest']
            ui.user_color = self.request.GET['user_color']
            ui.user_location = self.request.GET['user_location']
            ui.sex = self.request.GET['sex']
            ui.user_test = self.request.GET['user_test']
            uis.add_user(ui)
            rp.body = uis.user_output()
            all = rp.page_head + rp.body
            all = all.format(**locals())
            self.response.write(all)
        else:
            self.response.write(fp.form_page_head + fp.page_form)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
