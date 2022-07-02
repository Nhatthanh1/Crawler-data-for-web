from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
y=open('D:\python\crawler\crawl UITcfs\contentpost.txt','w',encoding='utf-8')
f=open('D:\python\crawler\crawl UITcfs\contentcomment.txt', 'w', encoding='utf-8') 

# Khai bao browser
browser = webdriver.Chrome(executable_path=r"E:\chromedriver.exe")
sleep(random.randint(1,5))
def get_content(browser):
    # browser.get("")

    sleep(random.randint(1,5))
    post= browser.find_element_by_class_name("_5pbx")
    post_child=post.find_element_by_tag_name("p")
    y.write(post_child.text)

    sleep(random.randint(1,5))
    show_comments=browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span/a")
    show_comments.click()

    sleep(random.randint(1,5))
    show_comments_more=browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/div/a/div/span")
    show_comments_more.click()

    sleep(random.randint(1,5))

    comment_list = browser.find_elements_by_xpath("//div[@aria-label='Comment']")
    for comment in comment_list:
        # hiển thị tên người và nội dung, cách nhau bởi dấu :
        poster = comment.find_element_by_class_name("_6qw4")
        content = comment.find_element_by_class_name("_3l3x")
        f.write("*" + poster.text + ":" + content.text + '\n')

    sleep(random.randint(1,5))



browser.get("https://www.facebook.com/ConfessionUIT")
sleep(random.randint(1,5))
post_List=browser.find_elements_by_class_name("du4w35lb")
for post in post_List:
    postcfs=post.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/span/span/span[2]/span")
    postcfs.click() 
    get_content(browser)

sleep(random.randint(1,5))
y.close()
f.close()
browser.close()