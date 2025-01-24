Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = [23,45,10,5,16,16,15,45,89]
>>> 9/5*23+32
73.4
>>> def covert(c):
...     return 9/2*c+32
... 
>>> temp = []
>>> for i in li:
...     temp.append(convert(i))
... 
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    temp.append(convert(i))
NameError: name 'convert' is not defined. Did you mean: 'covert'?
>>> for i in li:
...     temp.append(covert(i))
... 
>>> temp
[135.5, 234.5, 77.0, 54.5, 104.0, 104.0, 99.5, 234.5, 432.5]
map(covert,li)
<map object at 0x000001271E8EA890>
list(map(covert,li))
[135.5, 234.5, 77.0, 54.5, 104.0, 104.0, 99.5, 234.5, 432.5]
def even(n):
    return n%2 == 0

def odd(n):
    return n%2 != 0

list(filter(even,li))
[10, 16, 16]
list(filter(odd,li))
[23, 45, 5, 15, 45, 89]
eval("23+52/61*1+28")
51.85245901639344
exec('a = 5')
a
5
exec('23+52/61*1+28')
m = exec('23+52/61*1+28')
m
m
m = exec('a = 23+52/61*1+28')
m
a
51.85245901639344
