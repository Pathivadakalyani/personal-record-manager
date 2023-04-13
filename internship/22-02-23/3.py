'''k=input('enter numbers with spaces')
print(k.split())
l=[]
for i in k.split():
     l.append(int(i))
print(l,b-a)'''


#square the list of numbers within a list
def square(a):
    return a**a
'''lst=[2,9,8,7]
lst2=[]
for i in lst:
    lst2.append(square(i))
print(lst2)
k=tuple(map(int,input('enter number with spaces').split())
print(k)
'''
#Another  method of list using map
lst=list(map(int,input('enter number with spaces ').split()))
new_lst=list(map(square,lst))
print(new_lst)




    
