import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllProductsSpider(CrawlSpider):
    name = 'all_products'
    allowed_domains = ['books.toscrape.com']

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='http://books.toscrape.com/',
                             headers={
                                 'User-Agent': self.user_agent
                             })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ol/li/article/h3"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']"), process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        information = {}
        for info in response.xpath("//tr"):
            information[info.xpath("./th/text()").get()] = info.xpath("./td/text()").get()

        yield {
            'book_name': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'rating': response.xpath("//div[@class='col-sm-6 product_main']/p[3]//@class").get(),
            'description': response.xpath("//article[@class='product_page']/p/text()").get(),
            'information': information
        }
