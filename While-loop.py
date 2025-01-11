
'''
while i <= 10:
    print(i)
    i += 1'''
'''
n = 5
while i<= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1
'''
'''
n = 186965
count = 0
while n > 0:
    count += 1
    n //= 10
print("count of digit is:",count)'''
n = 123456
rev = 0
while n > 0:
    rev = rev * 10 + n%10
    n //= 10
print(rev)
