import mysql.connector

#  MySQL se connect
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # agar password hai to likho
    database="demo"   # phpMyAdmin me pehle se hona chahiye
)
cursor = con.cursor()

# Table create (agar nahi hai)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
age INT)
""")

#  Data insert
name = input("Enter name: ")
age = int(input("Enter age: "))
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
con.commit()
print("Data inserted successfully!")

#  Show data
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

con.close()
