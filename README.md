## 代码说明

## `get_table_name.py`

从`shenzhen`, `shanghai` , `chuangyeban` ,`zhongxiaoban` 四个数据库中获取表名称, 分别存为`
shenzhen.csv` ,` shanghai.csv` ,` chuangyeban.csv` ,` zhongxiaoban.csv`.

The table lists are now located under:

    `/data4/yqhuang/database_table_list/`

You do not have run this code again.

## `sentiment_score.py`

定义了一些需要用到的函数和sentiment_score类

- `connect_database`  用于连接数据库,输入数据库名称
- `select_from_table` 用于从表中筛选信息,输入表名称,数据库连接,输出筛选的信息(list)
- `get_table_name_list` 用于获得数据库中表名称,输入数据库名称以及数据库连接,输出表名称(list)
- `open_dict` 用于导入情感词典
- `match` 用于匹配从数据库中得出的信息和sas文件的地点信息,输入数据库名称以及股票编号,输出匹配好的csv文件
- `sentiment_score` 进行情感打分,输入为单条文本信息,返回分数

## `main.py`

- `par1`: 为数据库名称(测试时使用shenzhen,因为只有这个的sas文件拆了)先读入存有数据库所有表名称的
csv文件,将数据库名称以及股票编号分别存为list然后连接数据库,对数据库中第一到第三个表(在测试
中为000001,000002,000004)进行打分,存为[股票编码]_sentiment.csv文件
(000001_sentiment.csv,000002_sentiment.csv,000004_sentiment.csv)关闭数据库连接最后对一至三表的
csv文件信息和sas文件五个地点信息进行匹配,输出[股票编码]_match.csv文件
(000001_match.csv,000002_match.csv,000004_match.csv)

- `par2`: The table list for `par1`

- `par3`: Percentage for the table list to process.

### 运行方式

    python3 main.py shenzhen /data4/yqhuang/database_table_list/shenzhen.csv 5

完成`shenzhen数`据库中`4%-5%`的股票的情感打分以及匹配
输出：

- `[股票编码]_sentiment.csv [股票编码]_match.csv`
- `5.csv`  中会有4%-5%的股票编码
