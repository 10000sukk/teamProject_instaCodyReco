from math import *
import pandas as pd
import re
def similarityLossFunction(color_code1 , feature_v1, color_code2 , feature_v2):
    print(color_code1)
    print(color_code2)
    color_code2 = str(color_code2)
    color_code2=re.findall('\d+', color_code2)
    feature_v2=str(feature_v2)
    feature_v2=re.findall('\d+\.*\d*',feature_v2)
    print(feature_v1)
    print(feature_v2)
    c_distance=sqrt(sum(pow(int(a)-int(b),2) for a,b in zip(color_code1,color_code2)))
    f_distance=sqrt(sum(pow(float(a)-float(b),2) for a,b in zip(feature_v1,feature_v2)))
    result=f_distance+c_distance/3
    return result



def recomend(category , pattern, color_code, feature_v, CsvfilePath):
    print("실행")
    df = pd.read_csv(CsvfilePath+'.csv', names = ['category','pattern','color_code','feature_v','path','likes'])
    droplist = []
    for i in range(len(df)):
        if (df.loc[i,'category'] != category) or (df.loc[i,'pattern'] != pattern):
             droplist.append(i)
    df = df.drop(droplist)
    data = df.loc[:,['color_code','feature_v']]
    print(data)
    value = []
    data = data.reset_index(drop=True)
    color_code = str(color_code)
    color_code=re.findall('\d+', color_code)
    for i in range(len(data)):
        print(data.loc[i,'color_code'])
        value.append(similarityLossFunction(color_code, feature_v, data.loc[i,'color_code'], data.loc[i,'feature_v']))
    df['similarity'] = value
    df = df.sort_values(['similarity'], ascending=True)
    df = df.head(15)
    df = df.sort_values(['likes'], ascending=False)
    print(df.loc[:,['path']])
