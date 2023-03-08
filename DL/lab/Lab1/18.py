# Create a CSV file and store student details like Name, Register number and CGPA. Write a python code to read the file content and display the content. Duplicate entries and null value entries has to be ignored while displaying. 

import csv
# Sample data
data = [
     ['Selva', '1001', '9.1'],
     ['Shiva', '1002', '9.1'],
     ['Nandhini', '1003', '7.8' ],
     ['Sri', '1004', '8.9' ],
     ['pawan', '1005' , '9.5'],
     ['Bavani', '1006', '8.5'],
     ['', '1007', '9.1'],
     ['shankar', '', '7.8' ]
]

with open('student.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Reg No', 'CGPA'])
    for row in data:
         if row[0] and row[1] and row[2]:
            writer.writerow(row)

with open( 'student.csv', mode= 'r') as file:
    reader = csv. reader(file)
    next(reader)
    for row in reader:
         if len(row) == 3 and row[0] and row[1] and row[2]:
            print(f"Name: {row[0]}, Reg No: {row[1]}, CGPA: {row[2]}")
