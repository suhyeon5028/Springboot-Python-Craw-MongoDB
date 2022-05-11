import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.cursor import CursorType

def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


list = []

aid = 1

while True:
    format_aid = '{0:010d}'.format(aid)
    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{format_aid}?sid=100")
        soup = BeautifulSoup(html.text, 'html.parser')
        
        company = soup.select_one(
            ".media_end_linked_more_point")
        title = soup.select_one(
            ".media_end_head_headline")
        time = soup.select_one(
            ".media_end_head_info_datestamp_bunch span")
        aid += 1
        
        # print(company.get_text())
        # print(title.get_text())
        # print(time.get_text())
        
        if(html.status_code == 200):
            dict = {"company":company.get_text(),"title":title.get_text(),"createdAt": time.get_text()}
            list.append(dict)

    except Exception as e:
        pass
    if len(list) == 20:
        break
    

# Mongo 연결
mongo = MongoClient("localhost", 20000)

mongo_save(mongo, list, "greendb", "navers")  # List안에 dict을 넣어야 함
