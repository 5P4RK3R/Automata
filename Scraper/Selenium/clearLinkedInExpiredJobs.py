import time
# from turtle import clear
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver = webdriver.Safari()
driver.get('https://www.linkedin.com')
driver.fullscreen_window()

sessionKey = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
sessionPassword = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))
# sessionKey  = driver.find_element_by_id('session_key')
# sessionPassword  = driver.find_element_by_id('session_password')
signInBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "sign-in-form__submit-button")))
# signInBtn = driver.find_element(by=By.CLASS_NAME,value='sign-in-form__submit-button')
# print(signInBtn)
sessionKey.clear()
sessionKey.send_keys('mahendransparker@gmail.com')
sessionPassword.clear()
sessionPassword.send_keys('gojuryu45')
signInBtn.click()

time.sleep(15)
Jobs = driver.find_element(by=By.XPATH,value="//span[@title='Jobs']")
print(Jobs)
# Jobs = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@data-control-name='jobshome_nav_my_jobs']")))
Jobs.click()
time.sleep(5)

# MyJobs = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@data-link-to='jobs']")))
MyJobs = driver.find_element(by=By.XPATH,value="//a[@data-control-name='jobshome_nav_my_jobs']")

MyJobs.click()
# elem = driver.find_element(by=By.CLASS_NAME,"")
# savedJobs = driver.find_element(by=By.XPATH,value="//button[@aria-label='Saved']")
# print(savedJobs)
# expiredJobs = driver.find_elements(by=By.XPATH,value="//span[@class='entity-result__title-text']")
# expiredJobs = driver.find_elements(by=By.CLASS_NAME,value="entity-result__title-text")
# # expiredJobs = WebDriverWait(driver,10).until(EC._element_if_visible((By.CLASS_NAME,"entity-result__simple-insight-text")))
# for job in expiredJobs:
#     print(job)
time.sleep(50)
driver.quit()