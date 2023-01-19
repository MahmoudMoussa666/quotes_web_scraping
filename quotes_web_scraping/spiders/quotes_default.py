import scrapy


class QuotesDefaultSpider(scrapy.Spider):
    name = 'quotes_default'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

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
            yield response.follow(next.get())
