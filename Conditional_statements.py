n = int(input("Enter the number n.."))
m = int(input("Enter the number m.."))
p = int(input("Enter the number p.."))
'''if n%2 == 0:
    print("Number is even..")
else:
    print("Number is odd..")'''

'''if n > m:
    print("n is greater..")
else:
    print("m is greater..")'''

if n > m and n > p:
    print("n is greatest..")
elif m > n and m > p:
    print("m is greatest..")
else:
    print("p is greatest..")

