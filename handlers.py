from time import sleep
from datetime import datetime
from typing import List
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


from modules.res import ParcingResource as Res
from modules.items import Items
from connections import Connect 


def create_resource(params, res) -> Res:
    pagination_url = params['pagination_tag']
    top_tag = params['top_tag'].split()
    link_tag = params['link_tag'].split()
    header_tag = params['header_tag'].split()
    date_tag = params['date_tag']
    content_here = params['content_here']
    content_tag = params['content_tag'].split()
    pag_from = params['pagination_from']
    pag_to = params['pagination_to']
    render = params['render']
    url = params['resource_url']

    resourse = Res(id=res['id'], name=res['res_name'], url=url,
                   top_tag=top_tag, link_tag=link_tag, header_tag=header_tag, content_tag=content_tag,
                   date_tag=date_tag, pagination_tag=pagination_url,
                   pag_from=pag_from, pag_to=pag_to, render=render, content_here=content_here)
    
    return resourse

def parce_resource(resourse: Res):

    data = []
    cnt = 0
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    dif = 1 if resourse.pag_from < resourse.pag_to else -1


    if resourse.render == 0:
        req = requests.get(resourse.res_url, headers)
        soup = BeautifulSoup(req.text, 'lxml')

    for item in range(resourse.pag_from, resourse.pag_to, dif):
        if resourse.render == 0:
            req = requests.get(f'{resourse.pagination_tag}{item}/', headers)
        else:
            driver = webdriver.Chrome()
            driver.get(f'{resourse.pagination_tag}{item}/')
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
        resourses = soup.findAll(f'{resourse.top_tag[0]}', class_=f'{resourse.top_tag[1]}')
        for res in resourses:
            link = res.find(f'{resourse.link_tag[0]}').get('href')
            header = res.find(f'{resourse.header_tag[0]}', class_=f'{resourse.header_tag[1]}').text.strip()
            time = res.find(f'{resourse.date_tag}').text.strip()
            try:
                date_obj = datetime.strptime(time, '%d.%m.%Y %H:%M')
                nd_date = date_obj.timestamp()
            except:
                nd_date = 'null'
            s_date = datetime.now()


            if resourse.content_here == 0:
                print(link)
                try:
                    req_con = requests.get(link, headers)
                    spc = BeautifulSoup(req_con.text, 'lxml')
                    content = spc.find(f'{resourse.content_tag[0]}', class_=f'{resourse.content_tag[1]}').text.strip()
                except:
                    content = "Not Found"
            else:
                try:
                    content = res.find(f'{resourse.content_tag[0]}', class_=f'{resourse.content_tag[1]}').text.strip()
                except:
                    content = "Not found"

            it = Items(res=resourse.res_id, link=link, title=header, content=content, nd_date=nd_date,
                       s_date=s_date, not_date=time)

            data.append(it)

        sleep(1)    
        cnt += 1
        print(f"{cnt} Iteration, {len(resourses)} the len of res and {len(data)} of total")

    push_into_db(data=data)


def push_into_db(data: List[Items]):
    db = Connect()
    db.insert_items(data)



def get_all_resources() -> list:
    db = Connect()
    return db.get_all_resourses()



def get_one_res(res_name) -> dict:
    db = Connect()
    return db.get_elements_for_res(res_name=res_name)



