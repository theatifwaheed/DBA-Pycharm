# CONNECTION

import pypyodbc as odbc
class CDB:
    def new_connect(self):
        DATABASE = 'TheAtifWaheed'
        DRIVER = 'SQL Server'
        SERVER = 'DESKTOP-2V3R7TP\SQLEXPRESS'
        print("Connecting...")
        connString = "DRIVER={" + DRIVER + "}; SERVER=" + SERVER + "; DATABASE=" + DATABASE
                     # '; Trust_Connection=Yes'
        self.con = odbc.connect(connString)
        print("Connected...")

        # DRIVER = 'SQL Server'
        # SERVER = 'HEPTA14'
        # DATABASE = 'TheAtifWaheed'

    def getData (self, s_id):
        cursor = self.con.cursor()
        getdata = "select * from LABTASK4 where ID = " + s_id
        cursor.execute(getdata)
        data = cursor.fetchall()
        return data

 
    
    def updateData(self, id, name, degree):
        upQuery = "update LABTASK4 SET ID = " + id + ", NAME = '" + name + "', DEGREE = '" + degree + "' where ID = " + id
        cursor = self.con.cursor()
        cursor.execute(upQuery)
        cursor.commit()
        print(upQuery)

