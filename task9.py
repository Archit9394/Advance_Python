# 9. 	Create a login page backend to ask user to enter the UserEmail and password.
# Make sure to ask Re-Type Password and if the password is incorrect give chance to
# enter it again but it should not be more than 3 times.
userEmail="archit@gmail.com"
password="archit"

for i in range(3):
    email=input("Please enter your email:")
    pswd=input("Please enter your password")
    print (email.lower())
    if (email.lower()==userEmail and pswd==password):
        print('Welcome')
        break
    else:
        print ('Wrong Email or password')