class Page(object):
    def __init__(self):
        self.page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        '''
        self.page_div = '''
        <div>Hello</div>'''
        self.page_close = '''
    </body>
</html>
        '''

    def print_page(self):
        all = self.page_head + self.page_div + self.page_close
        all = all.format(**locals())
        return all
