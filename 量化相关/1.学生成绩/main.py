import pandas as pd 
from pymongo import MongoClient
import glob
import numpy as np 

class MongDB(object):
    def __init__(self,dbName= None,collectionName=None):
        # 数据库名
        self.dbName = dbName
        # 集合名
        self.collectionName = collectionName
        # mongodb服务器
        self.client= MongoClient("localhost",27017)

        self.DB = self.client[self.dbName]
        self.collection = self.DB[self.collectionName]
    
    
    def Insert(self,path = None):
        # 读取csv文件
        df = pd.read_csv(path)
        # 转换为字典格式
        data = df.to_dict("records")
        # 插入数据
        self.collection.insert_many(data,ordered=False)
        # flag
        print("all done")


    def find_two(self):
        #获取数据库的连接，转换为pd格式，进行数据分析
        data = pd.DataFrame(list(self.collection.find()))

        score = data[["total"]]
        bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450,500,550,600,650,700]
        # 分组统计
        score2 = pd.cut(score.values.flatten(), bins=bins)
        score2 = pd.DataFrame(score2, columns=["status"]) 
        data["status"] = score2


        # # 每个区间学生的总人数
        data_status_count = data.pivot_table(
            index="status",
            values="total",
            aggfunc={"total":"count"}
        )
        data_status_count.rename(columns={"total": "总人数"},inplace=True)
       
        # # 每个区间学生总分的均值
        data_status_mean = data.pivot_table(
            index="status",
            values="total",
            aggfunc={"total":"std"}
        )
        data_status_mean.rename(columns={"total": "data_status_mean"},inplace=True)
        

        # # 每个区间学生总分的方差
        data_status_var = data.pivot_table(
            index="status",
            values="total",
            aggfunc={"total":"var"}
        )
        data_status_var.rename(columns={"total": "方差"},inplace=True)
      
        # 数据连接，写入数据库
        output = pd.concat([data_status_count,data_status_mean,data_status_var],axis=1)
        output_df = output.to_dict("records")


        # 更改集合写入
        self.collectionName = "status"
        self.collection = self.DB[self.collectionName]

        insert_status = self.collection.insert_many(output_df)
        print("done-find2")
        insert_status.insert_many(output_df)

        return data 

    def sexual(self):
        # 从区间中得到带有status的数据
        data =  self.find()
        print("已获取数据")
        data_female = data.loc[data.sexual=="female"]
        print(data_female)


    def find_three(self):
        data =pd.DataFrame(list(self.collection.find()))

        # 查询分数大于500的
        data_5 = data.loc[data["total"]>500 ]
        data_5 = data_5.drop_duplicates()

        # 查询分数小于600的
        data_6 = data.loc[data["total"]<=600 ].drop_duplicates()
        data_6 = data_6.drop_duplicates()

        #数据联合,求交集
        data_56 = pd.concat([data_5,data_6],join="inner",ignore_index=True).drop_duplicates()
        # 语文成绩大于100
        data_56_cn = data_56[data_56["chinese"]>100].drop_duplicates()
        data_rank = data_56_cn.sort_values("math",ascending=False)

        data_rank_df = data_rank.to_dict("records")
        # 更改集合写入
        self.collectionName = "rank"
        self.collection = self.DB[self.collectionName]

        self.collection.insert_many(data_rank_df)
        print("done-find3")


if __name__=="__main__":

    mongodb = MongDB(dbName="python_test",collectionName="record")
    
    # 题目四
    # mongodb.sexual()

    # 题目三
    # mongodb.find_three()

    # 题目二
    # mongodb.find_two()

    # 题目一
    # path = glob.glob("data_/*.csv")    
    # for i in path:
    #     mongodb.Insert(path=i)
