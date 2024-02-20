## Python Basics for WebScraping

- Open files
To create a file and write in it
```python
with open('filename.txt','w') as file:
    file.write("txt to write")
```
- Pandas
Import from dictionary a dataframe: 
```python
df = pd.DataFrame.from_dict(name_dict)
df.to_csv("name_of_csv.csv")
```

- Try-except
```python
for element in list:
    try:
        print(element/2)
    except: # jump here if there's an error
        print("Error")

```

## HTML tags
opening tag, attribute type/value, affected content and close tag
```html
<h1 class="title"> Titanic </h1>
```

common html tags:
- head
- body the whole page
- header
- article
- p: paragraph
- h1,h2,h3: different of levels
- div: divider, generic container
- nav: navigational
- li: list item
- a: anchor (hyper link)
- button：button can be clicked
- table: for making table in html
- td： table data
- tr: row cells in a tab
- ul: unordered list
- iframe: embed another page in a page (nesting browsing)

Tree structure
root: article tag.
then: element h, p, div
attribute and element has no children

my venv: web-scraping
conda create --name web-scraping

# BeautifulSoup

Steps to scrap the page:
- fetch the pages using requests
- get the page content
- create soup: parser to parse the object
- find the element with soup.find

```python
# fetch the pages, obtain a response object
result = requests.get("www.google.com)

# page content
content = result.text

# create soup object, parse the content
soup = BeautifulSoup(content,"lxml")

# locate an element by the id
soup.find(id="specific_id")

# find by the tag
soup.find('tag_name', class="class_name")

# for example
soup.find('article', class_="main_article")
soup.find('h1') # returns an object

# locate all elements
soup.find_all('h2') # returns a list

```

## Scrap a single HTML page

Right click inspect to get the part of the html code of the page

## Scraping multiple pages on a single page
target page: https://subslikescript.com/movies

The href gives the address(or subaddress from the root)

## Pagination
Multiple page from the website. Easier with Selenium

ul class="pagination"

## XPath
Selecting nodes from documents

Select an element with //tagName
// means pick out the node at any level in an XML document

//tagName[1]: pick the first one
//tagName[@AttributeName="Value"]

functions:
- contains(): //tagName[contains(@AttributeName,"Value")]; and; or
- starts-with()

e.g. //p/text()
//div[@class="full-script"]/text()
//p[(@class="plot")or(@class="plot2")]
//p[contains(@class, "plot")]

### XPath syntax

/: select **the children** from the node set on the left side of this character
//:matchin nods set on any level within the document

//article/h1/text()

.:the present context should be used
..:refers to a parent node
*/:select all
./*: all the children nodes considering the current node

XPath starts with 1.

# Selenium

## Identify a js driven website

Inspect-setting-preference, if disable javascript and the website stops working then the site is driven by JS

target website: https://www.adamchoi.co.uk/overs/detailed 

## Locate element with Selenium

```python
driver.find_element_by_id('id')
driver.find_element_by_class_name('classname')
# for example
driver.find_element_by_class_name('full-script')
driver.find_element_by_tag_name('h1')

# for multiple elements
find_elements_by_class_name('full-script') # returns a list
```

By elements is usually used if we want to locate multiple tages.

```html
<article class="main-article">
    <h1> Titanic (1997) </h1>
    <p class="plot"> 84 years later ... </p>
    <div class="full-script"> 13 meters. You... </div>
</article>
```

Find elements by xpath
```Python
driver.find_element_by_xpath('//tag[@AttributeName="Value"]')
```
In Value we need to write the Xpath.

## Button with Selenium

Build Xpath in the inspection section.

## Save the data in pandas DataFrame

## Select elements to a drop down
Dynamic dropdown: the link doens't change but the contents shown changes.

## Explicit wait
```Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# EC: expected condition of wait
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPath," ")))
```
