import random
import pyodbc
import time
import datetime

maksimal = range(100000000)
n=312


for i in maksimal:
    n += 1
    now = datetime.datetime.now()
    date_time = now.strftime("%d/%m/%y %H:%M:%S")
    time.sleep(2)

    try:
        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\iqbal\nutrifood\pythonProject\pytdb.accdb;'
        conn = pyodbc.connect(con_string)
        cursor = conn.cursor()

        myuser = (

            (n, date_time, 'lajang', random.randrange(30, 50),random.randrange(30, 50)),

        )
        cursor.executemany('INSERT INTO Table1 VALUES (?,?,?,?,?)', myuser)
        conn.commit()
        print('Data Inserted')
        print(i)
        print(date_time)


    except pyodbc.Error as e:
        print("Error in connection", e)