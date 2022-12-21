from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.mhjf0sv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#old_content > table > tbody > tr:nth-child(4) > td.title > div > a
#old_content > table > tbody > tr:nth-child(4) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(3) > td:nth-child(3) > div > div > img

trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    a = tr.select_one('td.title > div > a')
    if a is not None:
        title = a.text
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        star = tr.select_one('td:nth-child(3) > div > div > img').text
        doc = {
            'title':title,
            'rank':rank,
            'star':star
        }
        db.movies.insert_one(doc)
