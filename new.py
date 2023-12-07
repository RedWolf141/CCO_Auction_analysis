from fnmatch import fnmatch
from lib2to3.pgen2 import driver
from multiprocessing import set_forkserver_preload
from operator import truth
from re import I
from scipy import rand
from scipy.misc import derivative
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from sympy import E, sec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from math import ceil
import os.path

import schedule
import time
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920*1080")
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument("Content-Type=application/json; charset=utf-8")

class ResponsiveScreen:
	def __init__(self, urls):
		self.browser = webdriver.Chrome(ChromeDriverManager().install)
		self.browser.maximize_window()
		self.urls = urls
		self.sizes = [480,960,1360,1920]
	
	def screenshot(self, url):
		BROWSER_HEIGHT = 1027
		self.browser.get(url)
		for size in self.sizes:
			self.browser.set_window_size(size, BROWSER_HEIGHT)
			self.browser.execute_script("window.scrollTo(0,0)")
			time.sleep(3)
		scroll_size = self.browser.execute_script (
			"return document.body.scrollHeight"
		)
		total_sections = ceil(scroll_size / BROWSER_HEIGHT)

		for section in range(total_sections +1):
			self.browser.execute_script (
				f"window.scrollTo(0, {section * BROWSER_HEIGHT})"
			)
			time.sleep(2)
			self.browser.save_screenshot(f"screenshots/{size}x{section}.png")
	
	def start(self):
		for url in self.urls:
			self.screenshot(url)
	
	def finish(self):
		self.browser.quit()

def doScreenShot():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('https://cybercodeonline.com')

    driver.find_element_by_xpath('//*[@id="main"]/div/ion-content/div/div[5]/p').click()
    #driver.find_element_by_xpath('//*[@id="main"]/div/ion-content/div/div[4]/div[4]').click()

    driver.implicitly_wait(1000)

    #아이디
    driver.find_element_by_class_name("h-8  ").send_keys("wolf141@furry.com")
    driver.implicitly_wait(1000)
    #비밀번호
    driver.find_element_by_xpath('//*[@id="main"]/div/ion-content/div/div[4]/div[2]/div[2]/div[2]/div/input').send_keys("qwer1234")
    driver.implicitly_wait(1000)

    #로그인
    driver.find_element_by_xpath('//*[@id="main"]/div/ion-content/div/div[4]/div[3]/div[2]/a/span').click()
    driver.implicitly_wait(1000)

    #한글패치
    driver.find_element_by_xpath('//*[@id="root"]/ion-app/div[4]/div/div/div/div[4]/div[2]/div').click()
    driver.implicitly_wait(1000)

    #둘러보기
    driver.find_element_by_xpath('//*[@id="main"]/div/ion-tabs/div/ion-router-outlet/div/ion-content/div/div/div[3]/span/span').click()
    time.sleep(3)

    #메테리얼
    driver.find_element_by_xpath('//*[@id="main"]/div[2]/ion-content/div/div[13]').click()
    time.sleep(5)

    #AI core
    driver.find_element_by_xpath('//*[@id="main"]/div[3]/ion-content/div/div[1]').click()
    time.sleep(5)
    i = 1
    msg = f"screen{i}.png"

    while True:
        msg = f"screen{i}.png"
        if (not os.path.isfile(msg)):
            msg = f"screen{i}.png"
            now = datetime.now()
            print("지금은", now.year, "년", now.month, "월", now.day, "일", now.hour, "시", now.minute, "분", now.second, "초입니다. \n")
            break

        i += 1
    driver.save_screenshot(f"./screen{i}.png")
    time.sleep(5)


#플레이어 마켓
#driver.find_element_by_xpath('//*[@id="main"]/div/ion-tabs/div/ion-router-outlet/div/ion-content/div/div/div[4]/span[4]/div/span').click()



schedule.every(1).hour.do(doScreenShot)
doScreenShot()
while True:
	schedule.run_pending()
	time.sleep(1)
while (True):
    pass
