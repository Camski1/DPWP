class ResultsPage(object):
    def __init__(self):
        self.__title = "Welcome"
        self.css = "css/main.css"
        self.__head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Sup</title>
    </head>
</html>
    <body>
                '''
        self.__body = ""
        self.__error = ""
        self.__close = '''
    </body>
</html>
                '''

    def print_out(self):
        all = self.__title + self.__head + self.__body + self.__error + self.__close
        return all
