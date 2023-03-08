gender = input("Enter the Employee Gender (M for Male, F for Female) : ")
salary = int(input("Enter the Employee Salary"))

total_salary = salary

if salary < 10000:
    bonus = salary * 0.02
    total_salary += bonus

if gender == 'm':
    bonus = salary * 0.05
    total_salary += bonus
elif gender == "f":
    bonus = salary * 0.15
    total_salary += bonus

print(bonus)
print(total_salary)