
import webapp2
from pages import Page
from data import RecData, Bigos, PotatoCakes, Zrazy, Nalesniki, Golumpki

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        rd = RecData()
        bigos = Bigos()
        pc = PotatoCakes()
        zr = Zrazy()
        nal = Nalesniki()
        gol = Golumpki()
        rd.rec_arr[0] = bigos.rec_array
        rd.rec_arr[1] =pc.rec_array
        rd.rec_arr[2] =zr.rec_array
        rd.rec_arr[3] =nal.rec_array
        rd.rec_arr[4] =gol.rec_array
        for item in rd.rec_arr:
            print item[0]
        self.response.write(p.print_page())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
