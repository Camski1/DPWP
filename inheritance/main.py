
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [ ['first_name', 'text','First Name'], ['last_name', 'text','Last Name'], ['submit', 'Submit'] ]
        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self._head = '''
<DOCTYPE HTML>
<html>
    <head>
    <title>Sup</title>
    </head>
    <body>
        '''
        self._body = "Hello"
        self._close = '''
    </body>
</html>
        '''
    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        Page.__init__(self)
        self._form_open = '<form method="GET">'
        self.form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:
            self._form_inputs += '<input type="' +item[1] + '" name="' + item[0]
            try:
                self._form_inputs += '" placeholder="' + item[2] + '"/><br/>'
            except:
                self._form_inputs += '"/><br/>'
        print self._form_inputs
    #Poly
    def print_out(self):
       return self._head + self._body + self._form_open + self._form_inputs + self.form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
