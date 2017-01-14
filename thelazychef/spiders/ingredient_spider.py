import scrapy

class IngredientSpider(scrapy.Spider):
    name = "ingredients"

    def __init__(self, url=None, *args, **kwargs):
        super(IngredientSpider, self).__init__(*args, **kwargs)
        self.start_urls = "{}".format(url)

    def parse(self, response):
        print "Check"
