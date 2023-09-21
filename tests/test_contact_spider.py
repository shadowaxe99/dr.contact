
import unittest
from scrapy.http import Request, HtmlResponse
from contact_list_scraper.spiders.contact_spider import ContactSpider

class TestContactSpider(unittest.TestCase):

    def setUp(self):
        self.spider = ContactSpider()

    def test_parse(self):
        url = 'http://www.example.com'
        request = Request(url=url)
        response = HtmlResponse(url=url, request=request, body='<html></html>', encoding='utf-8')

        result = self.spider.parse(response)
        self.assertIsInstance(result, Request)

    def test_parse_contact_page(self):
        url = 'http://www.example.com/contact'
        request = Request(url=url)
        response = HtmlResponse(url=url, request=request, body='<html></html>', encoding='utf-8')

        result = self.spider.parse_contact_page(response)
        self.assertIsInstance(result, dict)
        self.assertIn('url', result)
        self.assertIn('file_type', result)

if __name__ == '__main__':
    unittest.main()
