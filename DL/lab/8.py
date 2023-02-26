# Write a Python program to strip a set of characters from a string Encrypt a given  message by “rotating” each letter by a fixed number of places. To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary, so ‘A’ rotated by 3 is ‘D’ and ‘Z’ rotated by 1 is ‘A’. Write a function called rotate_word that takes a string and an integer as parameters, and returns a new string that contains the  letters  from  the  original  string  rotated  by  the  given  amount.  E.g  Given  String: HAL Encrypted String: JCN (Rotated by 2)

def rotate_word(s, n):
    return ''.join([chr(ord(i) + n) for i in s])

print(rotate_word('HAL', 2))
