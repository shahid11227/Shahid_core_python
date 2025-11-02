import mysql.connector

class Mydb_demo:
    def __init__(self):
        
        #self.myconn=mysql.connector.connect(host="localhost",user="root",password="")
        self.myconn=mysql.connector.connect(host="localhost",user="root",password="",database="th45eshopdb")
        self.querywriter=self.myconn.cursor()

    def create_db(self):
        self.querywriter.execute("create database th45eshopdb")
        print("database created successfully")

    def show_all_dbs(self):
        self.querywriter.execute("show databases")

        for dbb in self.querywriter:
            print(dbb)
    def create_table(self):
        qry_logintbl="create table logintable(username varchar(100),password varchar(100))"
        qry_itemstbl="create table Itemstable(itemname varchar(100),price int)"
       
        self.querywriter.execute(qry_logintbl)
        print("Table created successfully")

    def show_all_tables(self):
        self.querywriter.execute("show tables")

        for tbl in self.querywriter:
            print(tbl)
    def addUser(self):
        qry_add="INSERT INTO `logintable` (`username`, `password`) VALUES ('tanu', 'ils345')"
        self.querywriter.execute(qry_add)
        self.myconn.commit()
        print("User registered successfully")


username=input("enter your user name")
password=input("enter your Password")
db=Mydb_demo()
#db.create_db()
db.show_all_dbs()
#db.create_table()
##db.show_all_tables()
#db.addUser(username,password)
