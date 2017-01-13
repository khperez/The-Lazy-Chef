import scrapy

class IngredientSpider(scrapy.Spider):
    name = "ingredients"
    start_urls = [
        'https://www.budgetbytes.com/2017/01/chicken-broccoli-pasta-lemon-cream-sauce/'
    ]

    def parse(self, response):
        for ingredient in response.css('h2.entry-title'):
            yield {
                'title': recipe.css('a::text').extract(),
                'link': recipe.css('a::attr(href)').extract()
            }
