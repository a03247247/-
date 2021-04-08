import urllib.parse
import requests
import time
import json
import csv
import os
from bs4 import BeautifulSoup
import csv

searchP =str(input("請輸入你想搜尋的產品"))

def search_momo():

    url = "https://m.momoshop.com.tw/mosearch/" + searchP + ".html"

    headers = {'User-Agent': 'mozilla/5.0 (Linux; Android 6.0.1; '
                             'Nexus 5x build/mtc19t applewebkit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2702.81 Mobile Safari/537.36'}

    resp = requests.get(url, headers=headers)
    if not resp:
        return []

    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')




    info_items = soup.find_all("li", "goodsItemLi")

    with open('本週新片.csv', 'w', encoding='utf-8', newline='') as csv_file:
     csv_writer = csv.writer(csv_file)
     csv_writer.writerow(['商品名稱', '商品價格', '網址'])

     for item in info_items:
        name =info_items.find('h3').text.strip()
        price = info_items.find('b' , 'price').text.strip()
        urlX = 'http://m.momoshop.com.tw' + info_items.find('a')['href']


        csv_writer.writerow([name,price,urlX])
