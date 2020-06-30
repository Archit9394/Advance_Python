#2. Write a program in Python to multiple the element of list by itself using a
# traditional function and pass the function to map to complete the operation.

list1= [1,2,3,4,5,6]
ans= map(lambda i:i*i,list1)
print(list(ans))