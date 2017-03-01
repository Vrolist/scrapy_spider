import scrapy

class db_movie(scrapy.Spider):
    name = "douban_movie"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/later/beijing/"]

    def parse(self, response):
        print(response)