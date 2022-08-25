import requests
from bs4 import BeautifulSoup

'''
    pip install requests
    pip install Beautifulsoup
'''

html = requests.get('http://www.dowellcomputer.com/main.jsp')

html = BeautifulSoup(html.text,"html.parser")
print(html)

links = html.select("td>a")
print(links[0])
print(links[1])

titleBox = html.select("#titleBox")
print(titleBox[0])
print(titleBox[0].find('a'))