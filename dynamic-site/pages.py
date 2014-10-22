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
        self.stuff = '''

        '''

        self.close = '''
    </body>
</html>
        '''

    def print_page(self):
        all = self.page_head + self.body + self.stuff + self.close
        all = all.format(**locals())
        return all


class RecDisp(Page):
    def __init__(self):
        Page.__init__(self)

    def page_items(self,resp):
        self.stuff = '<p>' + resp.rec_name + resp.rec_name + resp.rec_name +'</p>'

    def page_links(self,li):
        update = li
        for item in update:
            self.body += '<a method="GET" href="?name=' + item[0] + '"><div class="links"><h3>' + item[0] + "</h3><p>" + item[1] + "</p></div></a><br/>"
            #cont">Home</a>"

    def print_page(self):
        all = self.page_head + self.body + self.stuff + self.close
        all = all.format(**locals())
        return all

