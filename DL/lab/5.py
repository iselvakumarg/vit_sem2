str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
str3 = input("Enter a string: ")


if str1 < str2 and str1 < str3:
    if str2 < str3:
        print(str1, str2, str3)
    else:
        print(str1, str3, str2)

elif str2 < str1 and str2 < str3:
    if str1 < str3:
        print(str2, str1, str3)
    else:
        print(str2, str3, str1)
        
else:
    if str1 < str2:
        print(str3, str1, str2)
    else:
        print(str3, str2, str1)



