import csv
import os

# Folder path set karo
folder = r"D:\trick"
os.makedirs(folder, exist_ok=True)

# Full file path
file_path = os.path.join(folder, "students.csv")

# Data define karo
data = [
    ["RegNo", "Name", "Marks", "Gender"],
    [101, "Ali", 88, "M"],
    [102, "Asha", 92, "F"],
    [103, "Rahul", 75, "M"]
]

try:
    # File open and write
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(" CSV file created successfully!")
    print(" File path:", file_path)
    print(" Folder exists:", os.path.exists(folder))
    print(" File exists:", os.path.exists(file_path))

except Exception as e:
    print(" Error:", e)
