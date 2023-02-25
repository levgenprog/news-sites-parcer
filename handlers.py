from time import sleep
import requests
from bs4 import BeautifulSoup

import csv
from modules.res import ParcingResource as Res
from modules.items import Items
from connections import Connect 


def parce_resource(params):
    url = params['resource_url']
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.text, 'lxml')


    pagination_url = params['pagination_tag']
    top_tag = params['top_tag'].split()
    link_tag = params['link_tag'].split()
    header_tag = params['header_tag'].split()
    date_tag = params['date_tag']
    content_tag = params['content_tag'].split()

    date = [
        ['Header', 'Link', 'Content', 'Time'],
    ]
    cnt = 0
    for item in range(1, 15):
        req = requests.get(f'{pagination_url}{item}/', headers)
        resourses = soup.findAll(f'{top_tag[0]}', class_=f'{top_tag[1]}')
        for res in resourses:
            link = res.find(f'{link_tag[0]}', class_=f'{link_tag[1]}').get('href')
            header = res.find(f'{header_tag[0]}', class_=f'{header_tag[1]}').text.strip()
            time = res.find(f'{date_tag}').text.strip()

            req_content = requests.get(link, headers)
            sout_cont = BeautifulSoup(req_content.text, 'lxml')
            content = sout_cont.find(f'{content_tag[0]}', class_=f'{content_tag[1]}').text.strip()

            date.append([header, link, content, time])

        sleep(3)    
        cnt += 1
        print(f"{cnt} Iteration, {len(resourses)} the len of res and {len(date)} of total")

    with open('filename.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in date:
            writer.writerow(row)


def get_all_resources() -> list:
    db = Connect()
    return db.get_all_resourses()

def get_one_res(res_name) -> dict:
    db = Connect()
    return db.get_elements_for_res(res_name=res_name)



