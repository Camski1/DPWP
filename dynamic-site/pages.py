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
        <div class="nav">
            <ul>
                <li>Home</li>
                <li>About</li>
                <li>Find Food</li>
            </ul>
        </div>

        <div class = "left">
        '''
        self.body = '''

        '''
        self.end_left = '''
        </div>
        '''
        self.stuff = '''
            <div class="about">
            <h1>A little about FoodSki</h1>
            <p>FoodSki is all about bringing Polish Cuisine to the foodie world. Polish Cuisine is a style of cooking and food preparation originating in or widely popular in Poland. Polish cuisine has evolved over the centuries to become very eclectic due to Poland's history. Polish cuisine shares many similarities with other Slavic countries, especially Belarussian, Ukrainian and Russian cuisines.It has also been widely influenced by Central European cuisines, namely German, Austrian and Hungarian cuisines, as well as Jewish, French and Italian culinary traditions. It is rich in meat, especially pork, chicken and beef (depending on the region) and winter vegetables (cabbage in the dish bigos), and spices. It is also characteristic in its use of various kinds of noodles the most notable of which are kluski as well as cereals such as kasha (from the Polish word kasza). Generally speaking, Polish cuisine is hearty and uses a lot of cream and eggs. The traditional dishes are often demanding in preparation. Many Poles allow themselves a generous amount of time to serve and enjoy their festive meals, especially Christmas eve dinner (Wigilia) or Easter breakfast which could take a number of days to prepare in their entirety.</p>
            <img src="img/town.jpg" alt="Small Town in Poland">
        </div>

        '''

        self.close = '''
    </body>
</html>
        '''

    def print_page(self):
        all = self.page_head + self.body + self.end_left + self.stuff + self.close
        all = all.format(**locals())
        return all


class RecDisp(Page):
    def __init__(self):
        Page.__init__(self)


    def page_items(self,resp):

        self.stuff = '''
        <div class="right">
            <h1>''' + resp.rec_name + '''</h1>
            <p>''' + resp.rec_desc + '''</p>
            <img src="''' + resp.img + '''" alt="Small Town in Poland">
            <h2>Ingredients</h2>
            <ul>'''
        self.stuff_ingr = '''
        '''
        self.stuff_close = '''
            <ul>
        </div>
        '''



    def page_links(self,li):
        update = li
        for item in update:
            self.body += '<a method="GET" href="?name=' + item[0] + '"><div class="links"><h3>' + item[0] + "</h3><p>" + item[1] + "</p></div></a><br/>"
            #cont">Home</a>"

    def print_page(self):
        all = self.page_head + self.body + self.end_left + self.stuff + self.close
        all = all.format(**locals())
        return all

