Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = [1,2,3,4,5,6,7,8,9,10]
type(li)
<class 'list'>
k = ["apple",23,"ok"]
type(k)
<class 'list'>
m = list()
m
[]
k.append(56)
k
['apple', 23, 'ok', 56]
n = k
k
['apple', 23, 'ok', 56]
n
['apple', 23, 'ok', 56]
k[0]="mango"
k
['mango', 23, 'ok', 56]
n
['mango', 23, 'ok', 56]
k is n
True
b = k.copy()
b
['mango', 23, 'ok', 56]
k
['mango', 23, 'ok', 56]
b is k
False
b[0] = 56
b
[56, 23, 'ok', 56]
k
['mango', 23, 'ok', 56]
b.clear()
b
[]
n.insert(2,"amit")
n
['mango', 23, 'amit', 'ok', 56]
n[0] = "hello"
n
['hello', 23, 'amit', 'ok', 56]
k.append(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    k.append(1,2,3,4,5)
TypeError: list.append() takes exactly one argument (5 given)
k.append([1,2,3,4,5])
k
['hello', 23, 'amit', 'ok', 56, [1, 2, 3, 4, 5]]
k.extend([1,2,3,4,5])
k
['hello', 23, 'amit', 'ok', 56, [1, 2, 3, 4, 5], 1, 2, 3, 4, 5]
k.remove([1, 2, 3, 4, 5])
k
['hello', 23, 'amit', 'ok', 56, 1, 2, 3, 4, 5]
k.pop()
5
k.index(3)
7
k.append(23)
k.count(23)
2
k.reverse()
k
[23, 4, 3, 2, 1, 56, 'ok', 'amit', 23, 'hello']
k.sort()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    k.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
li.sort()
li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li.sort(reverse = True)
li
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
max(li)
10
min(li)
1
sum(li)
55
len(li)
10
lis = [[1,2,3],[4,5,6],[7,8,9]]
for i in lis:
    print(i)

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
>>> lis[0][1]
2
>>> lis[1][0]
4
>>> for i in range(len(lis)):
...     for j in range(len(lis[0])):
...         lis[i][j] += 1
... 
>>> lis
[[2, 3, 4], [5, 6, 7], [8, 9, 10]]
>>> for i in range(len(lis)):
...     for j in range(len(lis[0])):
...         print(lis[i][j],end=" ")
...     print()
... 
2 3 4 
5 6 7 
8 9 10 
