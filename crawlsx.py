from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import datetime,timedelta
# 1. khai báo biến browser
browser = webdriver.Chrome('C:/Users/TD/new_data/chromedriver')

browser.get("https://www.thantai.net/so-ket-qua")

current_day = datetime(2021,8,14)
data = []
i = 0
while i < 20*365:

    end = browser.find_element_by_id("end")
    end.clear()
    end.send_keys("{}-{}-{}".format(current_day.day,current_day.month,current_day.year))

    button = browser.find_element_by_xpath("/html/body/div[2]/main/div/form/div[2]/div/button[9]")
    button.click()


    KQ = browser.find_elements_by_class_name("font-weight-bold.text-danger.col-12.d-block.p-1.m-0")
    for j in KQ:
        print(j.text)
        data.append(j.text)
        i += 1
    current_day -= timedelta(days= 300)

df = pd.DataFrame(data,columns = ['KQ'])
df.to_csv("SXMB.csv", index = False)

browser.close()