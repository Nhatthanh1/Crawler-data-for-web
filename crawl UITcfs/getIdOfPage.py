from itertools import count
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
f2=open('Id.txt','w',encoding='utf-8')
def readData(fileName):
    f = open(fileName, 'r', encoding='utf-8')
    data = []
    for i, line in enumerate(f):
        try:
            line = repr(line)
            line = line[1:len(line) - 3]
            data.append(line)
        except:
            print("error write line")
    return data

def writeFileTxt(fileName, content):
    with open(fileName, 'a') as f1:
        f1.write(content + os.linesep)

def getPostIds(driver, filePath = 'posts.csv'):
    allPosts = readData(filePath)
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    shareBtn = driver.find_elements_by_xpath('//a[contains(@href, "/sharer.php")]')
    if (len(shareBtn)):
        for link in shareBtn:
            postId = link.get_attribute('href').split('sid=')[1].split('&')[0]
            if postId not in allPosts:
                f2.write(postId + '\n')
                writeFileTxt(filePath, postId)

def getnumOfPostFanpage(driver, pageId, amount, filePath = 'posts.csv'):
    driver.get("https://facebook.com/" + pageId)
    while len(readData(filePath)) < amount:
        getPostIds(driver, filePath)

driver = webdriver.Chrome(executable_path=r"E:\chromedriver.exe")
getnumOfPostFanpage(driver, 'ConfessionUIT', 5, 'posts.csv') 
f2.close()