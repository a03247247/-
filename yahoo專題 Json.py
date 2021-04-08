import requests
import time
import json
import os
from bs4 import BeautifulSoup

searchP =str(input("請輸入你想搜尋的產品"))
def search_yahoo():

    url = "https://tw.buy.yahoo.com/search/product?p="+searchP
    resp = requests.get(url)
    if not resp:
        return []
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')


    items = []
    for product in soup.find_all("li", "BaseGridItem__grid___2wuJ7 "
                                       "BaseGridItem__multipleImage___37M7b"):

        item_name = product.find('span',"BaseGridItem__title___2HWui").text.strip()
        item_price = product.find('em').text.strip()
        if not item_price:
            continue
        item_url = product.find('a')['href']

        item = {
            'name': item_name,
            'price': item_price,
            'url': item_url,
                    }
        items.append(item)
    return items


if __name__ == '__main__':

    items = search_yahoo()
    today = time.strftime('%Y-%m-%d')
    print('%s 搜尋 %s 共 %d 筆資料' % (today, searchP, len(items)))
    for i in items:
        print(i)
    data = {
        'date': today,
        'store': 'yahoo',
        'items': items
    }

    path="yahoo"

    if not os.path.isdir(path):
        os.mkdir(path)


    with open(os.path.join('yahoo', today+"yahoo爬蟲專案"), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False) #將jason轉STR