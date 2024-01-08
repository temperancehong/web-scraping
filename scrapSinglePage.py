# 

# essential dependencies
import requests
from bs4 import BeautifulSoup

website = "https://subslikescript.com/movie/Titanic-120338"
result = requests.get(website) # create a request
content = result.text

soup = BeautifulSoup(content, 'lxml') # parser is lxml
# print(soup.prettify()) # make the result better looking

# as reference
box = soup.find('article', class_= 'main-article')

# get the title
title = box.find('h1').get_text() # or soup.find('h1').get_text()
print(title)

# get transcript
transcript = box.find('div',class_='full-script').get_text(strip=True, separator=" ")
# separator replace a new line with a blank space

# write into txt file
# with open(f'{title}.txt','w') as file:
#     file.write(transcript)