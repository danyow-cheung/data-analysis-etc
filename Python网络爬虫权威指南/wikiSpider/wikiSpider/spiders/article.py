import scrapy

'''------------------------------------------------------------------------------------'''
'''------------------------------------------简易爬虫------------------------------------'''
'''------------------------------------------------------------------------------------'''

class ArticleSpider(scrapy.Spider):
    name = "article"

    '''start_requests 函数是 Scrapy 定义的程序入口，用于生成 Scrapy 用来抓取网站的 Request
对象。'''
    def start_requests(self):
        urls = [ 
            "http://en.wikipedia.org/wiki/Python_"
            '%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python'
        ]
        '''arse 是一个用户定义的回调函数，通过 callback=self.parse 传递给 Request 对象。在后
面的内容中，你会看到 parse 函数更强大的功能，不过现在只是让它打印网页的标题。'''
        return [scrapy.Request(url=url,callback=self.parse)for url in urls]

    def parse(self,response):
        url = response.url 
        title = response.css("h1::text").extract_first()
        print("url is {}".format(url))
        print("title is {}".format(title))
# 运行命令 
# scrapy runspider article.py


