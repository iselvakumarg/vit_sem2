# Give an appropriate list comprehension for each of the following: i) L1 = [1, ’x’, 4, 5.6, ’z’, 9, ‘a’, 0, 4] create a list which consists of integer values. ii) Producing a list of consonants that appear in string w. iii) Multiples of 10 (n values) iv) Construct a list of the form: [‘1a’,’2a’,’3a’,’4a’] v) Create a list which stores the sum of each of the elements from the two lists.

# i) L1 = [1, ’x’, 4, 5.6, ’z’, 9, ‘a’, 0, 4] create a list which consists of integer values.
L1 = [1, 'x', 4, 5.6, 'z', 9, 'a', 0, 4]
L2 = [i for i in L1 if type(i) == int]
print(L2)

# ii) Producing a list of consonants that appear in string w.
w = 'This is a string'
L3 = [i for i in w if i not in 'aeiou']
print(L3)

# iii) Multiples of 10 (n values)
L4 = [i for i in range(100) if i % 10 == 0]
print(L4)

# iv) Construct a list of the form: [‘1a’,’2a’,’3a’,’4a’]
L5 = [str(i) + 'a' for i in range(1, 5)]
print(L5)

# v) Create a list which stores the sum of each of the elements from the two lists.
L6 = [1, 2, 3, 4]
L7 = [5, 6, 7, 8]
L8 = [L6[i] + L7[i] for i in range(len(L6))]
print(L8)
