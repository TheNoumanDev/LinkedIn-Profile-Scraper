from selenium import webdriver
from bs4 import BeautifulSoup
import time

def login():
    signInButton = driver.find_element_by_xpath('/html/body/nav/div/a[2]')
    signInButton.click()
    #time.sleep(5)

    email = driver.find_element_by_xpath('//*[@id="username"]')
    email.send_keys('m_nouman@hotmail.com')
    #time.sleep(5)
    passs = driver.find_element_by_xpath('//*[@id="password"]')
    passs.send_keys('wolfie_54321')

login = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login.click()
 

driver = webdriver.Chrome(executable_path = "C:\\Users\m_nou\Downloads\chromedriver_win32 (1)\chromedriver.exe")
link = "https://www.linkedin.com/"
driver.get(link)
