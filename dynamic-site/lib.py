

class RecList(object):
    def __init__(self):
        self._rec_names = []

    @property
    def rec_names(self):
        return self._rec_names

    @rec_names.setter
    def rec_names(self, rec):
        self._rec_names = rec

    def print_rec_list(self):
        for item in self._rec_names:
            self._rec_names = item[0]
            print self._rec_names
