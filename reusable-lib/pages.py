
class ResultsPage(object):
    def __init__(self):
        self.page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>You're using coconuts!</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div class="nav">
            <ul>
                <li>Coconuts Beta</li>
                <li>About</li>
                <li>Feature List</li>
            </ul>
        </div>
        <div class="left">
            <div class="friends">
                <h3>Quest Companions</h3>
                <p>1</p>
            </div>

            <div class="find_friends">
                <h3>Find Britons</h3>
            </div>
        </div>
        <img src="img/coconuts.jpg" alt="coconuts">
        '''
        self.body = '''
        '''
        self.close = '''
    </body>
</html>
        '''


class FormPage(object):
    def __init__(self):
        #The page_head var is holding only static information
        self.form_page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Ask me the questions</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <h1>Ask me the questions, bridgekeeper. I am not afraid</h1>
        '''
        self.page_form = '''
        <div class="my_form">
            <form method="GET">
                <label for="name">What... is your name?</label><br>
                <input class="inp_name" type="text" name="user_name" id="name"/><br>

                <label for="quest">What... is your quest?</label><br>
                <textarea id="quest" name="user_quest" rows="7" cols="30"></textarea><br>

                <label for="color">What... is your favorite color?</label><br>
                <input id="color" class="inp_color" type="text" name="user_color" /><br>

                <label for="location">Where are you from?</label><br>
                <input id="location" type="text" name="user_location" /><br>

                <input id="ma-sex" type="radio" name="sex" value="male" checked>
				<label for="ma-sex">Male</label>
				<input id="fe-sex" type="radio" name="sex" value="female">
				<label for="fe-sex">Female</label><br>

				<label for="test">What... is F!VE plus F@UR? (just want to see if you are human)</label><br>
                <input id="test" type="text" name="user_test" /><br>

                <input class="sub_btn" type="submit" value="Submit" />
            </form>
        </div>

    </body>
</html>
        '''
