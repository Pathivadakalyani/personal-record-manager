Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> u=[]
>>> for i in range(0,11):
...     u.append(i)
... 
...     
>>> u
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> u=[i fo i in range(0,11)]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> u=[i for i in range(0,11)]
>>> u
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> #u=[exp for i in collection]
>>> u=[i if i%2==0 else 'NA' for i in range(0,11)]
>>> u
[0, 'NA', 2, 'NA', 4, 'NA', 6, 'NA', 8, 'NA', 10]
>>> #[expr for
>>> #[expr for loop_va in collec]
>>> #[expr for loop
>>> #[expr for loop

... -
