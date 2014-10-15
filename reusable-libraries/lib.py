class MovieData(object):
    def __init__(self):
        self.title = ""
        self.__year = 0
        self.director = ""

    @property
    def year(self):
        pass

    @year.setter
    def year(self, y):
        if y > 2014:
            print "Error, invalid date!"
            self.__year = 2014
        else:
            self.__year = y