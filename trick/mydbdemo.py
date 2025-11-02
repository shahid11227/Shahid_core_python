import pymysql


class mydb:
    def __init__(self):
        
        self.myconn=pymysql.connect(host="localhost",user="root",password="",database="theshopdb2")
        self.querywriter=self.myconn.cursor()
    def addUser(self,username,password):
        qry_add="INSERT INTO `logintable` (`username`, `password`) VALUES ('"+ username+"', '"+password+"')"
        
       
        self.querywriter.execute(qry_add)
        self.myconn.commit()
        print("User registered successfully")


    def getUsers(self,username,password):
        getuserquery1="select * from logintable "
        getuserquery2="select * from logintable where username='iram' "
        
        getuserquery3="select * from logintable where username=%s and password=%s "
        userval=(username,password,)
        self.querywriter.execute(getuserquery3,userval)
        
        allrecords=self.querywriter.fetchall()

        for record in allrecords:
            print(record)


#_________________________________MAIN START__________________________
print("Welcome to The Shop")
choice=input("Press 1 if you are Employee\n 2) for admin")
db=mydb()
if choice=="1":
    
    username=input("Enter your email")
    password=input("Enter new password")
    db.getUsers(username,password)
    


#db.addUser(username,password)
