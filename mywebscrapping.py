import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

#get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
#step2 :parse HTML content
soup =BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)
#step3:HTML tree traversal
title = soup.title
#print(type(title))
#step4 how to write comments
#markup ="<p><!--this is a comment i want to add--></p>"
#soup2 = BeautifulSoup(markup)
#print(type(soup2.p.string))
#exit()
#to finnd all the paragraphs
paras = soup.find_all('p')
#print(paras)
#to find a particular class in a para
print(soup.find('p')['class'])
#find elements with class lead 
#note we can add any atrribute of the class provided it should me within the class
print(soup.find_all("p",class_="lead"))
#get text from elements
print(soup.find('p').get_text())
#get all the anchor tags
anchor =soup.find_all('a')
#get all the links from the page
all_links = set()9
for link in anchor:
    if (link.get('href') !='#'):
      link_text ="https://codewithharry.com"+link.get('href')
      all_links.add(link)
      print(link_text)

#print(anchor)

navbarSupportedContent = soup.find(id='nav-content')
print(navbarSupportedContent.contents)
elem = soup.select('.modal-footer')
print(elem)

