unit=int(input("Enter unit = "))

if unit<=50:
    bill=unit*1
elif unit>50 and unit<=100:
    bill=50+(unit-50)*2
elif unit>100 and unit<=200:
    bill=50+100+(unit-100)*3
elif unit>200 and unit<=400:
    bill=50+100+300+(unit-200)*4
else:
    bill=50+100+300+800+(unit-400)*5

bill=bill+(bill/10)
print("bill = ",bill)
