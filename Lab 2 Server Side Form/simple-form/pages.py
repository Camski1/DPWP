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
        self.page_form = '''
        <div>
            <form method="GET">
            <label>Full Name:</label><br>
            <input type="text" name="user_name" /><br>

            <label>Email:</label><br>
            <input type="email" name="user_email" /><br>

            <input type="submit" value="Submit" />
            </form>
        </div>'''
        self.page_review = '''
        <div>
            <p>{user_name}</p>
        </div>'''
        self.page_close = '''
    </body>
</html>
        '''


        def print_out(self):
            all = self.page_head + self.page_form + self.page_review + self.page_close
            all = all.format(**locals())
            return all