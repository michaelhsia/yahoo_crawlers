import requests
from bs4 import BeautifulSoup

stock_num = input('請輸入要查詢的股號')
url = 'https://tw.stock.yahoo.com/quote/' + str(stock_num)
r = requests.get(url)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('ul', class_='D(f) Fld(c) Flw(w) H(192px) Mx(-16px)')  # find() 會回傳 html
    # table = soup.find_all('ul', class_='D(f) Fld(c) Flw(w) H(192px) Mx(-16px)')：find_all() 回傳 list
    spans = table.find_all('span')
    # spans = table[0].find_all('span')：因為是 list 所以要套用index來取出值（html element），才能用 find() 或 find_all()
    for s in spans:
        print(s.text)