
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedi Knight"
        luke.age = 27
        luke.home = "Tattooine"

        leia = Character()
        leia.name = "Princess Leia"
        leia.profession = "Princess"
        leia.age = luke.age
        leia.home = "Alderan"

        yoda = Character()
        yoda.name = "Master Yoda"
        yoda.profession = luke.profession
        yoda.age = 700
        yoda.home = "Dagobah"

        chars = [luke, leia, yoda]
        print chars[1].profession
class Character(object):
    def __init__(self): #construction function
        self.name = ""
        self.profession = ""
        self.age = 0
        self.home = ""
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
