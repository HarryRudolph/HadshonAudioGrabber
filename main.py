import time

from selenium import webdriver

url = "https://hadshon.edu.gov.il/"

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')

driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
time.sleep(5)
print(driver.title)
