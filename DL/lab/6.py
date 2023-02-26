# Write  a  program  that  takes  user’s  name  and  PAN  card  number.  Validate  the information using string functions
name = input("Enter the user name: ")
pan_no = input("Enter the PAN number: ")

print("Checking whether the name is valid: ", name.isalpha())
print("Checking whether the PAN number is valid: ", pan_no.isalnum())