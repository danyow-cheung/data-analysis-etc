import scrapy
from douban.items import DoubanItem
from bs4 import BeautifulSoup
import re 


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def parse(self, response):
        
        soup = BeautifulSoup(response.body.decode("utf-8","ignore"),"lxml")
        ol = soup.find("ol",attrs={"class":"grid_view"})

        for li in ol.findAll("li"):
            tep = []
            titles = []
            for span in li.findAll("span"):
                if span.has_attr("class"):
                    if span.attrs["class"][0] =="title":
                        titles.append(span.string.strip().replace(",","，"))
                    elif span.attrs["class"][0] =="rating_num":
                        tep.append(span.string.strip().replace(",","，"))
                    elif span.attrs["class"][0] =="inq":
                        tep.append(span.string.strip().replace(",","，"))

            tep.insert(0,titles[0])
            while len(tep)<3:
                tep.append("-")
            
            tep = tep[:3]
            item = DoubanItem()
            item["name"] = tep[0]
            item["fen"] = tep[1]
            item["words"] = tep[2]
            
            yield item 

            a = soup.find("a",text= re.compile("^后页"))
            if a:
                yield scrapy.Request("https://movie.douban.com/top250" + a.attrs["href"],callback=self.parse )
                    