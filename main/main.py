from cProfile import label
import requests
from bs4 import BeautifulSoup
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title ='Custom Title', width= 600, height= 300)

with dpg.window(label= 'Python Parcer'):
    dpg.add_text("Hi, this is KryptoParcer")
    dpg.add_button(label="Search")
    dpg.add_button(label= 'Exit')

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

url = "https://coinmarketcap.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
names = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('p', class_='sc-1eb5slv-0 iworPT')
prices = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('div' ,class_='sc-131di3y-0 cLgOOr')
market_caps = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('span', class_='sc-1ow4cwt-1 ieFnWP')


n=[]
p=[]
m_c=[]
menu=""




for name in names:
    n.append(name.text)
    
for price in prices:
    p.append(price.text)
    
for market_cap in market_caps:
    m_c.append(market_cap.text)


while True:
    print('\n' 
    '1. Увидеть полный список криптовалют''\n'
    '2. Найти информацию об определенной криптовалюте' '\n' 
    '3. Закончить программу')

    menu=input()
    if menu == "1":
        print(n,'\n',p,'\n',m_c)
        
    elif menu == "2":
        print("Введите название криптовалюты с условием регистра (например Bitcoin)")
        x=input()
        index=n.index(x)
        print(n[index],'Price:',p[index], 'Market_cap:',m_c[index])
    elif menu == "3":
        break
        


    