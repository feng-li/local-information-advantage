#! /usr/bin/python3

# -*- coding: utf-8 -*-

#连接数据库
import pymysql
import re
import jieba
import pandas as pd
import os

###连接数据库
#输入：数据库名称
def connect_database(database):
    con = pymysql.connect(
        user = "",
        password = "",
        port = 3306,
        host = "127.0.0.1",
        db = str(database),
        charset = 'utf8'
    )
    return(con)

###从表中选择信息
#输入：表名称，游标
def select_from_table(table_name, con):
    cur = pymysql.cursors.SSCursor(con)
    sql_1 = "select 内容,Id,已采,已发,点击,回复,时间,楼层 from "+str(table_name)
    content = []
    Id = []
    collect = []
    send = []
    click = []
    reply = []
    time = []
    floor = []

    cur.execute(sql_1)
    row = cur.fetchone()
    while row is not None:
        content.append(row[0])
        Id.append(row[1])
        collect.append(row[2])
        send.append(row[3])
        click.append(row[4])
        reply.append(row[5])
        time.append(row[6])
        floor.append(row[7])
        row = cur.fetchone()
    return(content, Id, collect, send, click, reply, time, floor)

###获得某数据库所有表的名称
#输入：数据库名称， 游标
#输出：表名称列表
def get_table_name_list(database, con):
    cur = pymysql.cursors.SSCursor(con)
    sql_1 = "select table_name from information_schema.tables where table_schema='"+str(database)+"'"
    cur.execute(sql_1)
    row = cur.fetchone()
    table_name_list = []
    while row is not None:
        if re.findall(r"\d+\.?\d*",row[0]):
            table_name_list.append(row[0])
            row = cur.fetchone()

    return(table_name_list)

#读入情感词典
def open_dict(Dict, path):
    path = path + '/%s.txt' % Dict
    emo_dict = []
    with open(path, 'r', encoding='utf-8') as dictionary:
        for word in dictionary:
            word = word.strip('\n').strip(' ')
            emo_dict.append(word)
            # dictionary.close()
    return emo_dict

cwd = os.path.dirname(os.path.abspath(__file__))

deny_word = open_dict(Dict = u'否定词', path = cwd+'/data/hownet_sentiment')
postdict = open_dict(Dict = u'正面情绪词语_', path = cwd + '/data/hownet_sentiment')
negdict = open_dict(Dict = u'负面情绪词语_', path = cwd + '/data/hownet_sentiment')

degree_word = open_dict(Dict = u'程度级别词语_', path = cwd + '/data/hownet_sentiment')
mostdict = degree_word[degree_word.index('extreme')+1 : degree_word.index('very')]#权重4，
verydict = degree_word[degree_word.index('very')+1 : degree_word.index('more')]#权重3
moredict = degree_word[degree_word.index('more')+1 : degree_word.index('ish')]#权重2
ishdict = degree_word[degree_word.index('ish')+1 : ]#权重0.5

#句子打分
#第一步：读取数据，进行分句。
#第二步：查找对分句的情感词，记录积极（1.0）或消极（-1.0）情感值，以及位置。
#第三步：往情感词前一位查找程度词。为程度词设权值（extreme-4,very-3,more-2,ish-0.5），乘以情感值。
#第四步：往情感词前一位查找否定词，得分变为相反数。
#第五步：计算一条句子所有分词的得分相加为整句的情感得分。


# Each sentence is segmented into words. We assign the key positive sentiment words as score 1 and key negative sentiment words as score -1 by looking up a prespecified sentiment dictionary. The score of a key sentiment word is further weighted by its modifier words with weights of 4, 3, 2, 0.5 for "extreme", "strong", "moderate", and "mild" degrees, respectively. If there is a negative word appeared before the key sentiment word, the opposite sore is used. The overall sentiment score is the sum of all the scores for the sentiment words in the sentence.



class sentiment_score():

    def __init__(self, text):
        self.text = text
        self.scores = 0

    def delete_useless_info(self):
        if re.search('作者',self.text):
            self.text = self.text[:re.search('作者',self.text).start()]

    def get_score(self):
        word_list = list(jieba.cut(self.text))#分句
        self.scores = 0#记录整句情感得分
        index = 0#记录词的位置
        score = 0
        for word in word_list:
            if word in postdict:#积极情绪词
                score = 1.0
                if word_list[index-1] in degree_word and index>0:#检查当前词语前一个词是否程度词
                    if word_list[index-1] in mostdict:#根据程度词的等级赋权
                        score *= 4
                    elif word_list[index-1] in verydict:
                        score *= 3
                    elif word_list[index-1] in moredict:
                        score *= 2
                    elif word_list[index-1] in ishdict:
                        score *= 0.5
                if word_list[index-1] in deny_word and index>0:#检查当前次的前一词是否为否定词
                    score = -score
            elif word in negdict:#消极情绪词
                score = -1.0
                if word_list[index-1] in degree_word and index>0:#检查当前词语前一个词是否程度词
                    if word_list[index-1] in mostdict:#根据程度词的等级赋权
                        score *= 4
                    elif word_list[index-1] in verydict:
                        score *= 3
                    elif word_list[index-1] in moredict:
                        score *= 2
                    elif word_list[index-1] in ishdict:
                        score *= 0.5
                        index += 1
                        self.scores += score
        return self.scores

#输入：数据库名称， 股票编号
#输出：匹配好地点信息的csv文件
# def match(database, stk):
#     ip_sas = pd.read_sas('/home1/yqhuang/split-docs/a_'+str(database)+'/_'+str(stk)+'.sas7bdat',encoding = 'gbk')
#     df_ip = ip_sas[['Id','posterprov','postercity','firmprov','firmcity1','firmcity2']]
#     df = pd.merge(df_sentiment, df_ip, how = 'outer')
#     df.to_csv(str(stk)+"_match.csv",index = False,sep=',')
