#Palindrome String..a = "aba", rev = "aba"


st = input("Enter the string..").lower()
'''
rev = st[::-1]
if st == rev:
    print("string is palindrome..")
else:
    print("string is not palindrome..")
'''
'''
st = st.split()
print(st)
for i in st:
    if len(i)%2 != 0:
        print(i)
    
'''
'''
st = st.replace(',',"third")
st = st.replace('.',",")
st = st.replace('third',".")
print(st)

'''
count = 0
for i in st:
    if i == 'i' or i == 'a' or i == 'e' or i == 'o' or i == 'u':
        count += 1
print(count)


















