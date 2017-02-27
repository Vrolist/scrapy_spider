import scrapy
import re
import urllib

class movie87_spider(scrapy.Spider):
    name = "comedy"
    allowed_domains = ["www.87movie.com"]
    start_urls = ["http://www.87movie.com/tag/%E5%96%9C%E5%89%A7/"]

    def parse_page(self, response):
        pass

    def parse(self,response):
        num_page = response.xpath('//ul[@class="pagination"]//li[last()]/a/@href').extract()
        number = 1
        if len(num_page) > 0:
            number = int(num_page[0].split('/')[-1].split('?')[0])
        for i in range(1, number+1):
            yield scrapy.Request(response.url + str(i) + '?o=data', callback=self.parse_page)