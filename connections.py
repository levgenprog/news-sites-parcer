import sqlite3


def initial(cur):
    # create res
    cur.execute('''
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
    cur.execute('''
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

def main():
    conn = sqlite3.connect('parcer.db')
    cur = conn.cursor()
    initial(cur)
    conn.close()


if __name__ == '__main__':
    main()


