
import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.body = "Hello!"
        p.title = "My Page!!!!!"
        p.css = "css/main.css"
        self.response.write(p.whole_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
