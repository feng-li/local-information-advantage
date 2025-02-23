# -*- coding: utf-8 -*-

import pymysql
import re
import pandas as pd
from sentiment_score import get_table_name_list, connect_database

database_list = ['chuangyeban','shanghai','shenzhen','zhongxiaoban']
for database in database_list:
    con = connect_database(database)
    table_list = get_table_name_list(database, con)
    con.close()
    df = pd.DataFrame(table_list)
    df.to_csv(str(database)+'.csv',index = False, header = False)
