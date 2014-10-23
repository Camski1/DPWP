
import webapp2
from pages import Page, RecDisp
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
        rdp = RecDisp()
        rd.rec_arr[0] = bigos.rec_array
        rd.rec_arr[1] = pc.rec_array
        rd.rec_arr[2] = zr.rec_array
        rd.rec_arr[3] = nal.rec_array
        rd.rec_arr[4] = gol.rec_array
        for item in rd.rec_arr:
            rdp.page_links([[item[0], item[1]]])
        if self.request.GET:
            name = self.request.GET['name']
            if name == 'Bigos':
                rdp.page_items(bigos)
                print "YES"
                self.response.write(rdp.print_page())
            elif name == "Placki Ziemniaczane":
                rdp.page_items(pc)
                print "YES"
                self.response.write(rdp.print_page())
            elif name == "Zrazy":
                rdp.page_items(zr)
                print "YES"
                self.response.write(rdp.print_page())
            elif name == "Nalesniki":
                rdp.page_items(nal)
                print "YES"
                self.response.write(rdp.print_page())
            elif name == "Golumpki":
                rdp.page_items(gol)
                print "YES"
                self.response.write(rdp.print_page())
            else:
                print "YES"
                self.response.write(rdp.print_page())
        else:
            self.response.write(rdp.print_page())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
