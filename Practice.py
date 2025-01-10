
n = int(input("Enter the number"))
'''
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")'''
'''
count = 0
prime = True
for i in range(2,n//2+1):
    count += 1
    if n%i == 0:
        prime = False
        break
    
if prime:
    print("Number is prime",count)
else:
    print("Number is not prime",count)'''


for i in range(2,n//2+1):
    if n%i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
