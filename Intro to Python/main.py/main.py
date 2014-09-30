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

'''
#while loop
i = 0
while i<=9:
    #print "count is", i
    #i = i + 1

#for loop
for i in range(0,10):
    print "count is", i
    i = i + 1
'''
#for each
for c in characters:
    #print c
    pass

#Function in py = def

def calc_area(h, w):
    area = h * w
    return area

a = calc_area(20, 40);
print a

weight = 200
height = 63
message = '''
<!DOCTYPE HTML>
    <head>
    </head>
    <body>
    {height}
    </body>
</html>
'''

message = message.format(**locals())
print message

