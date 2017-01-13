import scrapy

class RecipeSpider(scrapy.Spider):
    name = "recipes"
    start_urls = [
        'http://budgetbytes.com/2016'
    ]

    def parse(self, response):
        for recipe in response.css('h2.entry-title'):
            yield {
                'title': recipe.css('a::text').extract(),
                'link': recipe.css('a::attr(href)').extract()
            }
