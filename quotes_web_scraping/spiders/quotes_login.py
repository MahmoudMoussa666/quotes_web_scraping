import scrapy


class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes_login'
    allowed_domains = ['toscrape.com']
    
    def start_requests(self):
        yield scrapy.Request('http://quotes.toscrape.com/login')

    def parse(self, response):
        csrf = response.xpath('//form/input[@name="csrf_token"]/@value').get()
        
        yield scrapy.FormRequest('http://quotes.toscrape.com/login', formdata={'csrf_token': csrf,
                                                                                'username': 'admin',
                                                                                'password': 'password'},
                                                                    callback=self.parse_page)

    def parse_page(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield {
                'quote': quote.xpath('./span[@class="text"]/text()').get(),
                'by': quote.xpath('./span/small[@class="author"]/text()').get(),
                'tags': quote.xpath('./div[@class="tags"]/a/text()').getall()
            }
        next = response.xpath('//li[@class="next"]/a/@href')
        if next:
            yield response.follow(next.get(), callback=self.parse_page)
        