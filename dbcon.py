import pyodbc

print("mulai")

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\iqbal\nutrifood\pythonProject\pydb.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")



except pyodbc.Error as e:
    print("Error in Connection", e)

print("selesai")