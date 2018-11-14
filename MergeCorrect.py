#! /usr/bin/python3

import sys
import pandas as pd

path_to_list = sys.argv[1]
k = int(sys.argv[2])#从k-1%执行到k%

file_list = []
with open(path_to_list,"r") as f:
    for line in f:
        file_list.append(line[:(-1)]) # remove '\n'

file_len = len(file_list)
for i in range(int(file_len*(k-1)/100),int(file_len*k/100)):
    df = pd.read_csv(str(file_list[i]), low_memory = False)

    df1 = df[~df['回复'].isnull()].drop(['posterprov', 'postercity', 'firmprov', 'firmcity1', 'firmcity2'], 1)
    df2 = df[df['回复'].isnull()].drop(['回复', '已发', '已采', '情绪', '时间', '楼层', '点击'],1)

    dfout = pd.merge(df1, df2)
    dfout.to_csv(str(file_list[i])[:(-4)] + '_New.csv', index = False, sep=',')
