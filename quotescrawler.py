import scrapy


class QuotescrawlerSpider(scrapy.Spider):
    name = 'quotescrawler'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
