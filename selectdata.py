import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\iqbal\nutrifood\pythonProject\pytdb.accdb;'
    conn = pyodbc.connect(con_string)

    cur = conn.cursor()
    cur.execute('SELECT * FROM table1')

    for row in cur.fetchall():
        print(row)

except pyodbc.Error as e:
    print("Error in connection")