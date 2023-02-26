# Given a list, find frequency of each element and save it as list of tuple [(number, frequency)]. Input : test_list = [4, 5, 4, 5, 6, 6, 5] Output : [(4, 2), (5, 3), (6, 2)] Input : test_list = [4, 5, 4, 5, 6, 6, 6] Output : [(4, 2), (5, 3), (6, 3)] 

def frequency(l):
    return [(i, l.count(i)) for i in set(l)]

print(frequency([4, 5, 4, 5, 6, 6, 5]))
print(frequency([4, 5, 4, 5, 6, 6, 6]))