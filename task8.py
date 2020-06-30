# 8. 	Write a program to handle an error if the user entered the number more than
# four digits it should return “Please length is too short/long !!! Please provide only four
# digits”
while True:
    try:
        password=int(input("Enter a 4 Digit password:"))
        if (password>=1000 and password<=9999):
            print("Welcome")
            break
        else:
            print ("Please length is too short/long !!! Please provide only four digits")
    except ValueError:
        print("Please provide a valid input")
        