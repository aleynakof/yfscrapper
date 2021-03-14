import requests
from bs4 import BeautifulSoup

hisse_url = "https://www.hurriyet.com.tr/"

html_kod = requests.get(hisse_url)

soup = BeautifulSoup(html_kod.content, 'lxml')

bilgi_bar = soup.find_all('div', class_='bigpara-hw-top')[0].find('a').find_next('a')
print(bilgi_bar)

dolar_baslik = bilgi_bar.find('span').get_text()
print(dolar_baslik)
#dolar_deger = bilgi_bar.find('div', class_='parite-value up').get.text()
dolar_deger = bilgi_bar.find('div', class_='parite-value up').get_text()
print(dolar_deger)


