from scrapy import Spider
from scrapy.selector import Selector

from slickdeals.items import SlickdealsItem
class SlickdealsSpider(Spider):
    # Name of the spider
    name = "slickdeals"
    # Base URL
    allowed_domains = ["slickdeals.net"]
    # Subsequent URLs
    start_urls = [
        "https://slickdeals.net/deals/home-automation/",
    ]

    def parse(self, response):
        deal_items = Selector(response).xpath('//div[@class="fpItem  "]')
        for deal in deal_items:
            item = SlickdealsItem()
            item['name'] = deal.xpath('div/div[1]/div[@class="itemImageAndName"]/div[@class="itemImageLink"]/a[@class="itemTitle"]/text()').extract()[0]
            if len(deal.xpath('div/div[1]/div[@class="itemInfoLine"]/div[@class="priceLine"]/div[@class="itemPrice  wide "]/text()').extract()) != 0:
                item['price'] = deal.xpath('div/div[1]/div[@class="itemInfoLine"]/div[@class="priceLine"]/div[@class="itemPrice  wide "]/text()').extract()[0]
            else:
                item['price'] = 0
            yield item

