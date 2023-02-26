# Consider the student details are maintained using nested dictionary as follows: {Reg no: {subcode: CAT1, CAT2, SAT}}  a..Create nested dictionary for three subjects b. Display the information of a student given his register number c. To display the marks of a student given his subject code d. Update the details of the student given the register number.

students = {
    "101": {
         "sub1": [50, 60, 75],
         "sub2": [70, 80, 90],
         "sub3": [85, 90, 95]
     },
     "102": {
         "sub1": [60, 75, 80],
         "sub2": [80, 85, 90],
         "sub3": [90, 95, 98]
     },
     "103": {
         "subl": [70, 80, 85],
         "sub2": [85, 90, 92],
         "sub3": [95, 98, 99]
     }
}    
#b. Displaying the information of a student given their register number:
def display_student_info(reg_no):
    if reg_no in students:
        print(f"Register number: {reg_no}")
        for sub_code, marks in students[reg_no].items():
            print(f"{sub_code} marks: {marks}")
    else:
        print(f"No student found with register number {reg_no}")

# c. Displaying the marks of a student in a particular subject given their register number and subject code:
def display_marks_by_sub_code(reg_no, sub_code):
     if reg_no in students and sub_code in students[reg_no]:
        print(f"{sub_code} marks for student {reg_no}: {students[reg_no][sub_code]}")
     else:
        print(f"No marks found for subject {sub_code} and student {reg_no}")

# d. Updating the details of a student given their register number, subject code and marks:
def update_student_details(reg_no, sub_code, cat1, cat2, sat):
    if reg_no in students:
        if sub_code in students[reg_no]:
            students [reg_no][sub_code] = [cat1, cat2, sat]
            print(f"Updated {sub_code} marks for student {reg_no}: {students[reg_no][sub_code]}")
            print(f"No subject {sub_code} found for student {reg_no}")
    else:
        print(f"No student found with register number {reg_no}")


print(display_student_info( "101"))
print(display_marks_by_sub_code("101", "sub1"))
print(update_student_details("101", "sub1", 70,70,70))
