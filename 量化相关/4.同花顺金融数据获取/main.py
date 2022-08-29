'''
功能:爬取所有时间的财务数据 导出成csv文件
'''
from bs4 import BeautifulSoup
import urllib.request
import time
import requests
import requests
from fake_useragent import UserAgent

 
'''检查改网页是否可以爬取'''
def getHtml(url):
    html = ''
    ua = UserAgent()
    # header = {"User-Agent": ua.random, "Referer": url}
    headers= {'User-Agent':str(UserAgent().random)}
    # r = requests.get(url, headers=headers, timeout=10)
    url = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf8')
        print(html)
    except urllib.error.URLError as e:
        print(e)
    return html

'''爬虫下载报表'''
def getData(url):
    try:
        # 调用可否爬取函数
        html = getHtml(url)
        # 调用bs对象来实现爬取 
        soup = BeautifulSoup(html,"lxml")
        table_data = soup.find("div",attrs={"class":"table_data"})
    # 判错 遇错处理
    except Exception as err:
        print(err)



'''股票id对应的url页面'''
def get_all_stock_link():
    stock_list = []
    url_lst = []
    try:
        # 自定义url实现网页爬取
        url_style = "http://stockpage.10jqka.com.cn/{stock_number}/finance/#view/"

        # 打开文件
        f = open("data/stock_list.txt") 
        # 调用文件的 readline()方法
        line = f.readline()   #每次读取一行内容
        while line:
            # print(line,end = '')  # end = ''表示不换行
            line = f.readline()
            stock_list.append(line)
        f.close()
        
        for i in range(len(stock_list)):
            
            num = stock_list[i].replace("\n","")
            url = url_style.format(stock_number=num)
            url_lst.append(url)
        
    except Exception as err:
        print(err)

    return url_lst

if __name__ =="__main__":
    get_all_stock_link()


# url = "http://stockpage.10jqka.com.cn/600208/finance/#view"
# getHtml(url)
get_all_stock_link()




