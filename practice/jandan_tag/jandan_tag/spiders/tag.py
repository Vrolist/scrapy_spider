import scrapy
from ..items import JandanTagItem

class jandan_spider(scrapy.Spider):
    name = "jandan"
    allowed_domains = ["jandan.net"]
    start_urls = ["http://jandan.net/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD"]

    def parse_page(self,response):
        jandan_info = JandanTagItem()
        jandan_info['url'] = response.meta['url']
        jandan_info['title'] = response.xpath(".//*[@id='content']/div[2]/h1/a/text()").extract()
        jandan_info['content'] = response.xpath(".//*[@id='content']/div[2]/p/text()").extract()
        return  jandan_info

    def parse_links(self,response):
        all_links = response.xpath(".//*[@id='content']/div/div/div/h2/a/@href").extract()
        for i in all_links:
            yield scrapy.Request(i, meta={'url':i}, callback=self.parse_page)

    def parse(self, response):
        base_url = "http://jandan.net/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/page/{}"
        big_nums = response.xpath(".//*[@id='content']/div[25]/span[1]/text()").extract()
        big_num = int(big_nums[0].split('/')[-1])
        for i in range(1,big_num+1):
            yield scrapy.Request(base_url.format(i), callback=self.parse_links)
