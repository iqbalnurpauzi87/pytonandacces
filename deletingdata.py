import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\iqbal\nutrifood\pythonProject\pytdb.accdb;'
    conn = pyodbc.connect(con_string)

    user_id = 4126

    cur = conn.cursor()
    cur.execute('DELETE FROM Table1 WHERE id = ?', (user_id))
    conn.commit()
    print('data succes deleted')


except pyodbc.Error as e:
    print("error in connection", e)