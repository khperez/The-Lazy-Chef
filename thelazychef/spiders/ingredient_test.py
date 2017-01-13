# -*- coding: utf-8 -*-
import scrapy


class IngredientTestSpider(scrapy.Spider):
    name = "ingredient_test"
    allowed_domains = ["https://www.budgetbytes.com/2017/01/chicken-broccoli-pasta-lemon-cream-sauce/"]
    start_urls = ['http://https://www.budgetbytes.com/2017/01/chicken-broccoli-pasta-lemon-cream-sauce//']

    def parse(self, response):
        pass
