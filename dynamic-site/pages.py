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
        all = self.page_head + self.body + self.close
        all = all.format(**locals())
        return all

    def page_links(self,li):
        update = li
        for item in update:
            self.body += '<a method="GET" href="#' + item[0] + '"><div><h3>' + item[0] + "</h3><p>" + item[1] + "</p></div></a>"
            #cont">Home</a>"