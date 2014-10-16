
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