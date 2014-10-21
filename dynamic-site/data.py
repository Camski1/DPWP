class RecData(object):
    def __init__(self):
        self.rec_arr = [[],[],[]]

class Bigos(RecData):
    def __init__(self):
        RecData.__init__(self)
        self.rec_name = "Bigos"
        self.rec_desc = "Bigos is a stewed dish made from cabbage as a main ingredient. Fresh cabbage can be used as well as the soured one, called sauerkraut. Hence, more than one kind of bigos exists in the Polish cuisine."
        self.rec_ingr = ["2 thick slices hickory-smoked bacon", "1 pound kielbasa sausage sliced into 1/2 inch pieces", "1 pound cubed pork stew meat", "1/4 cup all-purpose flour", "3 cloves garlic, chopped", "1 onion, diced", "2 carrots, diced", "1 1/2 cups sliced fresh mushrooms", "4 cups shredded green cabbage", "1 (16 ounce) jar sauerkraut, rinsed and well drained", "1/4 cup dry red wine", "1 bay leaf", "1 teaspoon dried basil", "1 teaspoon dried marjoram", "1 tablespoon sweet paprika", "1/4 teaspoon salt", "1/8 teaspoon ground black pepper", "1/8 teaspoon caraway seed, crushed", "1 pinch cayenne pepper", "1/2 ounce dried mushrooms", "1 dash bottled hot pepper sauce", "1 dash Worcestershire sauce", "5 cups beef stock", "2 tablespoons canned tomato paste", "1 cup canned diced tomatoes"]
        self.directions = ["Preheat the oven to 350 degrees F (175 degrees C).", "Coat the cubes of pork lightly with flour and fry them in the bacon drippings over medium-high heat until golden brown. Use a slotted spoon to transfer the pork to the casserole. Add the garlic, onion, carrots, fresh mushrooms, cabbage and sauerkraut. Reduce heat to medium; cook and stir until the carrots are soft, about 10 minutes. Do not let the vegetables brown.", "Deglaze the pan by pouring in the red wine and stirring to loosen all of the bits of food and flour that are stuck to the bottom. Season with the bay leaf, basil, marjoram, paprika, salt, pepper, caraway seeds and cayenne pepper; cook for 1 minute.", "Mix in the dried mushrooms, hot pepper sauce, Worcestershire sauce, beef stock, tomato paste and tomatoes. Heat through just until boiling. Pour the vegetables and all of the liquid into the casserole dish with the meat. Cover with a lid.", "Bake in the preheated oven for 2 1/2 to 3 hours, until meat is very tender."]

        self.rec_array = [self.rec_name, self.rec_desc, self.rec_ingr, self.directions]





class PotatoCakes(RecData):
    def __init__(self):
        RecData.__init__(self)
        self.rec_name = "Placki Ziemniaczane"
        self.rec_desc = "lacki ziemniaczane is a Polish name for a quite well-known, simple and good food made from grated potatoes fried in a fat."
        self.rec_ingr = ["4-5 large potatoes, peeled and grated", "1 large onion", "3-4 minced garlic cloves", "2 eggs", "4 tbsp flour ", "1/2 teaspoon marjoram", "1/2 teaspoon salt (minimum)", "Freshly ground black pepper"]
        self.directions = ["Using a food processor or hand shredder, grate potatoes and onion using the finest grader.  The finer the potatoes are grated, the better because it is easier to cook.  If you grate the potatoes in larger chunks, you will just have to cook longer and use a little bit more oil for taste.", "Squeeze potatoes and onions with hands to remove excess liquid", "Put grated potatoes and onion in a large bowl and mix with eggs, garlic, flour, marjoram, salt, and pepper.", "Heat oil in large frying pan until almost smoking.  Carefully put a large spoonful of the potato mixture into the pan and flatten with a fork.  Repeat until you have 3-4 pancakes in the pan. Fry each pancake until it is golden brown on both sides.  Remove with spatula and drain on a paper towel.", "Serve potato pancakes warm with topping of choice."]

        self.rec_array = [self.rec_name, self.rec_desc, self.rec_ingr, self.directions]


class Zrazy(RecData):
    def __init__(self):
        RecData.__init__(self)
        self.rec_name = "Zrazy"
        self.rec_desc = "lacki ziemniaczane is a Polish name for a quite well-known, simple and good food made from grated potatoes fried in a fat."
        self.rec_ingr = ["4-5 large potatoes, peeled and grated", "1 large onion", "3-4 minced garlic cloves", "2 eggs", "4 tbsp flour ", "1/2 teaspoon marjoram", "1/2 teaspoon salt (minimum)", "Freshly ground black pepper"]
        self.directions = ["Using a food processor or hand shredder, grate potatoes and onion using the finest grader.  The finer the potatoes are grated, the better because it is easier to cook.  If you grate the potatoes in larger chunks, you will just have to cook longer and use a little bit more oil for taste.", "Squeeze potatoes and onions with hands to remove excess liquid", "Put grated potatoes and onion in a large bowl and mix with eggs, garlic, flour, marjoram, salt, and pepper.", "Heat oil in large frying pan until almost smoking.  Carefully put a large spoonful of the potato mixture into the pan and flatten with a fork.  Repeat until you have 3-4 pancakes in the pan. Fry each pancake until it is golden brown on both sides.  Remove with spatula and drain on a paper towel.", "Serve potato pancakes warm with topping of choice."]

        self.rec_array = [self.rec_name, self.rec_desc, self.rec_ingr, self.directions]
