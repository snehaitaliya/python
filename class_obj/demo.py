from datetime import datetime

while True:
    print("1. SAVING ACCOUNT")
    print("2. CURRENT ACCOUNT")

    n = int(input("Enter your choice : "))

    if n == 1:
        a = 20000
        print("Balance :", a)
        break
    elif n == 2:
        a = 30000
        print("Balance :", a)
        break
    else:
        print("Invalid Choice! Please enter 1 or 2.\n")

transactions = []

while True:
    passw=input("Enter Password : ")
    if passw.isalpha():
        print("Password should contain only alphabets and digits.")
    elif passw.isnumeric():
        print("Password should contain only alphabets and digits.")
    else:
        if passw.isalnum():
            print("Password Created Successfully!")
        else:
            print("Password should contain only alphabets and digits.")
        break        
        
        