'''
This function will hold the entire program
'''

def run_mad_lib():
    #alert the user that I will be asking questions
    print "Hello, I just need some info to create your Mad Lib. Please answer all of the questions."
    #info that will be taken from the user
    user_name = raw_input("Please enter your name.  ")# str
    user_age = raw_input("Please enter your age.  ")# int
    user_book = raw_input("Please enter the name of your favorite book.  ")#str
    user_fav_num = raw_input("Please enter your lucky number.  ")# int
    user_bike = raw_input("Please enter the age you learned to ride a bike.  ")# int
    user_sex = raw_input("Are you a boy or a girl?  ")#str
    print user_name

    user_ints = [int(user_age), int(user_fav_num), int(user_bike)]
    user_strs = dict()
    user_strs = {"name":user_name, "book":user_book, "sex":user_sex}

    '''
    This function will find the year the story is in. The function will take age of the user * the year the user learned
    to ride a bike to find the year.
    '''
    def year(num1, num2):
        story_year = num1 * num2
        return story_year
    story_year = year(user_ints[0], user_ints[2])

    #this loop will find the number of kills our hero has
    i = 0
    while i<=user_ints[1]:
        kills = i + user_ints[1]
        i = i + 1

    '''
    This function will compile the information that will write the story.
    '''

    def story(name, year, kills, book, age):
        if user_strs["sex"] == "girl": #if statement will find the sex of the user
            if user_ints[0] > 60: #if statement will see if the user is older then 60
                message = '''
Our brave Hero {name} was thought at the age of {age} to be out of her prime but she is about to show everyone she still has it. Today is the {year} year anniversary of the end of the Ebola outbreak that killed {kills} million people. {name} is sitting in her study reading {book} not knowing that her retirement from the CIA was about to come to an end.
For Full Ebook click link!
'''
                message = message.format(**locals())
                print message
            else:
                message = '''
Our brave Hero {name} was thought at the age of {age} to be in her prime and she is about to prove them all right. Today is the {year} year anniversary of the end of the Ebola outbreak that killed {kills} million people. {name} is sitting in her barracks reading {book} not knowing that she is about to be called upon by the CIA.
For Full Ebook click link!
'''
                message = message.format(**locals())
                print message
        else:
            if user_ints[0] > 60:
                message = '''
Our brave Hero {name} was thought at the age of {age} to be out of his prime but he is about to show everyone he still has it. Today is the {year} year anniversary of the end of the Ebola outbreak that killed {kills} million people. {name} is sitting in his study reading {book} not knowing that his retirement from the CIA was about to come to an end.
For Full Ebook click link!
'''
                message = message.format(**locals())
                print message
            else:
                message = '''
Our brave Hero {name} was thought at the age of {age} to be in his prime and he is about to prove them all right. Today is the {year} year anniversary of the end of the Ebola outbreak that killed {kills} million people. {name} is sitting in his barracks reading {book} not knowing that he is about to be called upon by the CIA.
For Full Ebook click link!
'''
                message = message.format(**locals())
                print message

    #this is calling the story function and adding the needed info
    story(user_strs["name"], story_year, kills, user_strs["book"], user_ints[0])
#calling the container function
run_mad_lib()