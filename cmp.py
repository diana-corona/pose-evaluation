
import pandas as pd
import numpy as np
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('input', nargs=2)

df1, df2 = parser.parse_args().input

df1 = pd.read_pickle(df1)
df2 = pd.read_pickle(df2)
df1 = df1.dropna()
df2 = df2.dropna()

df1 = df1.sort_values(by=['file_name', 'frame_number'])
#df2 = df1.sort_values(by=['file_name', 'frame_number'], ascending=False)
df2 = df2.sort_values(by=['file_name', 'frame_number'])
df1_dic = {} 
df2_dic = {} 

for i in range(df1.shape[0]):
  file_name = str(df1['file_name'].iloc[i].split('.')[0])+str(df1['frame_number'].iloc[i])
  df1_dic[file_name] = df1['value'].iloc[i]

for i in range(df2.shape[0]):
  file_name = str(df2['file_name'].iloc[i].split('.')[0])+str(df2['frame_number'].iloc[i])
  df2_dic[file_name] = df2['value'].iloc[i]

scores = []
for key in df1_dic.keys():
  if key in df2_dic.keys():
    scores.append(np.mean(np.abs(df1_dic[key] - df2_dic[key]).astype(float)))
  else:
    print(key)
#assert df1.shape == df2.shape

print ("Average difference: %s" % np.mean(scores))
