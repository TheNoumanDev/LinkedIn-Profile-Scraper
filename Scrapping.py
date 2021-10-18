from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

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

def link_generator(country,typee,num):
    f_l = 'https://www.linkedin.com/search/results/'
    m_l = '/?keywords='
    r_l = '&origin=SWITCH_SEARCH_VERTICAL&page='
    l_l = '&sid=cZR'
    return f_l + typee + m_l + country + r_l + str(num) + l_l

driver = webdriver.Chrome(executable_path = "C:\\Users\m_nou\Downloads\chromedriver_win32 (1)\chromedriver.exe")
link = "https://www.linkedin.com/"
driver.get(link)

login()

Country = "Pakistan" # User can select any country 
typee = "people" # it could be People or Companies
no_of_profiles =  '100'

i = 2
j = 64
while(True):
    if (i== 100):
        Country = chr(j + 1)
        j = j + 1
        i = 2
        link = link_generator(Country,typee,i)
    else:
        link = link_generator(Country,typee,i)
    driver.get(link)
    content = driver.page_source
    main = BeautifulSoup(content,'html.parser')
    s = main.findAll('li',attrs = {'class' : 'reusable-search__result-container' })
    for profile in s:
        pro = []
        time.sleep(2)
        pro_link = profile.find('a')['href']
        driver.get(pro_link)
        print(pro_link)
        sub = BeautifulSoup(driver.page_source,'html.parser')
        data = sub.find('div',attrs = {'class' : 'ph5 pb5'})
        if(data == None):
            data = sub.find('div',attrs = {'class' : 'ph5 '})
        try:
            name = data.find('div',attrs = {'class' : 'mt2 relative'}).find('h1').text
        except:
            name = ""
        try:
            job = data.find('div',attrs = {'class' : 'mt2 relative'}).find('div',attrs = {'class' : 'text-body-medium break-words'}).text.split("\n")[1]
        except:
            job = ""
        try:
            comp = data.find('div',attrs = {'class' : 'mt2 relative'}).find('ul',attrs = {'class': 'pv-text-details__right-panel'}).find('li',attrs = {'class': 'pv-text-details__right-panel-item'}).find('div').text.split("\n")[2]
        except:
            comp = ""
        try:
            address = data.find('div',attrs = {'class' : 'mt2 relative'}).find('div',attrs = {'class': 'pb2 pv-text-details__left-panel'}).find('span').text.split("\n")[1]
            try:
                country = address.split(",")[len(address.split(","))-1]
            except:
                country = Country
        except:
            address = ""
            country = Country
        try:
            connections = data.find('ul',attrs = {'class':'pv-top-card--list pv-top-card--list-bullet display-flex pb1'}).find('li',attrs = {'class':'text-body-small'}).text.split(" ")[0].split("\n")[2]
        except:
            connections = ""
        try:
            username = pro_link.split("/")[4].split("?")[0]
        except:
            username = ""
        """try:
            print("try")
            #.find('span',attrs = {'class':'align-self-center t-14 t-black--light'})
        except:
            followers = 
        followers = sub.find('div',attrs = {'class' : 'pv-deferred-area ember-view'}).find('section',attrs = {'class':'pv-profile-section pv-recent-activity-section-v2 artdeco-card p5 mt4 ember-view'}).text """
        pro.append(name.strip())
        pro.append(job.strip())
        pro.append(comp.strip())
        pro.append(address.strip())
        pro.append(country.strip())
        pro.append(connections.strip())
        pro.append(username.strip())
        if(name.strip() != ""):
            
            print(pro)
        # opening the csv file in 'a+' mode
            with open('profiles.csv', 'a+',encoding="utf-8",newline='') as file:
                myfile = csv.writer(file)
                myfile.writerow(pro)
        driver.back()
    i = i + 1