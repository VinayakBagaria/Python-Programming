from os import listdir
import sqlite3

def getFiles():
    path="C:\\Users\\bagariavinayak\\Desktop\\Classified\\gallery"
    files=listdir(path)
    g2 = []
    for elem in files:
        x=elem[:7]
        if(x.isdigit()):
            g2.append(x)

def insertIntoDatabase():
    connection = sqlite3.connect("contest.db")
    cursor = connection.cursor()
    cursor.execute("""DROP TABLE pictures""")
    sql_command = """
    CREATE TABLE pictures (
    pic_number VARCHAR PRIMARY KEY,
    reg_no INTEGER,
    Likes INTEGER);"""
    cursor.execute(sql_command)

    sql_command = """INSERT INTO pictures (pic_number,reg_no,Likes) VALUES ("1417175",14,20);"""
    cursor.execute(sql_command)

    cursor.execute("SELECT * FROM pictures")
    print("fetchall:")
    result = cursor.fetchall()
    for r in result:
        print(r)

    # never forget this, if you want the changes to be saved:
    connection.commit()

    connection.close()
getFiles()
insertIntoDatabase()