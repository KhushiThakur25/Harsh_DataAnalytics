Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = set()
st
set()
type(st)
<class 'set'>
st = {}
type(st)
<class 'dict'>
st = {1,2,3,4,5,1,2,1,2,1,3}
len(st)
5
st
{1, 2, 3, 4, 5}
st1 = {4,5,6,7,8}
st2 = {2,3,4}
st.union(st1)
{1, 2, 3, 4, 5, 6, 7, 8}
st
{1, 2, 3, 4, 5}
st1
{4, 5, 6, 7, 8}
st.update(st1)
st
{1, 2, 3, 4, 5, 6, 7, 8}
st = {1,2,3,4,5,1,2,1,2,1,3}
st.intersection(st1)
{4, 5}
st
{1, 2, 3, 4, 5}
st.intersection_update(st1)
st
{4, 5}
st = {1,2,3,4,5,1,2,1,2,1,3}
st2.issubset(st)
True
st1.issubset(st)
False
st2.issuperset(st)
False
st3 = {1,2}
st1.isdisjoint(st3)
True
st.difference(st2)
{1, 5}
st.symmetric_difference(st1)
{1, 2, 3, 6, 7, 8}
st
{1, 2, 3, 4, 5}
st.add(56)
st
{1, 2, 3, 4, 5, 56}
st3.clear()
st3
set()
st2.remove(4)
st2
{2, 3}
st2.remove(6)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    st2.remove(6)
KeyError: 6
>>> st2.discard(4)
>>> st2.discard(6)
>>> st2
{2, 3}
>>> st2.popitem()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    st2.popitem()
AttributeError: 'set' object has no attribute 'popitem'
>>> st
{1, 2, 3, 4, 5, 56}
>>> st[0]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    st[0]
TypeError: 'set' object is not subscriptable
>>> frozenset(st)
frozenset({1, 2, 3, 4, 5, 56})
>>> st.add(56)
>>> st = frozenset(st)
>>> st.add(23)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    st.add(23)
AttributeError: 'frozenset' object has no attribute 'add'
