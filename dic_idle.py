Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
di = {'name':'Amit','class':5,'roll-no':2,'marks':85}
type(di)
<class 'dict'>
di['session'] = 2020
di
{'name': 'Amit', 'class': 5, 'roll-no': 2, 'marks': 85, 'session': 2020}
dic = {'dep':'HR','Subj':'finance','salary':50000}
dic
{'dep': 'HR', 'Subj': 'finance', 'salary': 50000}
di
{'name': 'Amit', 'class': 5, 'roll-no': 2, 'marks': 85, 'session': 2020}
di.update(dic)
di
{'name': 'Amit', 'class': 5, 'roll-no': 2, 'marks': 85, 'session': 2020, 'dep': 'HR', 'Subj': 'finance', 'salary': 50000}
di.keys()
dict_keys(['name', 'class', 'roll-no', 'marks', 'session', 'dep', 'Subj', 'salary'])
di.values()
dict_values(['Amit', 5, 2, 85, 2020, 'HR', 'finance', 50000])
di.items()
dict_items([('name', 'Amit'), ('class', 5), ('roll-no', 2), ('marks', 85), ('session', 2020), ('dep', 'HR'), ('Subj', 'finance'), ('salary', 50000)])
di['class']
5
di['class'] = 6
di
{'name': 'Amit', 'class': 6, 'roll-no': 2, 'marks': 85, 'session': 2020, 'dep': 'HR', 'Subj': 'finance', 'salary': 50000}
dic.pop('roll-no')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dic.pop('roll-no')
KeyError: 'roll-no'
>>> di.pop('roll-no')
2
>>> di
{'name': 'Amit', 'class': 6, 'marks': 85, 'session': 2020, 'dep': 'HR', 'Subj': 'finance', 'salary': 50000}
>>> di.popitem()
('salary', 50000)
>>> di
{'name': 'Amit', 'class': 6, 'marks': 85, 'session': 2020, 'dep': 'HR', 'Subj': 'finance'}
>>> di.get('name')
'Amit'
>>> marks = {'sub':{'hindi':56,'eng':85,'maths':45},'colors':['red','green','yellow','blue']}
>>> marks.get('eng')
>>> marks['eng']
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    marks['eng']
KeyError: 'eng'
marks['sub']['eng']
85
marks['colors'][1]
'green'
