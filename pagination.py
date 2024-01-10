import requests
from bs4 import BeautifulSoup
# we have to concatenate the website address
root = 'https://subslikescript.com' # get the movies beginning with letter A
website = f'{root}/movies_letter-A'

result = requests.get(website) # create a request
content = result.text

soup = BeautifulSoup(content, 'lxml') # parser is lxml
# print(soup.prettify()) # make the result better looking


# pagination
pagination = soup.find('ul',class_="pagination") # each thing is a li tag
pages = pagination.find_all('li',class_="page-item")
last_page = pages[-2].text # find the one before the last element, the page number

links = []

for page in range(1, int(last_page)+1):
    # https://subslikescript.com/movies_letter-A?page=2
    result = requests.get(f'{website}?page={page}') # create a request
    content = result.text
    soup = BeautifulSoup(content, 'lxml') # parser is lxml

    # get the main block
    box = soup.find('article', class_= 'main-article')


    # get all the hrefs
    for link in box.find_all('a', href=True):# tag is a, and activate the href, returns a list
        links.append(link['href'])
        # print(link)
    print(links)

    for link in links:
        try:
            print(link)
            website = f'{root}/{link}'
            resul = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            box = soup.find('article', class_= 'main-article')

            title = box.find('h1').get_text() # or soup.find('h1').get_text()
            transcript = box.find('div',class_='full-script').get_text(strip=True, separator=" ")
            # with open(f'{title}.txt','w') as file:
                # file.write(transcript)
        except:
            print('----Link note working----')