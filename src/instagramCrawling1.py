from urllib.parse import quote_plus #아스키 코드로 변환해준다
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
import urllib.request
import os

#database연결하기
#자신의 host, dbname, user, password에 맞게 입력
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='ghks2122',
#                              db='instagram_dailylook',
#                              charset='utf8',
#                              cursorclass=pymysql.cursors.DictCursor)
#


def notMatch(list, a):
    n = 0
    for i in list:
        if a == i:
            n = 1
            break
    if n == 1:
        return 0
    else:
        return 1


baseUrl1 = 'https://www.instagram.com/explore/tags/'
baseUrl2 = '/?hl=ko'
plusUrl = input('크롤링할 해시태그를 입력하시오: ')
url = baseUrl1 + quote_plus(plusUrl) +baseUrl2

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()
time.sleep(3)
driver.find_element_by_name("username").send_keys("bcrhs4460@gmail.com")#아이디 입력
driver.find_element_by_name("password").send_keys("bcrhs147") #비밀번호 입력
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click() #로그인버튼 클릭
time.sleep(3)
#driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[3]/form/span/button').click()
#time.sleep(3)
#driver.find_element_by_xpath('//*[@id="security_code"]').send_keys(str(input('6자리 보안코드를 입력하시오:')))
#driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[2]/form/span/button').click()
#time.sleep(5) #위에서 불러오고 3초 기다린후에 분석을 시작

reallist =[]
list1 = [] #old list
list2 = [] #new list
pageString = driver.page_source
soup = BeautifulSoup(pageString, features='html.parser')
# totalCount = soup.find(name='span', attrs={'class': 'g47SY '}).get_text()
# print("총 게시물수 : " + totalCount)
count = csvList = os.walk('C:\\Users\\김환석\\PycharmProjects\\untitled7\\img\\cody\\코디testSet\\인플루엔서').__next__()[2]

alt = re.compile('.*사람 1명 이상.*사람들이 서 있음.*')

list1 = soup.find_all(name='div', attrs={'class': 'Nnq7C weEfm'})
for i in list1:
    temp = i.find_all(name='div', attrs={'class': 'v1Nh3 kIKUG _bz0w'})
    for j in temp:
        try:
            img = j.find('img')
            if alt.match(str(img.attrs['alt'])) != None:
                imgUrl = img.attrs['src']
                print(imgUrl)
                urllib.request.urlretrieve(imgUrl,
                                           "C:\\Users\\김환석\\PycharmProjects\\untitled7\\img\\cody\\코디testSet\\인플루엔서\\celebcody" + "(" + str(
                                               count) + ").jpg")
                time.sleep(0.1)
                count += 1
        except:
            print('다운로드 실패')
            continue



SCROLL_PAUASE_TIME = 3
n = 1



while True:
    time.sleep(SCROLL_PAUASE_TIME)
    #스크롤을 내려준다
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUASE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUASE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        else:
            last_height = new_height
            continue

    time.sleep(SCROLL_PAUASE_TIME)
    #다시 파싱한다
    pageString = driver.page_source
    soup = BeautifulSoup(pageString, features='html.parser')
    list2 = soup.find_all(name='div', attrs={'class': 'Nnq7C weEfm'})

    for i in range(10, len(list2)):
        try:
            if notMatch(list1, list2[i]) == 1:
                temp = list2[i].find_all(name='div', attrs={'class': 'v1Nh3 kIKUG _bz0w'})
                for j in temp:
                    try:
                        img = j.find('img')
                        if alt.match(str(img.attrs['alt'])) != None:
                            imgUrl = img.attrs['src']
                            urllib.request.urlretrieve(imgUrl,
                                                       "C:\\Users\\김환석\\PycharmProjects\\untitled7\\img\\cody\\코디testSet\\인플루엔서\\celeb_cody" + "(" + str(
                                                           count) + ").jpg")
                            time.sleep(0.1)
                            count += 1
                    except:
                        continue


        except:
            print('다운로드 실패')
            continue
    list1 = list2
##while 문의 끝

#사진 url로 pc에 저장하는것
#urllib.request.urlretrieve(j.attrs['herf'], "C:\\Users\\김환석\\PycharmProjects\\untitled7\\img\\인스타\\" + str(plusUrl) + "(" + str(fileNumber) + ")" + ".jpg")
