import os 
pname = input("項目名:\n")
os.system("Scrapy startproject "+ pname)
# 創建文件夾
os.chdir(pname)


wname = input("爬蟲名:\n")
website = input("網址:\n")
os.system("scrapy genspider "+wname +" "+website)
runc = ""

# from sc
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# from %s.spiders.%s import %s 

# 获取settings.py模版设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)

# 添加多个spider
# process.crawl(%s)

# 启动爬虫，会出现阻塞直至爬取完成
process.start()


'''
文件夹               文件                     描述
douban              main.py                 程序运行总入口
douban              scrapy.cfg              项目配置文件
douban/douban       __init__.py             初始化
douban/douban       items.py                抓取内容描述
douban/douban       middleewares.py         中间件
douban/douban       pipelines.py            管道，数据的清洗与存储
douban/douban       settings.py             配置文件
douban/douban/spider    __init__.py         初始文件
douban/douban/spider    top250.py           爬虫文件




'''