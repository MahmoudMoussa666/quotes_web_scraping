import scrapy
from scrapy.shell import inspect_response


class QuotesJsSpider(scrapy.Spider):
    name = 'quotes_js'
    allowed_domains = ['quotes.toscrape.com']

    def start_requests(self):
        url = 'http://quotes.toscrape.com/js/'
        yield scrapy.Request(url, meta={'playwright': True})

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield {
                'quote': quote.xpath('./span[@class="text"]/text()').get(),
                'by': quote.xpath('./span/small[@class="author"]/text()').get(),
                'tags': quote.xpath('./div[@class="tags"]/a/text()').getall()
            }
        next = response.xpath('//li[@class="next"]/a/@href')
        if next:
            yield response.follow(next.get(), meta={'playwright': True})