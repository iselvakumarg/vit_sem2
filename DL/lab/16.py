# Write a Python code to read the content of ‘ebook.txt’ and display the contents of the file onto the console. 

with open("ebook.txt", "r") as f:
    print(f.read())
