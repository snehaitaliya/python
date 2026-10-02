f=open("bank.txt","a")
from datetime import datetime
while True:
    print("1. SAVING ACCOUNT")
    print("2. CURRENT ACCOUNT")

    n=int(input("Enter your choice : "))

    if n==1 or n==2:
        if n==1:
            a=20000
            print(a)
            break
        else:
            a=30000
            print(a)
            break
    else:
        print("Enter valide choice :")
    
while True:

    p=input("Enter password :")
    al=0
    d=0
    valid=True

    for i in p:
        av=ord(i)
        if (65<=av<=90) or (97<=av<=122):
            al+=1
        elif (48<=av<=57):
            d+=1
        else:
            valid=False
            break

    if al>0 and d>0 and valid:
        print("Password entered SUCCESSFULLY..!!")
        break
    else:
        print("You should contain only alphabet or digit")
        
cnt=1
while cnt<=3:
    password=input("Enter confirm password : ")

    if p==password:
        print("YOUR ACCOUNT IS OPEN SUCCESSFULLY..!")
        break
    else:
        cnt+=1
        if cnt<=3:
            print("WRONG PASSWORD...")
        else:
            print("EXIT")
            exit()

t=[]
while True:

    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Change Password")
    print("5. Print Passbook")
    print("6. Exit")

    n1=input("Enter your choice : ")

    # Withdraw
    if n1=="1":
        password=input("Enter password : ")
        cnt=1
        while cnt<=3:
            password=p

            if p==password:
                print("OPEN YOUR ACCOUNT...!")
                break
            else:
                cnt+=1
                if cnt<=3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()


        if password==p:
            w=int(input("Enter withdraw amount : "))

            if a-w>=5000:
                a-=w

                dt=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                t.append(
                    f"Withdraw  ₹{w}  Balance: ₹{a}  {dt}"
                )
                print("WITHDRAW SUCCESSFUL")
                print("Balance =", a)
            else:
                print("Minimum balance ₹5000 required.")
        else:
            print("Wrong Password")

    # Deposit
    elif n1=="2":
        password=input("Enter password : ")
        cnt=1
        while cnt<=3:
            password=p
            if p==password:
                print("OPEN YOUR ACCOUNT...!")
                break
            else:
                cnt+=1
                if cnt<=3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()
        if password==p:
            dep=int(input("Enter deposit amount : "))

            if dep<=25000:
                a+=dep
                dt=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                t.append(
                    f"Deposit  ₹{dep}  Balance: ₹{a}  {dt}"
                )
                print("DEPOSIT SUCCESSFUL")
                print("Balance =", a)
            else:
                print("Maximum deposit limit is ₹25000")
        else:
            print("Wrong Password")

     # Check Balance
    elif n1=="3":
        password=input("Enter password : ")

        cnt=1
        while cnt<=3:
            password=p

            if p==password:
                print("OPEN YOUR ACCOUNT...!")
                break
            else:
                cnt+=1
                if cnt<=3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()

        print("Current Balance =", a)

    # Change Password
    elif n1=="4":

        cnt=1
        while cnt<=3:
            password=p

            if p==password:
                print("OPEN YOUR ACCOUNT...!")
                break
            else:
                cnt+=1
                if cnt<=3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()

        if password==p:
           
            while True:

                p=input("Enter password :")
                al=0
                d=0
                valid=True

                for i in p:
                    av=ord(i)
                    if (65<=av<=90) or (97<=av<=122):
                        al+=1
                    elif (48<=av<=57):
                        d+=1
                    else:
                        valid=False
                        break

                if al>0 and d>0 and valid:
                    print("Password entered SUCCESSFULLY..!!")
                    break
                else:
                    print("You should contain only alphabet or digit")
            cnt=1
            while cnt<=3:
                ppw=input("Confirm new password :")

                if p==ppw:
                    print("OPEN YOUR ACCOUNT...!")
                    break
                else:
                    cnt+=1
                    if cnt<=3:
                        print("WRONG PASSWORD...")
                    else:
                        print("EXIT")
                        
    # Passbook
    elif n1=="5":

        cnt=1
        while cnt<=3:
            password=p

            if p==password:
                print("OPEN YOUR ACCOUNT...!")
                break
            else:
                cnt+=1
                if cnt<=3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()

        if len(t)==0:
            print("No Transactions Found")
        else:
            for t in t:
                print(t)
        print("Current Balance :", a)

    # Exit
    elif n1=="6":
        print("Thank You !")
        break
    else:          
        print("Invalid Choice")