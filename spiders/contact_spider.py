
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from contact_list_scraper.items import ContactListItem

class ContactSpider(CrawlSpider):
    name = 'contact_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*\.(xls|xlsx|ods|csv|pdf|doc|docx|ppt|pptx|txt)$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ContactListItem()
        item['file_urls'] = [response.url]
        return item

This is a basic Scrapy spider that will crawl the domain "example.com" and follow all links to files with the extensions listed in the regular expression in the Rule. When it finds a link to a file with one of those extensions, it will call the "parse_item" method, which creates a new ContactListItem (a Scrapy Item), sets its "file_urls" field to a list containing the URL of the file, and returns the item.