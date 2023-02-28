import sqlite3
from typing import List
from modules.items import Items 

class Connect:
    con: sqlite3.Connection
    cursor: sqlite3.Cursor


    def openConnection(self) -> None:
        self.con = sqlite3.connect('parcer.db')
        self.cursor = self.con.cursor()


    def closeConnection(self)->None:
        self.con.close()


    def get_all_resourses(self) -> list:
        self.openConnection()
        res = self.cursor.execute(
            '''
            SELECT id, resource_name FROM resource
            '''
        )
        data = [{'id': raw[0], 'res_name': raw[1]} for raw in res]
        self.closeConnection
        return data


    def get_elements_for_res(self, res_name) -> dict:
        self.openConnection()
        
        self.cursor.execute(
            f'''
            SELECT * FROM resource WHERE resource_name = '{res_name}'
            '''
        )
        desc = self.cursor.description
        cols = [col[0] for col in desc]
        data = (dict(zip(cols, raw)) for raw in self.cursor.fetchall()) 
        self.closeConnection()
        return list(data)[0]
        
    def insert_items(self, items: List[Items])->None:
        self.openConnection()
        for item in items:
            self.cursor.execute(
                '''
                INSERT INTO items (res_id, link, title, content, nd_date, s_date, not_date) VALUES (?, ?, ?, ?, ?, ?, ?)
                ''',
                (item.res, item.link, item.title, item.content, item.nd_date, item.s_date, item.not_date)
            )
        self.con.commit()
        self.closeConnection()

    # def initial(self):
    #     self.openConnection()
    #     # create res
    #     self.cur.execute('''
    #         CREATE TABLE IF NOT EXISTS resource (
    #             id INTEGER PRIMARY KEY,
    #             resource_name TEXT UNIQUE,
    #             resource_url TEXT UNIQUE,
    #             top_tag TEXT,
    #             link_tag TEXT,
    #             header_tag TEXT,
    #             content_link TEXT,
    #             content_tag TEXT,
    #             date_tag TEXT),
    #             "pagination_tag"	TEXT,
    #             "pagination_from"	INTEGER,
    #             "pagination_to"	INTEGER,
    #             PRIMARY KEY("id")
    #         ''')
    #     # create items
    #     self.cur.execute('''
    #     CREATE TABLE IF NOT EXISTS "items" (
    #         "id"	INTEGER,
    #         "res_id"	INTEGER NOT NULL,
    #         "link"	TEXT,
    #         "title"	TEXT,
    #         "content"	INTEGER,
    #         "nd_date"	INTEGER,
    #         "s_date"	INTEGER,
    #         "not_date"	TEXT,
    #         PRIMARY KEY("id" AUTOINCREMENT),
    #         FOREIGN KEY("res_id") REFERENCES "resource"("id") ON DELETE CASCADE ON UPDATE CASCADE);
    #     ''')
    #     self.closeConnection()



