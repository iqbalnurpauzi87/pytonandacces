import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\iqbal\nutrifood\pythonProject\pytdb.accdb;'
    conn = pyodbc.connect(con_string)

    newdata = "databaru"
    user_id = 416

    cur = conn.cursor()
    cur.execute('UPDATE Table1 SET Field1 = ? WHERE id = ?', (newdata, user_id))
    conn.commit()

    print('data inserted')



except pyodbc.Error as e:
    print("Error in Connection", e)