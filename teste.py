from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.sorteonline.com.br/resultados").text

soup = BeautifulSoup(html, 'html.parser')

resultados = soup.find('div','card lot-megasena')

uls = resultados.find('ul')
dezenas = []
unique_numbers = []

for ul in uls:    
    if ul.get_text() is not None:                
        if ul.get_text() != str("/n"):            
            dezenas.append(ul.get_text())
   
dezenas = filter(None,dezenas)
for dezena in dezenas:
    if dezena is not None:
        print(str(dezena))                    