import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path =r'C:\Users\huyan\Desktop\Time Series'
company_list = ['AAPL_data.csv','GOOG_data.csv','MSFT_data.csv','AMZN_data.csv']
all_data = pd.DataFrame()
for file in company_list:
    current_df=pd.read_csv(path+'/'+file)
    all_data = pd.concat([all_data,current_df])
all_data.shape

all_data.head()

tech_list = all_data['Name'].unique()

for i, company in enumerate (tech_list,1):
    plt.subplot(2,2,i)
    df=all_data[all_data['Name']==company]
    plt.plot(df['date'],df['close'])
    plt.title(company)

import plotly.express as px

for company in tech_list:
    df = all_data[all_data['Name']==company]
    fig = px.line(df, x = 'date', y ='volume', title = company)
    fig.show()

pip install plotly

df = pd.read_csv(r'C:\Users\huyan\Desktop\Time Series/AAPL_data.csv')
df.head()

df['Daily_Price_change']= df['close']-df['open']
df.head()

df['1day % return']=((df['close']-df['open'])/df['close'])*100
df.head()

fig = px.line(df, x = 'date', y ='1day % return', title = company)
fig.show()

df2= df.copy()
df2.dtypes

df2['date'] =pd.to_datetime(df2['date'])
df2.set_index('date',inplace=True)
df2.head()
df2['2013-02-08':'2013-02-14']

df2['close'].resample('M').mean().plot()

df2['close'].resample('Y').mean().plot(kind='bar')

aapl = pd.read_csv(r'C:\Users\huyan\Desktop\Time Series/AAPL_data.csv')
amzn = pd.read_csv(r'C:\Users\huyan\Desktop\Time Series/AMZN_data.csv')
msft = pd.read_csv(r'C:\Users\huyan\Desktop\Time Series/MSFT_data.csv')
goog = pd.read_csv(r'C:\Users\huyan\Desktop\Time Series/GOOG_data.csv')

close=pd.DataFrame()
close['aapl']=aapl['close']
close['amzn']=amzn['close']
close['msft']=msft['close']
close['goog']=goog['close']

close.head()

import seaborn as sns
sns.pairplot(data=close)

sns.heatmap(close.corr(),annot = True)

aapl.head()

data=pd.DataFrame()

data['aapl_change']= ((aapl['close']-aapl['open'])/aapl['close'])*100
data['amzn_change']= ((amzn['close']-amzn['open'])/amzn['close'])*100
data['msft_change']= ((msft['close']-msft['open'])/msft['close'])*100
data['goog_change']= ((goog['close']-goog['open'])/goog['close'])*100
data.head()

sns.pairplot(data=data)
sns.heatmap(data.corr(),annot = True)
data.describe().T

