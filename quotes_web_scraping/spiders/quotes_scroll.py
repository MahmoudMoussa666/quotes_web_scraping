import scrapy
import json

class QuotesScrollSpider(scrapy.Spider):
    name = 'quotes_scroll'
    allowed_domains = ['quotes.toscrape.com']
    base_url = 'https://quotes.toscrape.com/api/quotes?page='
    current_page = 1
    
    def start_requests(self):
        return [scrapy.Request(url=self.base_url+str(self.current_page))]

    def parse(self, response):
        res =  json.loads(response.body)
        for quote in res['quotes']:
            yield {'author': quote['author']['name'],
                    'tags': quote['tags'], 
                    'quote': quote['text'] }
        if res['has_next']:
            self.current_page += 1
            yield scrapy.Request(url=self.base_url+str(self.current_page))
