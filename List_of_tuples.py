#•	Develop code, which takes a list as an input and outputs 'list of tuples';
#where each tuple contains (index, value). Example: input = [2,3,4,5,6]; output = [(0,2), (1,3), (2,4), (3, 5), (4, 6)]


list=[2,3,4,5,6]
res = [(list.index(val), val) for val in list]
print(res)
