# Write a program to Python find the values which is not divisible 3 but is
# should be a multiple of 7. Make sure to use only higher order function.

integers=[20,31,7,21,9,35,42]
ans=filter(lambda x:x%3!=0 and x%7==0,integers)
print (list(ans))