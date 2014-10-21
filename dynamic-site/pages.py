class Page(object):
    def __init__(self):
        self.page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>FoodSki</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        '''
        self.body = '''
        '''
        self.close = '''
    </body>
</html>
        '''
    def print_page(self):
        return self.page_head + self.body + self.close