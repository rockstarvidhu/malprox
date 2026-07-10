#outer loop
list1 = [1, 2, 3 ]
list2 = [2, 3, 4, 5, 6, 7, 8, 9]

#for x in list1:
 #   for y in list2:
  #      print(y, end = ' ')
   # print()

for i in range(9):
    for j in range(i-1):
        print("*", end = " ")
    print()
