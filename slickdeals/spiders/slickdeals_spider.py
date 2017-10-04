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
        deal_items = response.xpath('//*[@class="itemTitle"]/text()').extract()
        for deal in deal_items:
            item = SlickdealsItem()
            item['name'] = deal
            yield item

