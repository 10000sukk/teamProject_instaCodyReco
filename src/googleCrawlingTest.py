from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib.request
import argparse
import selenium
import time





searchterm = input('크롤링할 검색어를 입력하십시오:')  # will also be the name of the folder
url = "https://www.google.co.in/search?q=" + searchterm + "&source=lnms&tbm=isch"
# NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
browser = webdriver.Chrome()
browser.get(url)
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
counter = 0
succounter = 0

if not os.path.exists(searchterm):
    os.mkdir(searchterm)

SCROLL_PAUSE_TIME = 0.5


def scrollDown():
    # Get scroll height
    while True:
        last_height = browser.execute_script("return document.body.scrollHeight")
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            else:
                last_height = new_height
                continue


def scroll():
    while True:
        try:
            scrollDown()
            browser.find_element_by_xpath('//*[@id="smb"]').click()
        except:
            break


scroll()

for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print("Total Count:", counter)
    print("Succsessful Count:", succounter)
    print("URL:", json.loads(x.get_attribute('innerHTML'))["ou"])

    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    try:
        with urllib.request.urlopen(json.loads(x.get_attribute('innerHTML'))["ou"]) as f:
            with open('C:\\Users\\김환석\\PycharmProjects\\untitled7\\img\\구글\\색깔\\체크셔츠\\빨강체크셔츠\\red check shirts' "_" + str(counter) + ".jpg", "wb") as h:
                img = f.read()
                h.write(img)

        # imgUrl = i.select_one('.KL4Bh').img['src']
        #     with urlopen(imgUrl) as f:
        #         with open('./img/' + plusUrl + str(n) + '.jpg' , 'wb') as h:
        #             img = f.read()
        #             h.write(img)

        # raw_img = urllib.request.urlopen(req) as f:
        # File = open(os.path.join(searchterm, searchterm + "_" + str(counter) + "." + imgtype), "wb")
        # print(raw_img)
        # File.write(raw_img)
        # File.close()
        succounter = succounter + 1
    except:
        print("can't get img")

print(succounter, "pictures succesfully downloaded")
browser.close()


# from google_images_download import google_images_download
#
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# def imageCrawling(keyword, dir):
#     response = google_images_download.googleimagesdownload()
#
#     arguments = {"keywords":keyword,
#                  "limit":100,
#                  "print_urls":True,
#                  "no_directory":True,
#                  "output_directory":dir}
#
#
#
#     paths = response.download(arguments)
#     print(paths)
#
# imageCrawling("스트라이프맨투맨","C:\\Users\\김환석\\PycharmProjects\\untitled7\\img\\스트라이프맨투맨")