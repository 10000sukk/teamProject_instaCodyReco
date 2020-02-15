from urllib.parse import quote_plus #아스키 코드로 변환해준다
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd


baseUrl = 'https://www.google.com/search?q='
baseUrl1 = '&tbs=vw:g,ss:44&tbm=shop&sxsrf=ACYBGNRC497BvU3VU_yrCAY0c-L7veiLXQ:1573802781909&ei=HVPOXemFN8bj-AatmqfgDw&start=0&sa=N&ved=0ahUKEwipiIye2OvlAhXGMd4KHS3NCfw48AEQ8tMDCFE&biw=1536&bih=706'
plusUrl = input('검색할 옷을 입력하시오: ')
url = baseUrl + quote_plus(plusUrl) + baseUrl1 + str(pageNum)
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)  # 위에서 불러오고 3초 기다린후에 분석을 시작

pageString = driver.page_source
soup = BeautifulSoup(pageString, features="html.parser")

result = soup.findAll("div", {"class": "list_img"})