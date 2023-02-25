import sqlite3


class Connect:
    con: sqlite3.Connection
    cursor: sqlite3.Cursor


    def openConnection(self) -> None:
        self.con = sqlite3.connect('parcer.db')
        self.cur = self.con.cursor()

    def closeConnection(self)->None:
        self.con.close()
        
    def get_all_resourses(self) -> list:
        self.openConnection()
        res = self.cur.execute(
            '''
            SELECT resource_name FROM resource
            '''
        )
        # desc = self.cur.description
        # column_names = [col[0] for col in desc]
        # data = [dict(zip(column_names, row))  
        #         for row in self.cur.fetchall()]
        data = [raw[0] for raw in res]
        self.closeConnection
        return data

    def get_elements_for_res(self, res_name) -> dict:
        self.openConnection()
        
        self.cur.execute(
            f'''
            SELECT * FROM resource WHERE resource_name = '{res_name}'
            '''
        )
        desc = self.cur.description
        cols = [col[0] for col in desc]
        data = [dict(zip(cols, raw)) for raw in self.cur.fetchall()]
        self.closeConnection()
        return data
        

    def initial(self):
        self.openConnection()
        # create res
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS resource (
                id INTEGER PRIMARY KEY,
                resource_name TEXT UNIQUE,
                resource_url TEXT UNIQUE,
                top_tag TEXT,
                link_tag TEXT,
                header_tag TEXT,
                content_link TEXT,
                content_tag TEXT,
                date_tag TEXT)
            ''')
        # create items
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS "items" (
            "id"	INTEGER,
            "res_id"	INTEGER NOT NULL,
            "link"	TEXT,
            "title"	TEXT,
            "content"	INTEGER,
            "nd_date"	INTEGER,
            "s_date"	INTEGER,
            "not_date"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT),
            FOREIGN KEY("res_id") REFERENCES "resource"("id") ON DELETE CASCADE ON UPDATE CASCADE);
        ''')
        self.closeConnection()



