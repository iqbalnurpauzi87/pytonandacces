import random
import pyodbc
import time
import datetime

maksimal = range(100000000)
id_table=178198

for i_loop in maksimal:
    id_table += 1
    now = datetime.datetime.now()
    date_time = now.strftime("%d/%m/%y %H:%M:%S")
    # time.sleep(1/1000)

    try:
        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\iqbal\nutrifood\pythonProject\pytdb.accdb;'
        conn = pyodbc.connect(con_string)
        cursor = conn.cursor()

        a = random.randrange(30, 50)
        b = random.randrange(30, 50)
        c = random.randrange(30, 50)
        d = random.randrange(30, 50)
        e = random.randrange(30, 50)
        f = random.randrange(30, 50)
        g = random.randrange(30, 50)
        h = random.randrange(30, 50)
        i = random.randrange(30, 50)
        j = random.randrange(30, 50)
        k = random.randrange(30, 50)
        l = random.randrange(30, 50)
        m = random.randrange(30, 50)
        n = random.randrange(30, 50)
        o = random.randrange(30, 50)
        p = random.randrange(30, 50)
        q = random.randrange(30, 50)
        r = random.randrange(30, 50)
        s = random.randrange(30, 50)
        t = random.randrange(30, 50)
        u = random.randrange(30, 50)
        v = random.randrange(30, 50)
        w = random.randrange(30, 50)
        x = random.randrange(30, 50)
        y = random.randrange(30, 50)
        z = random.randrange(30, 50)

        myuser = (

            (id_table, date_time, 'idle', a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z),

        )
        cursor.executemany('INSERT INTO Table1 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', myuser)
        conn.commit()
        print(myuser)
        print('Data Inserted', i_loop)
        # print(i_loop)
        print("")


    except pyodbc.Error as e:
        print("Error in connection", e)