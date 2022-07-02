# import scrapy

# class BlogSpider(scrapy.Spider):
#     name = 'blogspider'
#     start_urls = ['https://www.zyte.com/blog/']

#     def parse(self, response):
#         for title in response.css('.oxy-post-title'):
#             yield {'title': title.css('::text').get()}

#         for next_page in response.css('a.next'):
#             yield response.follow(next_page, self.parse)
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# Khai báo browser

browser = webdriver.Chrome(executable_path=r"E:\chromedriver.exe")
# 2. Test open 1 website
browser.get("https://fb.com")
a="12333"
b="123"
# Điền thông tin vào ô user và passwords
txtUser=browser.find_element_by_id("email")
txtUser.send_keys(a)
txtPass=browser.find_element_by_id("pass")
txtPass.send_keys(b)
txtPass.send_keys(Keys.ENTER)

# Dừng chương trình 5s
# sleep(5)
# #4. Đóng trình duyệt
# browser.close()