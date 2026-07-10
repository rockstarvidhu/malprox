bill_total = 200
discount1 = 10
discount2 = 20

if bill_total > 100 and bill_total < 210:
    print("bill is greater than 100!")
    bill_total = bill_total - discount1

elif bill_total > 100 and bill_total<200:
    print("bill is less than 200")
    bill_total = bill_total - discount2

else:
    print("bill is less than 100")

print("the total bill is: " , bill_total)
