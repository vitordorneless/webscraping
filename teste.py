from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.sorteonline.com.br/resultados").text

soup = BeautifulSoup(html, 'html.parser')

temperaturas = soup.find('div','card lot-megasena')

uls = temperaturas.find('ul')

for ul in uls:
    print(ul.get_text())



#for temperatura in temperaturas:
#    print(temperatura.get_text())