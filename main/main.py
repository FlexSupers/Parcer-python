import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import csv
from colorama import init, Fore, Back, Style

FILENAME = "data.csv"

n = []
p = []
m_c = []

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
    print("\033[H\033[J")


def record():
    with open(FILENAME, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for line in users:
            writer.writerow(line)
        

def search():
    Table = PrettyTable()
    Table.field_names = ["№","Name","Price","Market Cap"]
    print("Введите название криптовалюты:")
    print("Чтобы выйти в главное меню, введите 4")
    x=input()
    if x=="4":
        menu()
    else:
        for name in n:
            if name.lower().find(x.lower())==0:
                i=n.index(name)
                Table.add_row([i+1,n[i], p[i], m_c[i]])
        print(Table)

def krasota():
    print(Style.BRIGHT + Fore.GREEN)
    print(  "******             **              *******             ********      *********     *******    ")
    print(  "**    **          ****             **    **         ********         *********     **    **   ")
    print(  "**    **         **  **            **     **       *****             ***           **     **  ")
    print(  "**    **        **    **           **    **       ****               *********     **    **   ")
    print(  "******         **      **          ******         ****               *********     ******     ")
    print(  "**            ************         ** **           *****             ***           ** **      ")
    print(  "**           **          **        **   **          *******          *********     **   **    ")
    print(  "**          **            **       **     **          *********      *********     **     **  ")
    print('\n          Выполнено Гороховым Владимиром, Сарончиным Артемом и Букреевым Никитой'              )
  

def vivod():
    Table = PrettyTable()
    Table.field_names = ["№","Name","Price","Market Cap"]
    for index in range(10):
        Table.add_row([index+1,n[index], p[index], m_c[index]])
    print(Table)



def menu():
    while True:
        record()
        print('\n' 
        '1. Увидеть полный список криптовалют''\n'
        '2. Найти информацию об определенной криптовалюте' '\n' 
        '3. Выход')

        menu=input()
        if menu == "1":
            vivod()
        
        elif menu == "2":
            search()

        elif menu == "3":
            break
            

if __name__ == "__main__":
    parsing()
    krasota()
    menu()
    clear()