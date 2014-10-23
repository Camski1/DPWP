'''
Cameron Kozinski
oct 22nd 2014
Design Patterns for Web Programming
Dynamic Site
'''
import webapp2
from pages import Page, RecDisp #this is importing the classes from pages.py
from data import RecData, Bigos, PotatoCakes, Zrazy, Nalesniki, Golumpki #this is importing the classes from data.py

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #the 7 vars bellow are calling the classes
        rd = RecData()
        bigos = Bigos()
        pc = PotatoCakes()
        zr = Zrazy()
        nal = Nalesniki()
        gol = Golumpki()
        rdp = RecDisp()
        #the 5 transfers bellow are moving information into the RecData array
        rd._rec_arr[0] = bigos.rec_array
        rd._rec_arr[1] = pc.rec_array
        rd._rec_arr[2] = zr.rec_array
        rd._rec_arr[3] = nal.rec_array
        rd._rec_arr[4] = gol.rec_array
        #this loop is sending the name and description of each item in RecData pages.py to make the links
        for item in rd._rec_arr:
            rdp.page_links([[item[0], item[1]]])
        #The ifs are finding if the user has clicked on a link. If not it will show the home page, if so it will recognize the name and move data as needed
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
