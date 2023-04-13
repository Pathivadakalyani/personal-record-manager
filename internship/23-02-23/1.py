Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> o=map(int['1','2'])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    o=map(int['1','2'])
TypeError: type 'int' is not subscriptable
>>> o=map(int,['1','2'])
>>> o
<map object at 0x000002040FD0B910>
>>> list(o)
[1, 2]
>>> lst=[1,7,9,5]
>>> lst[1,7,2,4,9]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    lst[1,7,2,4,9]
TypeError: list indices must be integers or slices, not tuple
>>> lst=[1,7,2,4,9]
>>> result=filter(lambda x:x%2==0,lst)
>>> result
<filter object at 0x000002040FD0B790>
>>> list(result)
[2, 4]
>>> 
>>> o=True
>>> t=o if o==True else 'eswar'
>>> t
True
>>> if o==True:
...     t=oelse:
...         
SyntaxError: incomplete input
>>> if o==True:
...     t=o
... else:
...     t='eswar'
... 
...     
>>> t
True
