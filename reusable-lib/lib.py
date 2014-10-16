
class UserInfoStr(object):
    def __init__(self):
        self.__user_arr = []

    def add_user(self, u):
        self.__user_arr.append(u)
        if u.sex == "female":
            u.user_name = "Sister " + u.user_name + " of " + u.user_location
        else:
            u.user_name = "Sir. " + u.user_name + " of " + u.user_location

        print u.user_name

    def user_output(self):
        output = ""
        for user in self.__user_arr:
            if user.user_test == str(5 + 4):
                output += '''
        <div class='about'>
            <h1>{user.user_name}</h1>
            <h2> My Favorite color is: {user.user_color} </h2>
            <div class='quest'>
                <p> My Quest is:<br /> {user.user_quest}</p>
            </div>
        </div>
                '''
                return output.format(**locals())
            else:
                output = '''<div class='error'><h1>Your mother was a hamster and your father smelt of elderberries</h1></div>'''
                return output


class UserInfo(object):
    def __init__(self):
        self.__user_name = ""
        self.__user_quest = ""
        self.__user_color = ""
        self.__user_location = ""
        self.__sex = ""
        self.user_test = ""


    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, n):
        self.__user_name = n
        ###

    @property
    def user_quest(self):
        return self.__user_quest

    @user_quest.setter
    def user_quest(self, q):
        self.__user_quest = q
        ###

    @property
    def user_color(self):
        return self.__user_color

    @user_color.setter
    def user_color(self, c):
        self.__user_color = c
        ###

    @property
    def user_location(self):
        return self.__user_location

    @user_location.setter
    def user_location(self, l):
        self.__user_location = l
        ###

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, s):
        self.__sex = s
        ###