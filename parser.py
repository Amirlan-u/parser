import requests
from bs4 import BeautifulSoup
import lxml

url= ('https://kz.e-katalog.com/ek-list.php?presets_=21592%2C3690%2C21899%2C3694&katalog_=61&pf_=1&maxPrice_=50000&order_=pop&save_podbor_=1')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

name = []


items = soup.find_all('td', class_="model-short-info")
for n, i in enumerate(items, start=1):
    names = i.find('span', class_="u").text
    name.append(names)

prise = []
item = soup.find_all('td', class_="model-hot-prices-td")
for n, i in enumerate(item, start=1):
    prises = i.find('a', class_="href").text.strip()
    prise.append(prises)
print(prise)
print(items)