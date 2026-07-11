list1 = [1, 2, 3, 4, 5]
#print function to print all elements in list
print(*list1)
print(list1, sep = "  ")

#inserting value to list
list1.insert(list1[2], 6)
print(list1)

#append function
list1.append(44)
print(list1)

#to extend list
list1.extend([6, 77, 89, 99])
print(list1)

#to remove elements
list1.pop(4)
print(list1)

del list1[3]
print(list1)


#iterating through list
for x in list1:
    print("value is : ", x)
    