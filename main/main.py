from operator import index
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import csv

FILENAME = "data.csv"

n = []
p = []
m_c = []
menu=""

users = [n, p, m_c]

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


def clear():
    n.clear()
    p.clear()
    m_c.clear()




def record():
    with open(FILENAME, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for line in users:
            writer.writerow(line)
        

def search():
    parsing()
    Table = PrettyTable()
    Table.field_names = ["№","Name","Price","Marcet Cap"]
    print("Введите название криптовалюты с условием регистра (например Bitcoin)")
    x=input()
    try:
        index=n.index(x)
        #print(n[index],'Price:',p[index], 'Market_cap:',m_c[index])
        Table.add_row([index+1,n[index], p[index], m_c[index]])
        print(Table)
    except ValueError:
        print("Неправильно введенна криптовалюта")
        search()



def vivod():
    parsing()
    record()
    Table = PrettyTable()
    Table.field_names = ["№","Name","Price","Marcet Cap"]
    for index in range(10):
        Table.add_row([index+1,n[index], p[index], m_c[index]])
    print(Table)


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
    clear() # не очищает

       


    