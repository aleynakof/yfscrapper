import requests
from bs4 import BeautifulSoup

hisse_url = "https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch"
print(hisse_url)

html_kod = requests.get(hisse_url)

#print(html_kod)
#print(html_kod.content)

#lxml kullanmak için pip install lxml çalıştırın
soup = BeautifulSoup(html_kod.content, "lxml")

#print(soup.title.text)

sayfa_title = soup.find("title").get_text()

#print(sayfa_title)


#listeden kutulmak için ilk elemanı getir
header = soup.find_all('div', id='quote-header-info')[0]
hisse_title = header.find('h1').get_text()
print(hisse_title)

hisse_fiyat = header.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px)').find('span').get_text()
print(hisse_fiyat)
