
import pypyodbc as odbc
DATABASE = 'TheAtifWaheed'
DRIVER = 'SQL Server'
SERVER = 'DESKTOP-2V3R7TP\SQLEXPRESS'


# connection_string = 'Driver = ' + DRIVER + '; Server = ' + SERVER + '; Database = ' + DATABASE + '; Trust_Connection = Yes'
# print(connection_string)
# con = odbc.connect(connection_string)
# "DRIVER={SQL Server};SERVER=DESKTOP-2V3R7TP\SQLEXPRESS;DATABASE=TheAtifWaheed"

con_string = "DRIVER={" + DRIVER + "};SERVER=" + SERVER + ";DATABASE=" + DATABASE
con = odbc.connect(con_string)



# STD = ['1', 'Atif', 'BSIT', '20']

# insertQuery = "insert into STD_RECORD VALUES (" + STD[0] + ", '" + STD[1] + "', '" + STD[2] + "', '" + STD[3] + "');"
# print(insertQuery)
# cursor = con.cursor()
# cursor.execute(insertQuery)
# cursor.commit()

