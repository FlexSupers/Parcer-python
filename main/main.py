from cProfile import label
from kivy.app import App
from kivy.uix.label import Label


import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
names = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('p', class_='sc-1eb5slv-0 iworPT')
prices = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('div' ,class_='sc-131di3y-0 cLgOOr')
market_caps = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('span', class_='sc-1ow4cwt-1 ieFnWP')

n=[]
p=[]
m_c=[]
for name in names:
    n.append(name.text)
    #print(name.text)

for price in prices:
    p.append(price.text)
    #print(price.text)

for market_cap in market_caps:
    m_c.append(market_cap.text)
    #print(market_cap.text)


print(n,'\n',p,'\n',m_c)

class MainApp(App):
    def build(self):
        label = Label(text = 'Привет! Я программа с актуальными криптовалютами. Что ты хочешь найти?',
        size_hint = (1, 1),
        pos_hint = {'center_x': .5, 'center_y': .9}
        )

        return label



if __name__ == '__main__':
    MainApp().run()