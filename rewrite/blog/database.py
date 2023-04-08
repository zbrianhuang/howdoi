import sqlite3
import os
import uuid
from datetime import datetime
def database():
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "db.sqlite3")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    current_date = "d"+str(datetime.now())[:10].replace("-","_")
    id = uuid.uuid4()
    print(current_date)
    try:
        #createTable(cur,"main_index","(id CHAR PRIMARY KEY,date TEXT,url TEXT)")
        createTable(cur,current_date,"(id CHAR PRIMARY KEY,title TEXT,subject TEXT,author TEXT)")
    except:
        print("Warning: "+current_date +" already exists")
    query = "VALUES (\"{}\",\"{}\",\"{}\")".format(id,current_date,"www.yahoo.com")
    insert(cur,"main_index",query)
    query = "VALUES (\"{}\",\"{}\",\"{}\",\"{}\")".format(id,"Sports Betting Guide","Sports","Jim")
    insert(cur,current_date,query)
    conn.commit()
def createTable(cursor,name,args):
    strBuild = "CREATE TABLE "+name+" "+args
    cursor.execute(strBuild)
def insert(cursor,table,values):
    strBuild = "INSERT INTO "+table+" "+values
    print(strBuild)
    cursor.execute(strBuild)
    
database()


