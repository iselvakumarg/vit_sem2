hourly_wage = float(input("Enter the Hourly Wage of the Employ: "))
total_regular_hours = float(input("Enter the total regular Hours: "))
total_overtime_hours = float(input("Enter the total overtime Hours: "))

overtime_pay = total_overtime_hours * (1.5 * hourly_wage)

total_weekly_pay = hourly_wage * total_regular_hours + overtime_pay

print(total_weekly_pay)