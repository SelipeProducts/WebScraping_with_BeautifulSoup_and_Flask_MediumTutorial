#Tutorial Following https://medium.com/code-gandalf/web-scraping-in-python-with-beautifulsoup-and-flask-641efdb6ad5d


from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

#had to import to get parser library features
import lxml

import random

#source variable which will hold the result of our request
#GET request to web url and convert the HTML to plain text 
source = requests.get('https://webscraper.netlify.com/').text


#declare a soup variable and store the value we get after passing source to BS
soup = BeautifulSoup(source, 'lxml')

#prints entire soup
def print_all():
  print(soup)


#examples)
# <variable> = soup.find('<HTML_element_name>')
# <variable> = soup.find('<HTML_element_name>').select_one('child_element')
# <variable> = soup.find('<HTML_element_name>').find_all('child_element')

#returns first element with h2 tag
def find_first():
  find_h2 = soup.find('h2')
  print(find_h2)

#returns all elements with h2 tag
def find_all():
  find_all_h2 = soup.find_all('h2')
  print(find_all_h2)

#returns first h2 elements within first aricle
def find_first_elements_first_child():
  find_child = soup.find('article').select_one('h2')
  print(find_child)
#returns all h2 elements within first article
def find_first_elements_child_all():
  find_child = soup.find('article').find_all('h2')
  print(find_child)



#soup.find
#soup.find_all
#soup.find.select_one
#soup.find.find_all

#--------------------------------------------------------
#prints nth type
def nth_of_type():
  head0 = soup.find('main').select_one('article:nth-of-type(4)')
  print(head0)

#prints text within forth article and within div elements
def nth_4_div_text():
  head = soup.find('main').select_one('article:nth-of-type(4)').div.text
  print(head)

#prints div within forth article and within div element
def nth_4_div():
  head1 = soup.find('main').select_one('article:nth-of-type(4)').div
  print(head1)

#prints h2 title, p aurther, and div without html tags
def nth_4_text():
  head3 = soup.find('main').select_one('article:nth-of-type(4)').text
  print(head3)


#soup.find('elem').select_one('article:nth-of-type(4)')
#soup.find('elem').select_one('article:nth-of-type(4)').div.text
#soup.find('elem').select_one('article:nth-of-type(4)').div
#soup.find('elem').select_one('article:nth-of-type(4)').text


#----------------------------------------------------------------

def find_author_and_cleanup():
  author_date = soup.find('main').select_one('p').text
  print(author_date)
  author_date_split = author_date.split(',')
  author = author_date_split[0]
  date = author_date_split[1]
  date = date.lstrip()

  print(author)
  print(date)


#----------------------------------------------------------------

#Flask App code
app = Flask(__name__)
@app.route('/')
def index():
  #local variables that will be passed 
  head = soup.header.h1.text
  second_author = soup.main.select_one('article:nth-of-type(2)').p.text
  first_article = soup.main.article.div

  return render_template('index.html',  **locals())

app.debug = True
app.run(host='0.0.0.0', port=random.randint(2000, 9000))


# how you can scrape multiple pages?
# The answer is multiple: for, while, try, except and if-else loops!
