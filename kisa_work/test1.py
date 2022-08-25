import requests
from bs4 import BeautifulSoup

'''
    pip install requests
    pip install Beautifulsoup
'''

html = requests.get('https://search.danawa.com/dsearch.php')

html = BeautifulSoup(html.text,"html.parser")
print(html)

titleBox = html.select("p .prod_name")
print(titleBox)
