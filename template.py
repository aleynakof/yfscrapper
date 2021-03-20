import requests
from bs4 import BeautifulSoup
import ortak

hisse_url = ""

html_kod = requests.get(hisse_url)

soup = BeautifulSoup(html_kod.content, 'lxml')