from cProfile import label
from msilib.schema import Error
import requests
from bs4 import BeautifulSoup
import dearpygui.dearpygui as dpg
import sys
import csv

n = []
p = []
m_c = []
menu=""


def parsing():
    url = "https://coinmarketcap.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    names = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('p', class_='sc-1eb5slv-0 iworPT')
    prices = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('div' ,class_='sc-131di3y-0 cLgOOr')
    market_caps = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find_all('span', class_='sc-1ow4cwt-1 ieFnWP')

    for name in names:
        n.append(name.text)
    
    for price in prices:
        p.append(price.text)
    
    for market_cap in market_caps:
        m_c.append(market_cap.text)




def record():
    lines = [str(n), str(p), str(m_c)]
    with open(r"data.csv", "w") as file:
        for  line in lines:
            file.write(line + '\n')
    file.close()




def search():
    parsing()
    print("Введите название криптовалюты с условием регистра (например Bitcoin)")
    x=input()
    try:
        index=n.index(x)
        print(n[index],'Price:',p[index], 'Market_cap:',m_c[index])
    except ValueError:
        print("Неправильно введенна криптовалюта")
        search()




def vivod():
    parsing()
    record()
    for index in range(10):
        print(n[index],'Price:',p[index], 'Market_cap:',m_c[index], '\n')
        index=index+1



def menu():
    while True:
        print('\n' 
        '1. Увидеть полный список криптовалют''\n'
        '2. Найти информацию об определенной криптовалюте' '\n' 
        '3. Закончить программу')

        menu=input()
        if menu == "1":
            vivod()
        
        elif menu == "2":
            search()

        elif menu == "3":
            break

if __name__ == "__main__":
    menu()

       


    