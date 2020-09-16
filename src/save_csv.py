import pandas as pd
import re

#csv에 row한줄 추가해주는 것
def addCSV(category , pattern, color_code, feature_v, path):
    list = []
    numberListInPath = re.findall('\d+', path)
    print(numberListInPath)
    likes = numberListInPath[-1]
    list.extend([[category, pattern, color_code, feature_v, path, likes]])
    dataframe = pd.DataFrame(list)
    dataframe.to_csv("dataset" + ".csv", header=False, index=False,
                     mode='a')

#csv파일을 likes수로 정렬해주는것
#savepath 인자는 현재 csv파일이 저장된 경로
def sortCSVwithLikes(savepath):
    df = pd.read_csv(savepath+'.csv', names = ['category','pattern','color_code','feature_v','path','likes'])
    df2 = df.sort_values(['likes'], ascending = False)
    df2 = df2.reset_index(drop= True)
    df2.to_csv(savepath+'.csv', mode='w')
