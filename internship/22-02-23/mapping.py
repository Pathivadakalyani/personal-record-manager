#using filter function we can divide only even numbers in a given list
k=list(map(int,input('enter numbers with sp').split()))
new_list=list(filter(lambda x:x%2==0,k))
print(new_list)
