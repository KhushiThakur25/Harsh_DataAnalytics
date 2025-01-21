Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============== RESTART: E:/Harsh_DataAnalytics/List_Qs.py ==============
tu = 1,23,45,64,5,6
type(tu)
<class 'tuple'>
tu[0]
1
tu[1]
23
tu[0:2]
(1, 23)
tu[0] = 100
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tu[0] = 100
TypeError: 'tuple' object does not support item assignment
tu.count(6)
1
>>> tu.index(45)
2
>>> len(tu)
6
>>> max(tu)
64
>>> min(tu)
1
>>> sum(tu)
144
>>> tu = list(tu)
>>> type(tu)
<class 'list'>
>>> tu[0] = 100
>>> tu = tuple(tu)
>>> type(tu)
<class 'tuple'>
>>> tu
(100, 23, 45, 64, 5, 6)
