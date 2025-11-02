import csv

# Data bana rahe hain (ye tumhara "text data" hai)
data = [
    ["RegNo", "Name", "Marks", "Gender"],
    [101, "Ali", 88, "M"],
    [102, "Asha", 92, "F"],
    [103, "Rahul", 75, "M"]
]

# CSV file bana rahe hain
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("✅ CSV file created successfully!")
