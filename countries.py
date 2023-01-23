import csv, sqlite3
conn = sqlite3.connect("countries.db")
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS countries;')

c.execute('''
    CREATE TABLE countries (
    name TEXT NOT NULL ,
    alpha TEXT NOT NULL ,
    code INTEGER NOT NULL ,
    region TEXT NOT NULL ,
    intermediate_region TEXT,
    PRIMARY KEY (code)
    );
    ''')

with open('countries.csv','r') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['name'], i['alpha-3'], i['country-code'], i['region'], i['intermediate-region']) for i in dr]

c.executemany("INSERT INTO countries (name, alpha, code, region, intermediate_region) VALUES (?, ?, ?, ?, ?);", to_db)

conn.commit()
c.close()
