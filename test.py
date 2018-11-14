import pandas as pd

d1 = {'id':[1,2,3,4],'emo':[0.1,0.3,0.4,0.7],"loc":['','','','']}
d2 = {'id':[1,2,5,7],'loc': ['bj','sh','sc','gz']}

f1 = pd.DataFrame(d1)
f2 = pd.DataFrame(d2)
