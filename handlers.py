from time import sleep
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import csv
from modules.res import ParcingResource as Res
from modules.items import Items
from connections import Connect 


def parce_resource(params, res_id):
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
    dif = 1 if pag_to > pag_from else -1


    date = []


    cnt = 0


    url = params['resource_url']
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.text, 'lxml')

    for item in range(pag_from, pag_to, dif):
        if render == 0:
            req = requests.get(f'{pagination_url}{item}/', headers)
            # soup = BeautifulSoup(req.text, 'lxml')
            # print(soup)
            # break
        else:
            driver = webdriver.Chrome()
            driver.get(f'{pagination_url}{item}/')
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
        resourses = soup.findAll(f'{top_tag[0]}', class_=f'{top_tag[1]}')
        for res in resourses:
            link = res.find(f'{link_tag[0]}').get('href')
            header = res.find(f'{header_tag[0]}', class_=f'{header_tag[1]}').text.strip()
            time = res.find(f'{date_tag}').text.strip()
            try:
                date_obj = datetime.strptime(time, '%d.%m.%Y %H:%M')
                nd_date = date_obj.timestamp()
            except:
                nd_date = 'null'
            s_date = datetime.now()


            if content_here == 0:
                req = requests.get(link, headers)
                spc = BeautifulSoup(req.text, 'lxml')
                content = spc.find(f'{content_tag[0]}', class_=f'{content_tag[1]}').text.strip()
            else:
                content = res.find(f'{content_tag[0]}', class_=f'{content_tag[1]}').text.strip()

            it = Items(res=res_id, link=link, title=header, content=content, nd_date=nd_date,
                       s_date=s_date, not_date=time)

            date.append(it)

        sleep(1)    
        cnt += 1
        print(f"{cnt} Iteration, {len(resourses)} the len of res and {len(date)} of total")

    # with open('filename.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     for row in date:
    #         writer.writerow(row)
    print(len(date))
    db = Connect()
    db.insert_items(date)


def get_all_resources() -> list:
    db = Connect()
    return db.get_all_resourses()

def get_one_res(res_name) -> dict:
    db = Connect()
    return db.get_elements_for_res(res_name=res_name)



