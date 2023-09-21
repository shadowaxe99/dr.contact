
import scrapy

class ContactListItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    file_type = scrapy.Field()
