'''n = int(input("Enter the value of n"))
m = int(input("Enter the value of m"))
if n < 0 and m < 0:
    print("Numbers are negative",n,m)
elif n > 0 and m > 0:
    print("Numbers are positive",n,m)
elif n > 0 and m < 0:
    print("n is positive but m is negative")
elif n < 0 and m > 0:
    print("m is positive but n is negative")
else:
    print("Number is zero",n)'''

'''year = int(input("Enter the year"))
if year%4 == 0:
    print("year is leap year..")
elif year%100 == 0:
    print("Year is not a leap year..")
else:
    print("Year is not a leap year..")'''
'''
print("Enter your marks of..")
py = int(input("Physics"))
ch = int(input("chemistry"))
bi = int(input("biology"))
ma = int(input("maths"))
co = int(input("computer"))

total = py + ch + bi + ma + co
percentage = total/5
print("your percentage is:",percentage)
print("Your grade is:",end = " ")
if percentage > 90:
    print("A")
elif percentage > 80:
    print("B")
elif percentage > 70:
    print("C")
elif percentage > 60:
    print("D")
elif percentage > 50:
    print("E")
elif percentage > 40:
    print("F")
else:
    print("Fail")
'''
b_salary = int(input("Enter your basic salary.."))

if b_salary <= 10000:
    HRA = 0.2 * b_salary
    DA = 0.8 * b_salary
elif b_salary <= 20000:
    HRA = 0.25 * b_salary
    DA = 0.9 * b_salary
else:
    HRA = 0.3 * b_salary
    DA = 0.95 * b_salary
print("Your gross salary is:",b_salary+HRA+DA)
