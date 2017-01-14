import scrapy
import re

class IngredientAlpha(scrapy.Spider):
    name = "ingredient_alpha"
    start_urls = [
        "http://damndelicious.net/2016/10/18/ground-beef-noodle-stir-fry/"
    ]

    def parse(self, response):
        measurements = ['lb', 'lbs', 'pound', 'pounds',
                        'tbsp', 'tbsps', 'tablespoon', 'tablespoons',
                        'tsp', 'teaspoon', 'teaspoons',
                        'cup', 'cups',
                        'oz', 'ounce', 'ounces']
        ingredients = response.xpath('//li[@class="ingredient"]/text()').extract()
        target =  open("ingredients.txt", "wb")
        for ingredient in ingredients:
            ingredient_string = " "
            ingredient = ingredient.encode('utf-8')
            ingredient = ingredient.split(" ")
            if ingredient[0].isdigit():
                ingredient.remove(ingredient[0])
            elif ingredient[0].find("/") is not -1:
                ingredient.remove(ingredient[0])
            elif re.match("[^\x00-\x7f]", ingredient[0]) is not None:
                ingredient.remove(ingredient[0])
            for word in ingredient:
                # Find measurement labels
                if word.lower() in measurements:
                    ingredient.remove(word)
                # Remove currency labels
                if "$" in word:
                    ingredient.remove(word)
            ingredient_string = ingredient_string.join(ingredient)
            target.write("{}\n".format(ingredient_string))
