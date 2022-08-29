'''------------------------------------------------------------------------------------'''
'''------------------------------------------带规则的抓取--------------------------------'''
'''------------------------------------------------------------------------------------'''

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']

    start_urls = ['https://en.wikipedia.org/wiki/'
             'Benevolent_dictator_for_life']


    '''这行代码提供了 Scrapy 的 Rule 对象列表，这些对象定义了所有链接的过滤规则。
    当设置 多个规则时，每个链接都要按顺序检查。匹配的第一个规则用来决定如何处理链接。
    如果 链接不能匹配任何规则，就会被忽略。'''
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items',
            follow=True)]

    def parse_items(self,response):
        url = response.url 
        title = response.css("h1::text").extract_first()

        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()

        lastUpdated = response.css("li#footer-info-lastmod::text").extract_first()
        
        lastUpdated = lastUpdated.replace(
                  'This page was last edited on ', '')
        print('URL is: {}'.format(url))
        print('title is: {} '.format(title))
        print('text is: {}'.format(text))
        print('Last updated: {}'.format(lastUpdated))
# scrapy runspider articles.py