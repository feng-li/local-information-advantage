#! /usr/bin/python3

# -*- coding: utf-8 -*-

from sentiment_score import*
import pandas as pd
from sas7bdat import SAS7BDAT
import sys
import re
import logging
from snownlp import SnowNLP

database = sys.argv[1]
database_table_list_path = sys.argv[2]
k = int(sys.argv[3])#从k-1%执行到k%
out_path = "/home1/yqhuang/sentiment_out/" + database + "/" # hard code, consider rewrite this

with open(str(database_table_list_path)) as f:
    table_name = []
    stk_name = []
    for line in f:
        table =line.split('\n')
        table_name.append(table[0])
        stk = re.findall(r"\d+\.?\d*",line)[0]
        stk_name.append(stk)

a = len(table_name)
con = connect_database(database)#连接数据库
stk_list = []

for i in range(int(a*(k-1)/100),int(a*k/100)):
    table = table_name[i]
    stk = stk_name[i]
    content, Id, collect, send, click, reply, time, floor = select_from_table(table, con)#选取信息
    score_list1 = []
    for text in content:#情感打分
        # text_score = sentiment_score(text) # This function is not so stable.
        # text_score.delete_useless_info()
        # score_list1.append(text_score.get_score())
        if len(text) == 0:
            text_score = -1
        else:
            text_score = SnowNLP(text).sentiments

        score_list1.append(text_score)

    df_sentiment = pd.DataFrame({'Id':Id, '已采':collect, '已发':send, '点击':click, '回复':reply, '时间':time, '楼层':floor, '情绪':score_list1})
    # columns = ['Id', '已采', '已发', '点击', '回复','时间','楼层','情绪']
    # dataframe.to_csv(out_path + str(stk)+"_sentiment.csv",index = False,sep=',', columns = columns)#输出情感信息的csv文件
    logging.info('Processing database ' + database + " with table " + table + " done.")

    ## ip_sas = pd.read_sas('/home1/yqhuang/split-docs/a_'+str(database)+'/_'+str(stk)+'.sas7bdat',encoding = 'gbk')
    ip_sas = SAS7BDAT('/home1/yqhuang/split-docs/a_'+str(database)+'/_'+str(stk)+'.sas7bdat', encoding='gbk').to_data_frame()

    df_ip = ip_sas[['Id','posterprov','postercity','firmprov','firmcity1','firmcity2']]
    df = pd.merge(df_sentiment, df_ip) # 'how = 'outer' was not good'
    df.to_csv(out_path + str(stk)+"_match_New.csv",index = False,sep=',')

    stk_list.append(stk)
    logging.info('Matching database ' + database + " with table " + table + " done.")

con.close()
# for i in range(int(a*(k-1)/100),int(a*k/100)):
#     stk = stk_name[i]
stk_df = pd.DataFrame(stk_list)
stk_df.to_csv(out_path + "log-" + str(k)+'.csv', index = False, header = False)
