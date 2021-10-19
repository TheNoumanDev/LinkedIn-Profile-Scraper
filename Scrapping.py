# Name : 'Muhammad Nouman Butt' & 'Rafaqat Hussain'

from selenium import webdriver  
from bs4 import BeautifulSoup
import time
import csv

# This Function will login an provided account to linkedIn to use it in web browser.

def login():
    signInButton = driver.find_element_by_xpath('/html/body/nav/div/a[2]') # This will find SignIn Button on webBrowser.
    signInButton.click()
    time.sleep(5)

    email = driver.find_element_by_xpath('//*[@id="username"]')           # This Will find the Username Text box
    email.send_keys('m_nouman@hotmail.com')                               # Provided username will be sent to the TextBox

    time.sleep(5)
    passs = driver.find_element_by_xpath('//*[@id="password"]')           # This Will find the Password Text box
    passs.send_keys('wolfie_54321')                                       # Provided Password will be sent to the TextBox

    login = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')   # This will again find the signIn button 
    login.click()                                                                       # and press it using click() function

# This Function will generate a new Link for everytime it will be called based on its parameters.
def link_generator(country,typee,num):
    f_l = 'https://www.linkedin.com/search/results/'
    m_l = '/?keywords='
    r_l = '&origin=SWITCH_SEARCH_VERTICAL&page='
    l_l = '&sid=cZR'
    return f_l + typee + m_l + country + r_l + str(num) + l_l

# This portion will Open a Chrome Webdriver and opens LinkedIn Page.
driver = webdriver.Chrome(executable_path = "C:\\Users\m_nou\Downloads\chromedriver_win32 (1)\chromedriver.exe")
link = "https://www.linkedin.com/"
driver.get(link)

login() # After Opening WebDriver Login Function is called to login into provided account

Country = "Pakistan"      # User can select any country 
typee = "people"          # it could be People or Companies
no_of_profiles =  '100'   # user can also select the number of profiles he wanna scrabe.

i = 2 # used for turning pages
j = 64 # used for changing search Keyword
while(True):
    if (i== 100):  # if pages reach 100 then Keyword will be changed and new 100 pages will load
        Country = chr(j + 1)
        j = j + 1
        i = 2      # and i will again set to 2nd page and new link will be generated 
        link = link_generator(Country,typee,i)
    else:
        link = link_generator(Country,typee,i)
    driver.get(link)
    content = driver.page_source
    main = BeautifulSoup(content,'html.parser')  # Here all the present page content will be soup into Main.
    s = main.findAll('li',attrs = {'class' : 'reusable-search__result-container' })  # All Present profiles Div will be stored into "s"

    # This for loop will take one profile from 's' and Extract data from each profile.
    for profile in s:
        pro = []
        time.sleep(8)
        pro_link = profile.find('a')['href']  # This will get Profile Link of the user and will open it in same driver.
        driver.get(pro_link)
        #print(pro_link)
        # From here One by one All data wil be Scraped and if in some Profile Data is not present it will not cause error. It will just skip the entity.
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
        
        # Here Data is being stored into List. Strip function is used to remove any extra spaces which is sometimes caused.
        pro.append(name.strip())
        pro.append(job.strip())
        pro.append(comp.strip())
        pro.append(address.strip())
        pro.append(country.strip())
        pro.append(connections.strip())
        pro.append(username.strip())
        if(name.strip() != ""):       #if someone's data is not found then it will not store empty data into CSv File.
            print(pro)

            # opening the csv file in 'a+' mode allows the user to save new data keeping the previous data as well.
            # If utf-8 is not used a Error will be cause and it newline is not used then it will skip one line everytime while Storing list.
            with open('profiles.csv', 'a+',encoding="utf-8",newline='') as file:
                myfile = csv.writer(file)
                myfile.writerow(pro)
        driver.back() # After Scraping a specific profile driver will be brought back to the pages.
    i = i + 1         # increment for pages.