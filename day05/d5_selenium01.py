from selenium import webdriver as wd
from selenium.webdriver.common.by import By

path = "C:\\PYTHONWORK\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-longging'])
driver = wd.Chrome(path, options=options)
driver.get('https://naver.com')

driver.find_element(By.ID, 'query').send_keys('파이썬')
driver.find_element(By.ID, 'search_btn').click()

# driver.find_element_by_id('query').send_keys('파이썬')
