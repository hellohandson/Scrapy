import scrapy

class DmozSpider(scrapy.Spider):
    name = "handson"
    allowed_domains = ["thehandson.co"]
    start_urls = [
        "http://thehandson.co/diary/diary/"
    ]

    def parse(self, response):
        for sel in response.xpath('//div'):
            title = sel.xpath('//h2/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('//h3/text()').extract()
            print title, link, desc

