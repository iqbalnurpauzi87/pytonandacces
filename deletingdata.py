import pyodbc

id_loc = 0
# jika error pastikan id nya yg di target ada

# try:
#     con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\iqbal\nutrifood\pythonProject\pytdb.accdb;'
#     conn = pyodbc.connect(con_string)
#
#     user_id = 9
#
#     cur = conn.cursor()
#     cur.execute('DELETE FROM Table1 WHERE id = ?', (user_id))
#     conn.commit()
#     print('data succes deleted')


def hapus_data(id_loc):
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\iqbal\nutrifood\pythonProject\pytdb.accdb;'
    conn = pyodbc.connect(con_string)

    # user_id = 5
    user_id = id_loc

    cur = conn.cursor()
    cur.execute('DELETE FROM Table1 WHERE id = ?', (user_id))
    conn.commit()
    print('data succes deleted')



# except pyodbc.Error as e:
#     print("error in connection", e)