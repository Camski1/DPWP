

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_button.label = "About US"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Label"
        contact_button.show_label()

class Button(object):
    def __init__(self):
        print "constructor method BTN"
        self.label = "" #public
        self.__size = 60 #private
        self._color = "fff" #protected
        #self.click()
        #self.on_roll_over("Hello")

    def click(self):
        print  "click"

    def on_roll_over(self, message):
        print  "roll over" + message

    def show_label(self):
        print "my label is " + self.label


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
