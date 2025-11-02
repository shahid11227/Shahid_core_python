
import pymysql

class SchoolDB:
    def _init_(self,):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password=""
        )
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE DATABASE IF NOT EXISTS schooldb")
        self.cur.execute("USE schooldb")

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                grade VARCHAR(10)
            )
        """)
        print("Table created successfully!")

    def add_student(self, name, age, grade):
        self.cur.execute(
            "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)",
            (name, age, grade)
        )
        self.conn.commit()
        print(" Student added successfully!")

    def show_students(self):
        self.cur.execute("SELECT * FROM students")
        for row in self.cur.fetchall():
            print(row)


# main
db = SchoolDB()
db.create_table()

sname = input("Enter student name: ")
sage = int(input("Enter age: "))
sgrade = input("Enter grade/class: ")

db.add_student(sname, sage, sgrade)
db.show_students()
