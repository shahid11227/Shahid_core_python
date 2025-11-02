import os
n1=int(input("Enter any number"))
n2=int(input("Enter any next number"))

    
res=0
try:
    res=n1/n2
    fruits=["a","b","c"]
    print(fruits[3])

except TypeError:
    print("Enter proper Numbers")
except ZeroDivisionError:
    print("you are dividing by zero , that is undefined")
except IndexError:
    print("you are accessing fruit which is not available")

print(res)
print("thanks")



'''
file_path="D:\\pythonwork\\txtfiles\\myfile.txt"
mode_read="r"
mode_write="x"

if os.path.exists(file_path):
    ptr=open(file_path,mode_read)
    print(ptr.read())
    ptr.close()

else:
    ptr=open(file_path,mode_write)
    data="hello i am python"
    ptr.write(data)
    ptr.close()
    print("file created successfully")
'''
