# Contact List Scraper

This project is a web scraper that collects links to spreadsheet files of contact lists from the web. It filters lists containing notable figures' contact info and supports multiple file types including xls, xlsx, ods, csv, pdf, doc, docx, ppt, pptx, txt.

## Installation

1. Clone the repository
2. Install the dependencies using pip:


pip install -r requirements.txt


## Usage

To start the scraper, navigate to the project directory and run:


scrapy crawl contact_spider


## Testing

To run the tests, navigate to the project directory and run:


python -m unittest discover tests


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)