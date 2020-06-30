# 6. 	Write a program in Python using generators to reverse the string. 
# Input String = “Consultadd Training”


string1="Consultadd Training"
def reverse(string1):
    for i in string1[::-1]:
        yield i

for i in reverse(string1):
    print (i,end='')