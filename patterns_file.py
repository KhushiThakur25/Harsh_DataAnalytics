'''for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4 or i==j or j == 4-i:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()  '''       
'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
for i in range(5):
    for j in range(5-i,0,-1):
        print(j,end = " ")
    print()
'''

for i in range(5):
    for j in range(4-i):
        print("-",end = " ")
    for k in range(4-i,5):
        print("*",end = " ")
    print()















