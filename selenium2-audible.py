from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options # for headless 
import time

# for explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options  = Options()
# options.add_argument('--headless')
options.headless = False
# options.add_argument('window-size=1920x1080')

web = "https://www.audible.com/adblbestsellers" # define our target search
path = r'E:\E_Code\chromedriver-win64\chromedriver.exe' # path of my chrome driver
driver = webdriver.Chrome(path, options=options)
driver.get(web)



driver.maximize_window() # have the window display all over the screen

# pagination
pagination = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text) # the last one is the arrow, the last page is by -2, return the max page number

next_page = driver.find_element_by_xpath('//span[contains(@class, "nextButton")]')
next_page.click() # click on the next page button

# make it stop at the last page
current_page = 1
book_title = []
book_author = []
book_length = []

while current_page <= last_page:
    # time.sleep(2) # implicit wait
    # maximum waiting for 10 seconds
    container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"adbl-impression-container")))
    # container = driver.find_element_by_class_name('adbl-impression-container')
    # products = container.find_elements_by_xpath('.//li[contains(@class,"productListItem")]')
    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located(By.XPATH,'.//li[contains(@class,"productListItem")]'))

    # scrap the title, author and audio time
    for product in products:
        book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

    current_page = current_page + 1

    try:
        next_page = driver.find_element_by_xpath('//span[contains(@class, "nextButton")]')
        next_page.click() # click on the next page button
    except:
        pass


driver.quit()
df_books = pd.DataFrame({'title':book_title, 'author':book_author, 'length':book_length})
df_books.to_csv("books_pagination.csv",index=False)
