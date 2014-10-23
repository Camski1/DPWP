'''
This class is acting as the template for RecDisp the information is static and is only changed via RecDisp.
'''
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
                <li><a href="?name=home">Home</a></li>
                <li><a href="?name=home">About</a></li>
                <li><a href="?name=home">Find Food</a></li>
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
            <p>FoodSki is all about bringing Polish Cuisine to the foodie world. Polish Cuisine is a style of cooking and food preparation originating in or widely popular in Poland. Polish cuisine has evolved over the centuries to become very eclectic due to Poland's history.</p>
            <p>Polish cuisine shares many similarities with other Slavic countries, especially Belarussian, Ukrainian and Russian cuisines.It has also been widely influenced by Central European cuisines, namely German, Austrian and Hungarian cuisines, as well as Jewish, French and Italian culinary traditions. It is rich in meat, especially pork, chicken and beef (depending on the region) and winter vegetables (cabbage in the dish bigos), and spices. It is also characteristic in its use of various kinds of noodles the most notable of which are kluski as well as cereals such as kasha (from the Polish word kasza).</p>
            <p> Generally speaking, Polish cuisine is hearty and uses a lot of cream and eggs. The traditional dishes are often demanding in preparation. Many Poles allow themselves a generous amount of time to serve and enjoy their festive meals, especially Christmas eve dinner (Wigilia) or Easter breakfast which could take a number of days to prepare in their entirety.</p>
            <img src="img/town.jpg" alt="Small Town in Poland">
        </div>

        '''

        self.close = '''
    </body>
</html>
        '''
    #this is the default display function.
    def print_page(self):
        all = self.page_head + self.body + self.end_left + self.stuff + self.close
        all = all.format(**locals())
        return all

'''
RecDisp is using Page as a template. The dynamic links and displays all work via this class
'''
class RecDisp(Page):
    def __init__(self):
        Page.__init__(self)#this is enabling the Page object in this class

    #this function will display the recipes. The information in resp is coming from the loop in main.
    def page_items(self,resp):
        #this is changing the empty string stuff in the Page class
        self.stuff = '''
        <div class="right">
            <h1>''' + resp.rec_name + '''</h1>
            <p>''' + resp.rec_desc + '''</p>
            <img src="''' + resp.img + '''" alt="Small Town in Poland">
            <ul class="times">
                <li>Prep Time: ''' + str(resp.prep) + '''</li>
                <li>Cook Time: ''' + str(resp.cook) + '''</li>
                <li>Total Time: ''' + str(resp.prep + resp.cook) + '''</li>
            </ul>
            <h2>Ingredients</h2>
            <ul>
                ''' + resp.rec_ingr + '''
            </ul>
            <h2>Directions</h2>
            <ol>
                ''' + resp.directions + '''
            </ol>
        </div>
        '''


    #this is creating the link that you can see on the website. The info in li is coming from the loop in main the finds the name and description. The recipes name is used for both the displayed name and the href name
    def page_links(self,li):
        update = li
        for item in update:
            self.body += '<a href="?name=' + item[0] + '"><div class="links"><h3>' + item[0] + "</h3><p>" + item[1] + "</p></div></a><br/>"

    #this is compiling the page elements and sending them to main.py
    def print_page(self):
        all = self.page_head + self.body + self.end_left + self.stuff + self.close
        all = all.format(**locals())
        return all

