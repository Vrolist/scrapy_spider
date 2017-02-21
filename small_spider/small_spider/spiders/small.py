import scrapy
from ..items import SmallSpiderItem

class tubagua_spider(scrapy.Spider):
    name = "pic_spider"
    allowed_domains = ["www.ivsky.com"]
    start_urls = ["http://www.ivsky.com/tupian/renwutupian/"]


    def parse(self, response):
        sspider = SmallSpiderItem()
        sspider['pic'] = response.xpath('//ul[@class="ali"]/li//img/@src').extract()
        # print(sspider['pic'],len(sspider['pic']))
        return sspider