import scrapy

class taobao_pc(scrapy.Spider):
    name = "taobao_pc"
    allowed_domains = ["s.taobao.com"]
    start_urls = ["https://s.taobao.com/search?spm=a217h.7276445.1997814021.1.mDvDa7&app=vproduct&vlist=1&q=%E7%AC%94%E8%AE%B0%E6%9C%AC&cat=1101&from_type=3c"]

    def parse(self, response):
        print(response)