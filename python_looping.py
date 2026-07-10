str = 'looping'
for item in str:
    print(item)

favorites = ['creme brulee', 'tiramisu', "apple pie", 'marblecake']
for item in favorites:
    if item == 'creme brulee':
        print("yess", item)

count = 0
while count < len(favorites):
     print("i like the desert..", favorites[count])
     count += 1

n = 1
while n < 10:
    print("the value of n is ", n)
    n += 1
    