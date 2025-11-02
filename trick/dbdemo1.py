import pymysql

class Mydb_demo:
    def __init__(self):
        
        self.myconn=pymysql.connect(host="localhost",user="root",password="")
        self.myconn=pymysql.connect(host="localhost",user="root",password="",database="theshopdb2")
        self.querywriter=self.myconn.cursor()

    def create_db(self):
        self.querywriter.execute("create database theshopdb2")
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
    def addUser(self,username,password):
        qry_add="INSERT INTO `logintable` (`username`, `password`) VALUES ('shahid', 'ils346')"
        self.querywriter.execute(qry_add)
        self.myconn.commit()
        print("User registered successfully")


username=input("enter your user name")
password=input("enter your Password")
db=Mydb_demo()
#db.create_db()
#db.show_all_dbs()
#db.create_table()
#db.show_all_tables()
db.addUser(username,password)
