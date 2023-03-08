# Create a dictionary for 6 employee details with empno as key, name, dob and net-pay as list of values use appropriate dictionary methods: a. Create a dictionary with the above information. b. Insert a new employee details as the second employee c. Delete the employee at the 4th position d. Delete the last employee e. Increment the salary of all employees by 5%.

#a. Create a dictionary with the above information.
employee_dict = {
     101: ["A", "1990-11-25", 70000],
     102: ["B", "1991-05-21", 10000],
     103: ["C", "1992-11-03", 35000],
     104: ["D", "1993-09-27", 85000],
     105: ["E", "1984-06-28", 80000],
     106: ["F", "1993-03-25", 15000]
}
# b. Insert a new employee details as the second employee
employee_dict[102] = ["G", "1994-08-12", 50000]
# C. Delete the employee at the 4th position
employee_dict.pop(104)
# d. Delete the last employee
employee_dict. popitem()
# e. Increment the salary of all employees by 5%
for emp_details in employee_dict. values():
    emp_details[2] *= 1.05

print(employee_dict,end="\n")
