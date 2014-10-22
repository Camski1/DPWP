class RecData(object):
    def __init__(self):
        self.rec_arr = [[],[],[],[],[]]

class Bigos(object):
    def __init__(self):
        self.rec_name = "Bigos"
        self.rec_desc = "Bigos is a stewed dish made from cabbage as a main ingredient. Fresh cabbage can be used as well as the soured one, called sauerkraut. Hence, more than one kind of bigos exists in the Polish cuisine."
        self.rec_ingr = ["2 thick slices hickory-smoked bacon", "1 pound kielbasa sausage sliced into 1/2 inch pieces", "1 pound cubed pork stew meat", "1/4 cup all-purpose flour", "3 cloves garlic, chopped", "1 onion, diced", "2 carrots, diced", "1 1/2 cups sliced fresh mushrooms", "4 cups shredded green cabbage", "1 (16 ounce) jar sauerkraut, rinsed and well drained", "1/4 cup dry red wine", "1 bay leaf", "1 teaspoon dried basil", "1 teaspoon dried marjoram", "1 tablespoon sweet paprika", "1/4 teaspoon salt", "1/8 teaspoon ground black pepper", "1/8 teaspoon caraway seed, crushed", "1 pinch cayenne pepper", "1/2 ounce dried mushrooms", "1 dash bottled hot pepper sauce", "1 dash Worcestershire sauce", "5 cups beef stock", "2 tablespoons canned tomato paste", "1 cup canned diced tomatoes"]
        self.directions = ["Preheat the oven to 350 degrees F (175 degrees C).", "Coat the cubes of pork lightly with flour and fry them in the bacon drippings over medium-high heat until golden brown. Use a slotted spoon to transfer the pork to the casserole. Add the garlic, onion, carrots, fresh mushrooms, cabbage and sauerkraut. Reduce heat to medium; cook and stir until the carrots are soft, about 10 minutes. Do not let the vegetables brown.", "Deglaze the pan by pouring in the red wine and stirring to loosen all of the bits of food and flour that are stuck to the bottom. Season with the bay leaf, basil, marjoram, paprika, salt, pepper, caraway seeds and cayenne pepper; cook for 1 minute.", "Mix in the dried mushrooms, hot pepper sauce, Worcestershire sauce, beef stock, tomato paste and tomatoes. Heat through just until boiling. Pour the vegetables and all of the liquid into the casserole dish with the meat. Cover with a lid.", "Bake in the preheated oven for 2 1/2 to 3 hours, until meat is very tender."]
        self.prep = 30
        self.cook = 90
        self.img = 'img/bigos.jpg'
        self.rec_array = [self.rec_name, self.rec_desc, self.rec_ingr, self.directions, self.prep, self.cook]

class PotatoCakes(object):
    def __init__(self):
        self.rec_name = "Placki Ziemniaczane"
        self.rec_desc = "Placki ziemniaczane is a Polish name for a quite well-known, simple and good food made from grated potatoes fried in a fat."
        self.rec_ingr = ["4-5 large potatoes, peeled and grated", "1 large onion", "3-4 minced garlic cloves", "2 eggs", "4 tbsp flour ", "1/2 teaspoon marjoram", "1/2 teaspoon salt (minimum)", "Freshly ground black pepper"]
        self.directions = ["Using a food processor or hand shredder, grate potatoes and onion using the finest grader.  The finer the potatoes are grated, the better because it is easier to cook.  If you grate the potatoes in larger chunks, you will just have to cook longer and use a little bit more oil for taste.", "Squeeze potatoes and onions with hands to remove excess liquid", "Put grated potatoes and onion in a large bowl and mix with eggs, garlic, flour, marjoram, salt, and pepper.", "Heat oil in large frying pan until almost smoking.  Carefully put a large spoonful of the potato mixture into the pan and flatten with a fork.  Repeat until you have 3-4 pancakes in the pan. Fry each pancake until it is golden brown on both sides.  Remove with spatula and drain on a paper towel.", "Serve potato pancakes warm with topping of choice."]
        self.prep = 30
        self.cook = 90
        self.img = 'img/pancakes.jpg'
        self.rec_array = [self.rec_name, self.rec_desc, self.rec_ingr, self.directions, self.prep, self.cook]


class Zrazy(object):
    def __init__(self):
        self.rec_name = "Zrazy"
        self.rec_desc = "Zrazy is an traditional Old Polish food coming from the Polish Gentry and the cuisine of hunters. Zrazy is made from slices of beef, veal or game, stir-fried and stewed with an addition of vegetables and spices."
        self.rec_ingr = ["700 g beef", "2 tbsp grainy mustard", "200 g smoked bacon, cut into strips", "200 g gherkin, cut into thin strips", "200 g brown onion, cut into strips", "500 ml beef stock"]
        self.directions = ["Cut the beef into 4 to 6 pieces and pound until thin. Spread each slice of beef with the mustard. On each slice, place a piece of bacon, gherkin and some onion. Roll up the beef slices and secure with toothpicks.","Heat oil in a deep frying pan and fry the beef roulades until brown on each side. Add 1/2 cup of beef stock. Simmer for 1 hour or until cooked, adding more stock when necessary. Season to taste.", "Serve with mashed beetroot."]
        self.prep = 30
        self.cook = 90
        self.img = 'img/Zrazy.jpg'
        self.rec_array = [self.rec_name, self.rec_desc, self.rec_ingr, self.directions, self.prep, self.cook]


class Nalesniki(object):
    def __init__(self):
        self.rec_name = "Nalesniki"
        self.rec_desc = "Typical of many cuisines, Polish nalesniki are just pancakes with various fillings (from sweet to spicy). Nalesniki evolved from Old Polish pies and pancakes under the influence of French cuisine, and have been very popular in Poland for decades."
        self.rec_ingr = ["1/2 cup all-purpose flour", "1/2 cup milk", "1/4 cup lukewarm water", "2 large eggs", "2 tablespoons butter, melted", "1/2 teaspoon salt"]
        self.directions = ["In a blender or food processor, combine all ingredients until smooth. Transfer to a pitcher, cover with plastic wrap and let rest for 30 minutes so the liquid can be absorbed by the flour.","Using a 2-ounce ladle, portion out batter into a nonstick crepe pan or small skillet that has been lightly coated with butter. Rotate pan and swirl batter until it covers the entire bottom of pan. Cook until lightly brown or spotted brown on the underside. Turn and cook second side until light brown.", "Remove to waxed paper or parchment paper and repeat with remaining batter and butter. Serve immediately or wrap and freeze up to 1 month."]
        self.prep = 30
        self.cook = 90
        self.img = 'img/Nalesniki.jpg'
        self.rec_array = [self.rec_name, self.rec_desc, self.rec_ingr, self.directions, self.prep, self.cook]


class Golumpki(object):
    def __init__(self):
        self.rec_name = "Golumpki"
        self.rec_desc = "Golabki or stuffed cabbage is one of a traditional food of Central and Eastern Europe. Polish golabki is a cooked knob of forcemeat wrapped up in a leaf of a white cabbage."
        self.rec_ingr = ["2 c. cooked rice", "1 to 1 1/2 lbs. raw ground beef", "1/4 tsp. salt & pepper", "1 med. green head of cabbage"]
        self.directions = ["Mix together the rice, salt/pepper, and raw ground beef. Boil the head of cabbage after coring it, just to loosen the leaves for about 3 to 5 minutes. Take 1 leaf out at a time and fill it with approximately 2 tablespoonfuls of rice-meat mixture. Fold it over horizontally and then bring in the sides of leaf to make a pocket. Arrange in a covered casserole dish or roasting pan and bake at 350 degrees for 1 hour."]
        self.prep = 30
        self.cook = 90
        self.img = 'img/Golumpki.jpg'
        self.rec_array = [self.rec_name, self.rec_desc, self.rec_ingr, self.directions, self.prep, self.cook]