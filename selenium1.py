from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

# create the driver
website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'E:\E_Code\chromedriver-win64\chromedriver.exe' # path of my chrome driver
driver = webdriver.Chrome(path)
driver.get(website)

# get the button
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain') # everytime we change it the site reloads
# but it slow, but we need to use wait to wait for the website to respond
time.sleep(3) # stop for 3 seconds and execute the next codes

date = []
home_team = []
score = []
away_team = []
# extract data from a table
matches = driver.find_elements_by_tag_name('tr') # return a list
for match in matches:
    # use current context therefore the '.'
    date.append(match.find_element_by_xpath('./td[1]').text)
    home = match.find_element_by_xpath('./td[2]').text
    home_team.append(home)
    # print(home)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)

driver.quit() # close the window
    
df = pd.DataFrame({'date': date, 'home_tean':home_team,
              'score':score, 'away_team':away_team})
df.to_csv("football_data.csv", index=False)
print(df)