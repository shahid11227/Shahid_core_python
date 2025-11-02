#csv comma seperated values

ptr=open("D:\\pythonwork\\csvfiles\\studentlist.csv")
#print(ptr.read())
records=ptr.readlines()
studentdata={}
for record in records:
    row=record.split(",")
    regno=row[0]
    name=row[1]
    address=row[2]
    marks=row[3]
    gender=row[4]

    studentdata[regno]={"Name":name,"Address":address,"Marks":marks,"Gender":gender}



print("___________Search Using Reg No_______")
rno=input("ENter your reg No")
if rno in studentdata:
    print("Registration Number\t=",rno , "\nStudent Name\t=",studentdata[rno]["Name"],"\nStudent Address\t=",studentdata[rno]["Address"],"\nStudent Marks\t=",studentdata[rno]["Marks"],"\nStudent Gender\t=",studentdata[rno]["Gender"])


