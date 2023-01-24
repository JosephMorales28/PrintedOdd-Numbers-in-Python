oddnumber=[1,3,5,7,9]
print(oddnumber)
print("\nAnother printed odd numbers using range")
odd=list(values + 1 for values in range(0,10,2))
print(odd)
print("\n2nd printed odd numbers using range")
odd_1=[values +1 for values in range(0,10,2)]
print(odd_1)
print("\n3rd printed odd number using if, else ,for loop and range")
for oddnumbers1 in range(0,10):
    if oddnumbers1%2==0:
        continue
    else:
        print(oddnumbers1)
print("\n4th printed odd numbers in right triangle mode")
odd_2=[]
for values in range(0,10,2):
    odd_=values +1
    odd_2.append(odd_)
    print(odd_2)
print("\n5th printed odd numbers in right triangle short code")
odd_3=[]
for values in range(0,10,2):
    odd_3.append(values +1)
    print(odd_3)
