################
#무신사 크롤링 하는것
#######3
import urllib
from idlelib import browser
import urllib.request
from urllib.parse import quote_plus #아스키 코드로 변환해준다
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pymysql
import re
import pandas as pd
import json



#해당 페이지를 크롤링 i가 페이지번호
def musinsaCrawling(pageNum):
    baseUrl = 'https://store.musinsa.com/app/product/search?search_type=1&q='
    baseUrl1 = '&page='
    url = baseUrl + quote_plus(plusUrl) + baseUrl1 + str(pageNum)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)  # 위에서 불러오고 1초 기다린후에 분석을 시작

    pageString = driver.page_source
    soup = BeautifulSoup(pageString, features="html.parser")

    result1 = soup.find(name = 'ul', attrs ={'class':'snap-article-list boxed-article-list article-list center list goods_small_media8'})
    result2 = result1.find_all(name = "img")

    for i in result2:
        try:
            image = i.attrs['data-original']
            reallink.append(image)
        except:
            continue

    print(reallink)
    driver.close()



#database연결하기
#자신의 host, dbname, user, password에 맞게 입력
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='ghks2122',
#                              db='instagram_dailylook',
#                              charset='utf8',
#                              cursorclass=pymysql.cursors.DictCursor)
#


plusUrl = input('검색할 옷을 입력하시오: ')
reallink = []


baseUrl = 'https://store.musinsa.com/app/product/search?search_type=1&q='
baseUrl1 = '&page=1'
url = baseUrl + quote_plus(plusUrl) + baseUrl1
driver = webdriver.Chrome()
driver.get(url)

time.sleep(3) #위에서 불러오고 3초 기다린후에 분석을 시작


pageString = driver.page_source
soup = BeautifulSoup(pageString, features="html.parser")
pageNum = int((soup.find("span",{"class" : "totalPagingNum"})).text)
print(pageNum)
driver.close()



for i in range(1,pageNum+1):
    musinsaCrawling(i)


print(reallink)






n = 1
for i in range(0,len(reallink)):
    urllib.request.urlretrieve( "http:"+reallink[i],"C:\\Users\\김환석\\PycharmProjects\\untitled7\\img\\무신사\\꽃무늬셔츠\\flowershirts" + "("+str(n)+")"+".jpg")
    n +=1




############################

#
# for link in links:
#     img = link.select('img')
#     imgUrl = img.attr['src']
#     print(imgUrl)

# insta = soup.find_all(name="div", attrs={"class":"right_contents"})
# box = insta.select_all('')

#
# n = 1
# for i in insta:
#     print('https://store.musinsa.com/' + i.a['href'])
#     imgUrl = i.select_one('list_img').img['src']
#     print("imgUrl = {}" , imgUrl)
    # with urlopen(imgUrl) as f:
    #     with open('./img/' + plusUrl + str(n) + '.jpg' , 'wb') as h:
    #         img = f.read()
    #         h.write(img)
    # n += 1
    # print(imgUrl)
    # print()

