#comment
'''
doc string
'''
first_name = "Cameron"
last_name = "Kozinski"
#response = raw_input("Please enter your name.  ")
#print response
birth_year = 1988
current_year = 2014
age = current_year - birth_year
#print "You are " + str(age) + " years old."
# int(var) to read as a number  str(var) to read as string
'''
if age > 100:
    print "You are doing great for your age!"
elif age > 30:
    print "How old are you? 20?"
else:
    print "You look like a teenager!"
'''
# pass will skip the line

characters = ["Bob", "Tom", "Jen"]
characters.append("Ray")
#print characters[0]

films = dict() #to create an "object"
films = {"Midnight in Paris":"Dali", "Waking Ned Devine":"Ireland"}
#print films["Midnight in Paris"]