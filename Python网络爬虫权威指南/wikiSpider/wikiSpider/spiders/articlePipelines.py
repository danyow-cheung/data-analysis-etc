
'''
因此 parse_items 现在的任务就是提取原始数据，尽可能少做数据处理，然后传递给管线 组件:
'''
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from wikiSpider.items import Article

class ArticleSpider(CrawlSpider):
    name = "articlePipelines"

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
