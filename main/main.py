import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
names = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('p', class_='sc-1eb5slv-0 iworPT')
prices = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('div' ,class_='sc-131di3y-0 cLgOOr')
#print(prices)
#print(names)
for name in names:
    print(name.text)
    
for price in prices:
    print(price.text)