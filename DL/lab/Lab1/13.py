# Obtain a nested list use looping constructs and list comprehension to flatten the list. Example: [[1],[2,3],[4,5,6],[7,8,9,10]] o/p: [1,2,3,4,5,6,7,8,9,10] 

def flatten_list(l):
    return [i for j in l for i in j]

print(flatten_list([[1],[2,3],[4,5,6],[7,8,9,10]]))

