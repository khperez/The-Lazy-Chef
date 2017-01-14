import scrapy

class IngredientAlpha(scrapy.Spider):
    name = "ingredient_alpha"
    start_urls = [
        "https://www.budgetbytes.com/2017/01/chicken-cranberry-salad-lemon-poppy-seed-dressing/"
    ]

    def parse(self, response):
        ingredients = response.xpath('//li[@class="ingredient"]/text()').extract()
        with open("test.txt", 'wb') as f:
            for ingredient in ingredients:
                f.write("{}\n".format(ingredients))
