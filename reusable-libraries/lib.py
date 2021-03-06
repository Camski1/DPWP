
class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []

    def add_movie(self, m):
        self.__movie_list.append(m)
        print m.title

    def compile_list(self):
        output = ""
        for movie in self.__movie_list:
           output += "<p>" + "Title: " + movie.title + "</p>" + " (" + str(movie.year) + ") " + " Director: " + movie.director + "<br />"
        return  output

    def calc_time(self):
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)

        years.sort()

        num = len(years) - 1
        span = years[num] - years[0]
        return span





class MovieData(object):
    def __init__(self):
        self.title = ""
        self.__year = 0
        self.director = ""

    @property
    def year(self):
        return  self.__year

    @year.setter
    def year(self, y):
        if y > 2014:
            print "Error, invalid date!"
            self.__year = 2014
        else:
            self.__year = y