Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: E:\Harsh_DataAnalytics\patterns_file.py ===========
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
st = "This Is Python language"
st[0]
'T'
st[6]
's'
st1 = 'a'
type(st1)
<class 'str'>
type(st)
<class 'str'>
st[0] = 'M'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    st[0] = 'M'
TypeError: 'str' object does not support item assignment
del st[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    del st[0]
TypeError: 'str' object doesn't support item deletion
st.upper()
'THIS IS PYTHON LANGUAGE'
st.lower()
'this is python language'
st.title()
'This Is Python Language'
st.capitalize()
'This is python language'
st.swapcase()
'tHIS iS pYTHON LANGUAGE'
st.isupper()
False
st.islower()
False
st.istitle()
False
st.isalpha()
False
st.isalnum()
False
st1 = "ksndd562"
st1.isalnum()
True
st1.isdigit()
False
st1.isnum()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    st1.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
st1.isnumeric()
False
st = "   This Is Python language   "
st.strip()
'This Is Python language'
st.lstrip()
'This Is Python language   '
st.rstrip()
'   This Is Python language'
st.endswith(" ")
True
st.startswith(" ")
True
st.count('i')
1
st.index('I')
8
st.rindex('I')
8
st.index('z')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    st.index('z')
ValueError: substring not found
st.find('i')
5
st.find('z')
-1
st = "This Is Python language"
st.split()
['This', 'Is', 'Python', 'language']
st
'This Is Python language'
s = st.split()
s
['This', 'Is', 'Python', 'language']
for i in s:
    print(i)

This
Is
Python
language
" ".join(s)
'This Is Python language'
"-".join(s)
'This-Is-Python-language'
for i in st:
    print(i)

T
h
i
s
 
I
s
 
P
y
t
h
o
n
 
l
a
n
g
u
a
g
e
st[0:8:1]
'This Is '
st[8:1:-1]
'P sI si'
len(st)
23
st[22:0:-1]
'egaugnal nohtyP sI sih'
st[22:-1:-1]
''
st[-1]
'e'
st[-2]
'g'
st[22]
'e'
st[22,-22,-1]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    st[22,-22,-1]
TypeError: string indices must be integers, not 'tuple'
>>> st[22:-22:-1]
'egaugnal nohtyP sI si'
>>> st[22:-23:-1]
'egaugnal nohtyP sI sih'
>>> st[22:-24:-1]
'egaugnal nohtyP sI sihT'
>>> st[::-1]
'egaugnal nohtyP sI sihT'
>>> s
['This', 'Is', 'Python', 'language']
>>> s[::-1]
['language', 'Python', 'Is', 'This']
>>> st
'This Is Python language'
>>> st.replace('s','q')
'Thiq Iq Python language'
>>> st.replace('s','q',1)
'Thiq Is Python language'
