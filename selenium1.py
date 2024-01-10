from selenium import webdriver


# create the driver
website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'E:\E_Code\chromedriver-win64\chromedriver.exe' # path of my chrome driver
driver = webdriver.Chrome(path)
driver.get(website)
driver.quit() # close the window