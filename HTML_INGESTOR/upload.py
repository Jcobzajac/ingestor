import urllib.request as urllib2
import urllib.error as urllib2
import html2text
from bs4 import BeautifulSoup 

with open("index.html") as file:
    soup = BeautifulSoup(file,"html.parser")
    print(soup.get_text())

