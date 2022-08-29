# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
from wikiSpider.items import Article
from string import whitespace

'''
这个示例类应该替换成你的新管线组件代码。
在前面的几节中，你已经收集了两个原始格 式的字段，
而这些可能需要进行额外的数据处理:
lastUpdated(一个表示日期的、格式糟 糕的字符串对象)和 
text(一个混乱的由字符串片段组成的数组)。
'''

class WikispiderPipeline:
    def process_item(self, article, spider):
        dataStr = article['lastUpdated']
        article['lastUpdated'] = article['lastUpdated'].replace("this page was last edited on","")
        article['lastUpdated'] = article['lastUpdated'].strip()
        article['lastUpdated'] = datetime.strptime(
        article['lastUpdated'], '%d %B %Y, at %H:%M.')
        article['text'] = [line for line in article['text']
            if line not in whitespace]
        article['text'] = "".join(article['text'])
        return article
        