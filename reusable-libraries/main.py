
import webapp2
from lib import MovieData, FavoriteMovies
from pages import ResultsPage
class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = ResultsPage()
        fm = FavoriteMovies()
        #movie
        #year
        #director
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.director = "Rob Reiner"
        md1.year = 1989
        fm.add_movie(md1)

        md2 = MovieData()
        md2.title = "Dune"
        md2.director = "David Lynch"
        md2.year = 1986
        fm.add_movie(md2)

        fm.calc_time()
        p.body = fm.compile_list()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
