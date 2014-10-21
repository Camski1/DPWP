class RecData(object):
    def __init__(self):
        self._res_arr = []

class RecDataObject(object):
    def __init__(self):
        self.recp_name = ""
        self.resp_description = ""
        self.ingredients = []
        self.directions = []

class Bigos(RecDataObject):
    def __init__(self):
        RecDataObject.__init__()
        self.rec_name = "Bigos"
        self.rec_desc = "Bigos is a stewed dish made from cabbage as a main ingredient. Fresh cabbage can be used as well as the soured one, called sauerkraut. Hence, more than one kind of bigos exists in the Polish cuisine."
        self.rec_ingr = ["2 thick slices hickory-smoked bacon", "1 pound kielbasa sausage, sliced into 1/2 inch pieces", "1 pound cubed pork stew meat", "1/4 cup all-purpose flour", "3 cloves garlic, chopped", "1 onion, diced", "2 carrots, diced", "1 1/2 cups sliced fresh mushrooms", "4 cups shredded green cabbage", "1 (16 ounce) jar sauerkraut, rinsed and well drained", "1/4 cup dry red wine", "1 bay leaf", "1 teaspoon dried basil", "1 teaspoon dried marjoram", "1 tablespoon sweet paprika", "1/4 teaspoon salt", "1/8 teaspoon ground black pepper", "1/8 teaspoon caraway seed, crushed", "1 pinch cayenne pepper", "1/2 ounce dried mushrooms", "1 dash bottled hot pepper sauce", "1 dash Worcestershire sauce", "5 cups beef stock", "2 tablespoons canned tomato paste", "1 cup canned diced tomatoes"]
        self.directions = ["Preheat the oven to 350 degrees F (175 degrees C).", "Coat the cubes of pork lightly with flour and fry them in the bacon drippings over medium-high heat until golden brown. Use a slotted spoon to transfer the pork to the casserole. Add the garlic, onion, carrots, fresh mushrooms, cabbage and sauerkraut. Reduce heat to medium; cook and stir until the carrots are soft, about 10 minutes. Do not let the vegetables brown.", "Deglaze the pan by pouring in the red wine and stirring to loosen all of the bits of food and flour that are stuck to the bottom. Season with the bay leaf, basil, marjoram, paprika, salt, pepper, caraway seeds and cayenne pepper; cook for 1 minute.", "Mix in the dried mushrooms, hot pepper sauce, Worcestershire sauce, beef stock, tomato paste and tomatoes. Heat through just until boiling. Pour the vegetables and all of the liquid into the casserole dish with the meat. Cover with a lid.", "Bake in the preheated oven for 2 1/2 to 3 hours, until meat is very tender."]
