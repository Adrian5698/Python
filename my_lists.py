#Week 2 Assignment on Lists
my_list = []
print('My_list', my_list)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.insert(1, 15)
print(my_list)
another_list = [50, 60, 70]
my_list.extend(another_list)
print(my_list)
my_list.pop(-1)
print(my_list)
my_list.sort()
print(my_list)
index = my_list.index(30)
print('Index of value 30 is;', index)