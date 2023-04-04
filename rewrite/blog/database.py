import sqlite3
import os
from datetime import datetime
def database():
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "db.sqlite3")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    tableName = "d"+str(datetime.now())[:10].replace("-","_")
    print(tableName)
    try:
        createTable(cur,tableName,"(id INTEGER PRIMARY KEY AUTOINCREMENT,hi TEXT,size INTEGER)")
    except:
        print("Warning: "+tableName +" already exists")
    insert(cur,tableName,"(hi, size) VALUES ('HELLO', 4)")
    conn.commit()
def createTable(cursor,name,args):
    strBuild = "CREATE TABLE "+name+" "+args
    cursor.execute(strBuild)
def insert(cursor,table,values):
    strBuild = "INSERT INTO "+table+" "+values
    print(strBuild)
    cursor.execute(strBuild)
database()


