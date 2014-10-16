'''
Cameron Kozinski
oct 15th 2014
Design Patterns for Web Programming
Reusable Library
'''
import webapp2
from pages import ResultsPage, FormPage
from lib import UserInfo, UserInfoStr

'''
This is the main handler that is controlling all of the other class.
All of the information being added to the viewable pages will be added in the class.
'''
class MainHandler(webapp2.RequestHandler):
    def get(self):
        uis = UserInfoStr()#this var holding the user info strings class from the lib file
        rp = ResultsPage()#this is making the result page usable in the main handler
        fp = FormPage()#this is making the form page usable in the main handler
        ui = UserInfo()#this var holding the user info class from the lib file
        if self.request.GET:#this is checking to see if info has been taken from the user
            ui.user_name = self.request.GET['user_name']#all of these vars are the information taken from the user. The information is then sent to the userInfo class
            ui.user_quest = self.request.GET['user_quest']
            ui.user_color = self.request.GET['user_color']
            ui.user_location = self.request.GET['user_location']
            ui.sex = self.request.GET['sex']
            ui.user_test = self.request.GET['user_test']
            uis.add_user(ui)#this is taking the information from the UserInfo and sending it to the UserInfoStr
            rp.body = uis.user_output()#this is taking the info from UserInfoStr and sending it to the results page
            all = rp.page_head + rp.body + rp.close
            all = all.format(**locals())
            self.response.write(all)#this is posting the info to the screen
        else:
            self.response.write(fp.form_page_head + fp.page_form)#this is posting the form to the screen


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
