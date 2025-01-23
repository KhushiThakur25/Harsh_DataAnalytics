
dic = {'1':'One',
       '2':'Two',
       '3':'Three',
       '4':'Four',
       '5':'Five',
       '6':'Six',
       '7':'Seven'}

n = input("Enter the value")

st = n.split()
rev = ""
print(st)
for i in st:
    rev += " " + dic.get(i)
print(rev)
