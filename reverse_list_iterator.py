#Develop code that considers a given list and iterates it from the reverse direction. (Use iterator class for this problem).


input_list = [0,1,2,3,4,5,6,7,8,9]
my_list = input_list[::-1]
value=my_list.__iter__()
for i in my_list:
    try:
        item=value.__next__()
        print(item)
    except StopIteration:
        break