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

## BeautifulSoup

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