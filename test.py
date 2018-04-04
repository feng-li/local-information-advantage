# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 20:57:43 2018

@author: Lai
"""

from emotion_score import* 
import pandas as pd
import sys
import re


#300002 chuangyeban 
#600281 shanghai
#600346 shagnhai
#000517 shenzhen
#000004 shenzhen
#002076 zhongxiaoban
#shanghai  content_600000 ~~~ 发现数据库的表的名称有不同的，而且股票的序号也不是连续的

database = sys.argv[1]

with open(str(database)+'.csv') as f:
    table_name = []
    stk_name = []
    for line in f:
        table =line.split('\n')
        table_name.append(table[0])
        stk = re.findall(r"\d+\.?\d*",line)[0]
        stk_name.append(stk)
        
a = len(table_name)
con = connect_database(database)#连接数据库
for i in range(0,3):
    table = table_name[i]
    stk = stk_name[i]
    content, Id, collect, send, click, reply, time, floor = select_from_table(table, con)#选取信息
    score_list1 = []
    for text in content:#情感打分
        text_score = emotion_score(text)
        text_score.delete_useless_info()
        score_list1.append(text_score.get_score())

    dataframe = pd.DataFrame({'Id':Id, '已采':collect, '已发':send, '点击':click, '回复':reply, '时间':time, '楼层':floor, '情绪':score_list1})
    columns = ['Id', '已采', '已发', '点击', '回复','时间','楼层','情绪']
    dataframe.to_csv(str(stk)+"_emotion.csv",index = False,sep=',', columns = columns)#输出情感信息的csv文件
con.close()
for i in range(0,3): 
    stk = stk_name[i]
    match(database, stk)#将情感信息文件和地点信息文件进行匹配，输出csv
    

