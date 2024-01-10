import requests
from bs4 import BeautifulSoup
# we have to concatenate the website address
root = 'https://subslikescript.com/'
website = f'{root}/movies'

result = requests.get(website) # create a request
content = result.text

soup = BeautifulSoup(content, 'lxml') # parser is lxml
# print(soup.prettify()) # make the result better looking

# get the main block
box = soup.find('article', class_= 'main-article')

# create a list for the links
links = []

# get all the hrefs
for link in box.find_all('a', href=True):# tag is a, and activate the href, returns a list
    links.append(link['href'])
    # print(link)
print(links)

for link in links:
    website = f'{root}/{link}'
    resul = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_= 'main-article')

    title = box.find('h1').get_text() # or soup.find('h1').get_text()
    transcript = box.find('div',class_='full-script').get_text(strip=True, separator=" ")
    # with open(f'{title}.txt','w') as file:
        # file.write(transcript)
