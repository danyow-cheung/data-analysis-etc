'''------------------------------------------------------------------------------------'''
'''--------------------------------------------创建item---------------------------------'''
'''-------------------------------------------------------------------------------------'''
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from wikiSpider.items import Article


class ArticleSpider(CrawlSpider):
    name = "articleItems"

    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent','_dictator_for_life']

    rules = [Rule(LinkExtractor(allow="(/wiki/)((?!:).)*$"),callback='parse_items',follow=True)]

    def parse_items(self,response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css("h1::text").extract_first()

        article['text'] = response.xpath('//div[@id=''"mw-content-text"]//text()').extract()

        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        article['lastUpdated'] = lastUpdated.replace('This page was '
                 'last edited on ', '')

        return article

# scrapy runspider articleItems.py         
'''
输出item
$ scrapy runspider articleItems.py -o articles.csv -t csv
$ scrapy runspider articleItems.py -o articles.json -t json
$ scrapy runspider articleItems.py -o articles.xml -t xml

'''