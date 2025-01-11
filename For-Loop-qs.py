n = int(input("Enter the number.."))
'''
sums = 0
for i in range(1,n+1):
    sums += i
print("Sums is :",sums)

fact = 1
for i in range(n,0,-1):
    fact *= i
print("Factorial is :",fact)
'''

first = 0
second = 1
print(first,second,end = " ")
for i in range(n-2):
    third = first + second
    print(third,end = " ")
    first = second
    second = third
