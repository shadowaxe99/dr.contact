
import unittest
from contact_list_scraper.utils.file_handler import FileHandler

class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.file_handler = FileHandler()

    def test_handle_xls(self):
        result = self.file_handler.handle('test.xls')
        self.assertTrue(result)

    def test_handle_xlsx(self):
        result = self.file_handler.handle('test.xlsx')
        self.assertTrue(result)

    def test_handle_ods(self):
        result = self.file_handler.handle('test.ods')
        self.assertTrue(result)

    def test_handle_csv(self):
        result = self.file_handler.handle('test.csv')
        self.assertTrue(result)

    def test_handle_pdf(self):
        result = self.file_handler.handle('test.pdf')
        self.assertTrue(result)

    def test_handle_doc(self):
        result = self.file_handler.handle('test.doc')
        self.assertTrue(result)

    def test_handle_docx(self):
        result = self.file_handler.handle('test.docx')
        self.assertTrue(result)

    def test_handle_ppt(self):
        result = self.file_handler.handle('test.ppt')
        self.assertTrue(result)

    def test_handle_pptx(self):
        result = self.file_handler.handle('test.pptx')
        self.assertTrue(result)

    def test_handle_txt(self):
        result = self.file_handler.handle('test.txt')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
