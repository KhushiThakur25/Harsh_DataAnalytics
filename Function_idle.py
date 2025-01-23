Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def greet():
    print("Hello world")

greet()
Hello world
name = input("enter the name..")
enter the name..riya
def greet(name):
    print("hello",name)

greet(name)
hello riya
def greet(name):
    return "hello",name

greet("siya")
('hello', 'siya')
s = greet("siya")
s
('hello', 'siya')
def greet():
    return "hello"

s = greet()
s + "geet"
'hellogeet'
s + " geet"
'hello geet'
def calc(a,b,c):
    print(a+b+c)

calc(2,3,4)
9
def calc(a,b,c):
    print(a,b,c)

calc(3,2,4)
3 2 4
calc(x = 2,y = 3,z = 5)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    calc(x = 2,y = 3,z = 5)
TypeError: calc() got an unexpected keyword argument 'x'
calc(a = 2,c = 3,b = 5)
2 5 3
def calc(a = 2,c = 3,b = 5):
...     print(a,b,c)
... 
>>> calc(12)
12 5 3
>>> def calc(a,b,c):
...     print(a,b,c)
... 
>>> calc(2)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    calc(2)
TypeError: calc() missing 2 required positional arguments: 'b' and 'c'
>>> def detail(args*):
...     
SyntaxError: invalid syntax
>>> def detail(*args):
...     print(args)
... 
>>> detail(1,2,4,5,6,5)
(1, 2, 4, 5, 6, 5)
>>> def detail(**kwargs):
    print(kwargs)

detail('name':'Riya','class':3)
SyntaxError: invalid syntax
detail('name'='Riya','class'=3)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
detail(name='Riya',classs=3)
{'name': 'Riya', 'classs': 3}
