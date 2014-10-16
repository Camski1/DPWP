'''
This class is holding all of the info for the results page
'''
class ResultsPage(object):
    def __init__(self):
        #tpage_head is holding all static information
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
                <h3>Quest Companions... 1</h3>
            </div>

            <div class="find_friends">
                <h3>Find Britons</h3>
            </div>
            <img src="img/god.jpg" alt="god">
        </div>
        <div class="profile">
            <img src="img/coconuts.jpg" alt="coconuts">
        </div>
        '''
        #body is an empty string for all user input data
        self.body = '''
        '''
        #close is holding all static information
        self.close = '''
        <div class="comment">
            <img src="img/coconuts.jpg" alt="coconuts">
            <form method="GET">
                <label for="comment">Whats on your mind??</label><br>
                <textarea id="comment" name="user_comment" rows="7" cols="60"></textarea><br>
                <input class="sub_btn" type="button" value="Post" />
            </form>
        </div>
    </body>
</html>
        '''

'''
This class is holding all of the info for the form page. The form is taking six kinds
of info from the user.
'''
class FormPage(object):
    def __init__(self):
        #The page_head var is holding only static information.
        self.form_page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Ask me the questions</title>
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
        <div class="form_head">
            <h1>Ask me the questions, bridgekeeper. I am not afraid</h1>
        </div>
        '''
        self.page_form = '''
        <div class="my_form">
            <form method="GET">
                <label for="name">What... is your name?</label><br>
                <input class="imps" type="text" name="user_name" id="name"/><br>

                <label for="quest">What... is your quest?</label><br>
                <textarea id="quest" name="user_quest" rows="7" cols="59"></textarea><br>

                <label for="color">What... is your favorite color?</label><br>
                <input id="color" class="imps" type="text" name="user_color" /><br>

                <label for="location">Where are you from?</label><br>
                <input class="imps" id="location" type="text" name="user_location" /><br>

                <input class="gen" id="ma-sex" type="radio" name="sex" value="male" checked>
				<label for="ma-sex">Male</label>
				<input class="gen" id="fe-sex" type="radio" name="sex" value="female">
				<label for="fe-sex">Female</label><br>

				<label for="test">What... is F!VE plus F@UR? (just want to see if you are human)</label><br>
                <input id="test" type="text" name="user_test" /><br>

                <input class="sub_btn" type="submit" value="Submit" />
            </form>
        </div>
        <div class="info">
            <img src="img/god.jpg" alt="god">
            <h2>A little about Coconuts</h2>
            <p>Bloody Peasant! Knights of Ni, we are but simple travelers who seek the enchanter who lives beyond these woods. Knights of Ni, we are but simple travelers who seek the enchanter who lives beyond these woods.</p>
            <p>We found them. She looks like one. I have to push the pram a lot. Oh! Come and see the violence inherent in the system! Help, help, I'm being repressed! Did you dress her up like this? I dunno. Must be a king.</p>
        </div>
    </body>
</html>
        '''
