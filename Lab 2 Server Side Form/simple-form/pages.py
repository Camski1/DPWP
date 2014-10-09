'''
This class is holding all of the information needed to write the html page
'''
class Page(object):
    def __init__(self):
        #The page_head var is holding only static information
        self.page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>

        <div class="head">
            <h1>I Love Forms</h1>
            <h2>A site for people that love forms!</h2>
        </div>
        <div class="about">
            <h3>A little about I Love Forms</h3>
            <p> Various Characters: [Repeated throughout the series] Oh my Gods!
                Doctor Gaius Baltar: [after Baltar walks in on Boomer trying to commit suicide] Sometimes we must embrace that which opens up to us.  Lt. Sharon 'Boomer' Valerii: Embrace?  Doctor Gaius Baltar: Life can be a curse, as well as a blessing. You will believe me when I say that there are far worse things than death in this world.  Lt. Sharon 'Boomer' Valerii: So what you're saying is...  Doctor Gaius Baltar: No, no. What I'm saying means nothing. Listen to your heart. Do that which you truly believe to be right.  [he kisses her on the forehead and walks out of the room, while he's walking down the hall he hears a gun fire]
                Commander William Adama: I gave the order, Son. It was my responsibility.  Captain Lee 'Apollo' Adama: I pulled the trigger. That's mine.
                Col. Saul Tigh: I can't believe you sided with that woman against the Old Man, I wouldn't do that if you put a gun to my head, and you did! As far as I'm concerned you're not fit to wear the uniform.  Captain Lee 'Apollo' Adama: Yeah, you're right about that part, I am not fit to wear the uniform.  [pause]  Captain Lee 'Apollo' Adama: And maybe I never was. Then again neither are you.  [turns to Tigh]  Captain Lee 'Apollo' Adama: But this isn't my ship, it sure as hell isn't yours. It's his, and when he wakes up, he'll decide what to do with the both of us.  [leaves sickbay to return to his cell]
                Col. Saul Tigh: I can't believe you sided with that woman against the Old Man, I wouldn't do that if you put a gun to my head, and you did! As far as I'm concerned you're not fit to wear the uniform.  Captain Lee 'Apollo' Adama: Yeah, you're right about that part, I am not fit to wear the uniform.  [pause]  Captain Lee 'Apollo' Adama: And maybe I never was. Then again neither are you.  [turns to Tigh]  Captain Lee 'Apollo' Adama: But this isn't my ship, it sure as hell isn't yours. It's his, and when he wakes up, he'll decide what to do with the both of us.  [leaves sickbay to return to his cell]
            </p>
            <p>Become a member today!</p>
        </div>
        '''
        #The page_form var is holding the form that will be displayed when the user first runs the page
        self.page_form = '''
        <div class="my_form">
            <h3>Please fill out form</h3>
            <form method="GET">
                <label>Full Name:</label><br>
                <input class="inp_name" type="text" name="user_name" /><br>

                <label>Email:</label><br>
                <input class="inp_email" type="email" name="user_email" /><br>

                <label>What is your favorite color?</label><br>
                <input class="inp_color" type="text" name="user_color" /><br>

                <label>What Continent do you live on?</label><br>
                <select name="user_cont">
                    <option>Asia</option>
                    <option>Africa</option>
                    <option>North America</option>
                    <option>South America</option>
                    <option>Antarctica</option>
                    <option>Europe</option>
                    <option>Australia</option>
                </select><br>

                <label>What is your preferences for newsletter? Select one.</label><br>
                <input id="news" name="user_news" type='checkbox' value="Monthly" />
				<label for="news">Monthly.</label>
				<input id="news" name="user_news" type='checkbox' value="Bi-Weekly" />
				<label for="news">Bi-Weekly.</label>
                <input id="news" name="user_news" type='checkbox' value="Weekly"/>
				<label for="news">Weekly.</label><br>

                <input class="sub_btn" type="submit" value="Submit" />
            </form>
        </div>'''
        #the page_review var will display after the user has filled out the form, and display all of the imputed info to be checked by the user
        self.page_review = '''
        <div class="page_rev">
            <h3>Is the information correct?</h3>
            <p>Your name: {user_name}</p>
            <p>Your Email: {user_email}</p>
            <p>Your favorite color is: {user_color}</p>
            <p>Your current continent: {user_cont}</p>
            <p>Newsletter Preference: {user_news}</p>
            <button id="btn1" type="button">Cancel</button>
			<button id="btn2"type="button">Save</button>
        </div>'''
        #page_close is holding closing tags and static information
        self.page_close = '''
        <div class="footer">
            <ul>
                <li>Home</li>
                <li>Forms</li>
                <li>About</li>
                <li>Contact</li>
            </ul>
        </div>
    </body>
</html>
        '''


