file = open('data.txt','r')
data = file.read()
#data = file.read(100)
#data = file.readline()
# file.seek(50)
# data = file.read()
print(data)
file.close()

'''types of file is 
1.text file - 
2.binary file - images

modes of file are:
1.read - 'r','rb'
2.write - 'w','wb'
3.append - 'a','ab'
4.xwrite - 'x','xb' '''