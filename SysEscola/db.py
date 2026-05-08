from pathlib import Path 
import json 

DB_FILE = Path(__file__).parent / 'log.json'

class Database:

    def __init__(self):
        ... 
    
    def insert(self, query):
        ...
    
    def update(self, query):
        ...

class DB(Database):
    def __init__(self):
        ...
    
    def insert(self, query):
        query_formated = query 
        with open(DB_FILE,'w') as _file:
            json.dump(query_formated, _file, indent=4, ensure_ascii=False)

    def load(self):
        with open(DB_FILE, 'r', encoding='utf-8') as _file:
            json_file = json.load(_file)
            #print(json_file)

    def update(self, query):
        #query_formated = query 
        #with open(DB_FILE,'w') as _file:
        #    json.dump(query_formated, _file, indent=4, ensure_ascii=False)
        ...

if __name__ == '__main__':
    db = DB()
    db.load()
    print('Gravou')