import time
import requests


from selenium import webdriver

url = "https://hadshon.edu.gov.il/wp-content/uploads/2020/09/%D7%9E%D7%93324%D7%A6.mp3?_=1"

path = "/Users/Harry/test/test.mp3"

#time.sleep(5)

r = requests.get(url, verify=False)

f = open(path, "wb")
f.write(r.content)
print(r)
