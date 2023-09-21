
import os
from scrapy.exceptions import DropItem
from .utils.file_handler import FileHandler
from .utils.notable_filter import NotableFilter

class ContactListScraperPipeline:
    def __init__(self):
        self.file_handler = FileHandler()
        self.notable_filter = NotableFilter()

    def process_item(self, item, spider):
        file_url = item['file_urls'][0]
        file_extension = os.path.splitext(file_url)[1]

        if file_extension in ['.xls', '.xlsx', '.ods', '.csv', '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.txt']:
            if self.notable_filter.contains_notable(item['file_path']):
                return item
            else:
                raise DropItem(f"File {item['file_path']} does not contain notable figures contact info")
        else:
            raise DropItem(f"File {item['file_path']} is not a supported file type")
