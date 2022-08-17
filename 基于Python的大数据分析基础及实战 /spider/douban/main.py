
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from douban.spiders.top250 import Top250Spider


# 获取settings.py模版设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)

# 添加多个spider
process.crawl(Top250Spider)

# 启动爬虫，会出现阻塞直至爬取完成
process.start()
