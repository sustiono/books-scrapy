# Book Scrapy

Scrap books data from http://books.toscrape.com/ using Scrapy

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some packages needed.

```bash
git clone git@github.com:sustiono/books-scrapy.git
cd books-scrapy
pip3 install virtualenv
virtualenv .env
source .env/bin/activate
cd books
pip install -r requirements.txt
```

## Usage
Choose one of the commands below to get the results in the desired format

```bash
scrapy crawl all_products -o books.csv
scrapy crawl all_products -o books.json
scrapy crawl all_products -o books.xml
```
