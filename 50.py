import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data_source/news+aggregator/newsCorpora.csv', sep='\t', header=None)
df.columns = ['ID','TITLE','URL','PUBLISHER','CATEGORY','STORY','HOSTNAME','TIMESTAMP']
df_filter = df[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]

train, valid_test = train_test_split(df_filter, test_size=0.2, stratify=df_filter['CATEGORY'])
valid, test = train_test_split(valid_test, test_size=0.5, stratify=valid_test['CATEGORY'])

train.to_csv('data_source/50/train.txt', sep='\t', index=False)
valid.to_csv('data_source/50/valid.txt', sep='\t', index=False)
test.to_csv('data_source/50/test.txt', sep='\t', index=False)

