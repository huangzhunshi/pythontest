import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://yihui:GMYAvsgzE9fRRC1r@mysql-backup.dian.so:3306/oss')

df=pd.read_sql_query("select * from agent_employee where status =0 limit 10",engine)

from datetime import datetime
from datetime import timedelta
#数据处理
df['性别']=df['sex']
# df['性别'].replace('1.0','男')
df.loc[df['性别'] ==1.0,'性别']='男'
df.loc[df['性别']==2.0,'性别']='女'

df['入职日期'] = pd.to_datetime(df['create_time'])

# df['入职日期'] = [datetime.strftime(x,'%Y-%m-%d') for x in df['入职日期']]

df['入职日期'] = [datetime.strftime(x,'%Y-%m') for x in df['入职日期']]

print(df.head(10))

# df['入职日期'].value_counts().sort_index(ascending=True)

df['入职日期'].value_counts().sort_index(ascending=True)

