import sqlite3
conn=sqlite3.connect('mydb.db')
c=conn.cursor()
c.execute('''CREATE TABLE score_table (slno text, reg_no text, score int)''')
c.close()