def add(n,m):
    print("sum is",n+m)
def sub(n,m):
    print("sub is",n-m)
def mul(n,m):
    print("mul is",n*m)
def div(n,m):
    print("div is",n/m)

while True:
    n = int(input("Enter the number 1"))
    m = int(input("Enter the number 2"))
    print("""
    Enter your choice:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    """)
    ch = input("Enter the choice..")

    if ch == '+':
        add(n,m)
    elif ch == '-':
        sub(n,m)
    elif ch == '*':
        mul(n,m)
    elif ch == '/':
        div(n,m)
    else:
        print("Invalid input")
        break
