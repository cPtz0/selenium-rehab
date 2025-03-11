# 各類模組
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# PATH 指向chromedriver位置
Service = Service('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
# 指定使用Chrome做為控制模組
driver = webdriver.Chrome(service=Service)
# 開始進行操作
# 首先導向特定位置
driver.get("https://www.google.com")
driver.maximize_window()
# 練習：尋找element
#這裡尋找搜尋框
#search_box = driver.find_element(By.NAME,'q')
#search_box = driver.find_element(By.ID,'APjFqb')
#search_box = driver.find_element(By.CLASS_NAME,'gLFyf')
#search_box = driver.find_element(By.TAG_NAME,'textarea')
#注意XPATH計算從1開始
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea')

search_box.send_keys('Selenium')
search_box.submit()

time.sleep(3)