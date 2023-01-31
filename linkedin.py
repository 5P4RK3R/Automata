import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
driver = webdriver.Safari()
driver.fullscreen_window()
driver.get("https://www.linkedin.com/jobs/search/?geoId=102713980&location=India")
scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1
j = 1
while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        time.sleep(5)
        try:
            see_more_job = driver.find_element(by=By.XPATH,value="//button[@data-tracking-control-name='infinite-scroller_show-more']")
            see_more_job.click()
            
        except:
            j += 1
            if j==2:
                break
            continue
        else:
            break
  

### GET Jobs
websites = []
Jobs = driver.find_elements(by=By.XPATH,value="//ul[@class='jobs-search__results-list']//li")
for i,job in enumerate(Jobs):
    companies = {}
    try:
        time.sleep(2)   
        driver.execute_script("arguments[0].scrollIntoView();", job)
        job.click()
        company = driver.find_element(by=By.XPATH,value="//a[@data-tracking-control-name='public_jobs_topcard-org-name']")
        anchors = driver.find_element(by=By.XPATH,value="//a[@data-tracking-control-name='public_jobs_apply-link-offsite']")
        companies['name'] = company.text.strip()
        companies['url'] = anchors.get_attribute('href')
        websites.append(companies)
    except Exception as e:
        pass
data = {site['name']:site['url'] for site in websites}

obj = {}
obj["company"] = data.keys()
obj["url"] = data.values()
df = pd.DataFrame(obj)
df.to_csv("details.csv", sep='\t', encoding='utf-8')

driver.quit()