# get the HTML from a page

# essential dependencies
import requests
from bs4 import BeautifulSoup

website = "https://subslikescript.com/movie/Titanic-120338"
result = requests.get(website) # create a request
content = result.text

soup = BeautifulSoup(content, 'lxml') # parser is lxml
print(soup.prettify()) # make the result better looking