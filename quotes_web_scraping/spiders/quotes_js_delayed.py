import scrapy
from scrapy_playwright.page import PageMethod

class QuotesJsDelayedSpider(scrapy.Spider):
    name = 'quotes_js_delayed'
    allowed_domains = ['toscrape.com']
    url_parameter = '?delay=2000'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/js'
        yield scrapy.Request(url+self.url_parameter, meta={
            'playwright':True,
            'playwright_include_page': True,
            'playwright_page_methods': [PageMethod('wait_for_selector', 'div.quote')],
            'err_back': self.errback
        })

    async def parse(self, response):
        page = response.meta['playwright_page']
        await page.close()

        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield {
                'quote': quote.xpath('./span[@class="text"]/text()').get(),
                'by': quote.xpath('./span/small[@class="author"]/text()').get(),
                'tags': quote.xpath('./div[@class="tags"]/a/text()').getall()
            }
        next = response.xpath('//li[@class="next"]/a/@href')
        if next:
            yield response.follow(next.get()+self.url_parameter, meta={
            'playwright':True,
            'playwright_include_page': True,
            'playwright_page_methods': [PageMethod('wait_for_selector', 'div.quote')],
            'err_back': self.errback
            })
        else:
            print('There is no next button')
    

    async def errback(self, response):
        page = response.request.meta['playwright_page']
        await page.close()