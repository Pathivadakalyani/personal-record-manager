Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


=============================================================== RESTART: C:/Users/Ramesh/Desktop/internship/22-02-23/1.py ==============================================================

=============================================================== RESTART: C:/Users/Ramesh/Desktop/internship/22-02-23/1.py ==============================================================

=============================================================== RESTART: C:/Users/Ramesh/Desktop/internship/22-02-23/1.py ==============================================================

=============================================================== RESTART: C:/Users/Ramesh/Desktop/internship/22-02-23/1.py ==============================================================
add(2,3)
'b is big'
square = lamda a:a**2
SyntaxError: invalid syntax
square=lamda a:a**2
SyntaxError: invalid syntax
square=lambda a:a**2
square(78)
6084
cube=lambda a:a**3
cube(3)
27
max(1,7,9)]
SyntaxError: unmatched ']'
max(1,7,9)
9
min(8,0,-2)
-2
h=lambda lst:max(lst)
h([1,2,8.0,-7])
8.0
k='8 0 7 9'
k.split()
['8', '0', '7', '9']

=============================================================== RESTART: C:/Users/Ramesh/Desktop/internship/22-02-23/2.py ==============================================================
['6', '8', '9', '0']
[6, 8, 9, 0]

=============================================================== RESTART: C:/Users/Ramesh/Desktop/internship/22-02-23/3.py ==============================================================
[4, 387420489, 16777216, 823543]
>>> 
=============================================================== RESTART: C:/Users/Ramesh/Desktop/internship/22-02-23/3.py ==============================================================
enter number with spaces 
=============================================================== RESTART: C:/Users/Ramesh/Desktop/internship/22-02-23/3.py ==============================================================
enter number with spaces 2 7 5 2 8 9
Traceback (most recent call last):
  File "C:/Users/Ramesh/Desktop/internship/22-02-23/3.py", line 22, in <module>
    new_lst=lst(map(square,lst))
TypeError: 'list' object is not callable
>>> 
=============================================================== RESTART: C:/Users/Ramesh/Desktop/internship/22-02-23/3.py ==============================================================
enter number with spaces 7 4 9 2 3
[823543, 256, 387420489, 4, 27]
>>> 
============================================================ RESTART: C:/Users/Ramesh/Desktop/internship/22-02-23/mapping.py ===========================================================
enter numbers with sp 3 9 6 3 
[6]
>>> string='i am {0} doing {1} at {2}'.format('eswar','p fs','codegnan')
>>> string
'i am eswar doing p fs at codegnan'
>>> name='kalyani'
>>> org='codegnan'
>>> ins='python full stack'
>>> h=f'i am {name} doing{ins} at {org}
SyntaxError: incomplete input
>>> h=f 'i am {name} doing{ins} at {org}'
SyntaxError: invalid syntax
>>> h=f'i am {name} doing{ins} at {org}'
>>> h
'i am kalyani doingpython full stack at codegnan'
>>> h=f 'i am {name} doing {ins} at {org}'
SyntaxError: invalid syntax
>>> h=f'i am {name} doing {ins} at {org}'
>>> h
'i am kalyani doing python full stack at codegnan'
>>> year=2023
>>> h=f'i am {name} doing {ins} at {org} {year}'
>>> h
'i am kalyani doing python full stack at codegnan 2023'
>>> j = 'i am '%s'%'kalyani'
SyntaxError: unterminated string literal (detected at line 1)
>>> j = 'i am %s '%'kalyani'
>>> j
'i am kalyani '
>>> 'i am kalyani '
'i am kalyani '
