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

run_mad_lib()