import mysql.connector

class Mydb_demo:
    def __init__(self):
      
        self.myconn=mysql.connector.connect(host="localhost",user="root", password="",database="theshopdb")
        print(self.myconn)
        self.querywriter=self.myconn.cursor()
        print("1")

   

#username=input("enter your user name")
#password=input("enter your Password")
db=Mydb_demo()
#db.show_all_dbs()
db.create_table()
#db.show_all_tables()
#db.addUser(username,password)
