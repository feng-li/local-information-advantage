
## 代码说明

### get_table_name.py 
从shenzhen,shanghai,chuangyeban,zhongxiaoban四个数据库中获取表名称,分别存为shenzhen.csv,shanghai.csv,chuangyeban.csv,zhongxiaoban.csv

### emotion_score.py 
定义了一些需要用到的函数和emotion_score类  
1.**connect_database**用于连接数据库,输入数据库名称  
2.**select_from_table**用于从表中筛选信息,输入表名称,数据库连接,输出筛选的信息(list)  
3.**get_table_name_list**用于获得数据库中表名称,输入数据库名称以及数据库连接,输出表名称(list)  
4.**open_dict**用于导入情感词典  
5.**match**用于匹配从数据库中得出的信息和sas文件的地点信息,输入数据库名称以及股票编号,输出匹配好的csv文件  
6.**emotion_score**进行情感打分,输入为单条文本信息,返回分数

###test.py
参数为数据库名称(测试时使用shenzhen,因为只有这个的sas文件拆了)  
先读入存有数据库所有表名称的csv文件,将数据库名称以及股票编号分别存为list  
然后连接数据库,对数据库中第一到第三个表(在测试中为000001,000002,000004)进行打分,存为[股票编码]_emotion.csv文件(000001_emotion.csv,000002_emotion.csv,000004_emotion.csv)  
关闭数据库连接  
最后对一至三表的csv文件信息和sas文件五个地点信息进行匹配,输出[股票编码]_match.csv文件(000001_match.csv,000002_match.csv,000004_match.csv)

###运行方式
python3 test.py shenzhen 5
完成shenzhen数据库中4%-5%的股票的情感打分以及匹配  	
输出：[股票编码]_emotion.csv [股票编码]_match.csv 5.csv  	
5.csv中会有4%-5%的股票编码


