
import unittest
from contact_list_scraper.utils.notable_filter import NotableFilter

class TestNotableFilter(unittest.TestCase):

    def setUp(self):
        self.notable_filter = NotableFilter()

    def test_filter_notable(self):
        contacts = [
            {"name": "John Doe", "email": "john@example.com"},
            {"name": "Jane Doe", "email": "jane@example.com"},
            {"name": "Notable Person", "email": "notable@example.com"}
        ]
        notable_list = ["Notable Person"]
        result = self.notable_filter.filter_notable(contacts, notable_list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Notable Person")

    def test_filter_notable_empty(self):
        contacts = []
        notable_list = ["Notable Person"]
        result = self.notable_filter.filter_notable(contacts, notable_list)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
