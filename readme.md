## About the project
this project demonstrate the usage of **Scrapy** and **Playwright** to bypass any obstacle that you may find during web scraping like:
- infinite scrolling
- JavaScript rendered content
- delayed javascript content
- login

## About the website
[quotes.toscrape.com](quotes.toscrape.com) is a web scraping sandbox for developers validating their scraping technologies. It has many endpoints showing the quotes in many different ways, each of them including new scraping challenges, as described below.

### endpoints
- [Default](quotes.toscrape.com) Microdata and pagination
- [Scroll](quotes.toscrape.com/scroll) 	infinite scrolling pagination
- [JavaScript](quotes.toscrape.com/js) JavaScript generated content
- [Delayed](quotes.toscrape.com/js-delayed) Same as JavaScript but with a delay
- [Login](quotes.toscrape.com/login) login with CSRF token (any user/passwd works)

## Prerequisites  
1. python installed preferably in a virtual environment.
2. you can install all the requirements using this command pip install -r requirements.txt 

## Usage  
1. download the repository or clone it locally.
from the terminal cd into the project folder.
2. make sure you have installed python and the requirements.
3. you can crawl the website using the following commands.
- default endpoint  
`scrapy crawl quotes_default -o quotes_default.csv`
- infinite scrolling endpoint  
`scrapy crawl quotes_scroll -o quotes_scroll.csv`
- JavaScript endpoint  
`scrapy crawl quotes_js -o quotes_js.csv`
- delayed endpoint  
`scrapy crawl quotes_js_delayed -o quotes_js_delayed.csv`
- login endpoint  
`scrapy crawl quotes_login -o quotes_login.csv`

4. you will find the file which has the name you specified after -o in the project folder.
5. you may use csv or json format.