from datetime import dt
class first:
    def __init__(self):
        print("1. SAVING ACCOUNT")
        print("2. CURRENT ACCOUNT")

        n = int(input("Enter your choice : "))

        if n == 1:
            a = 20000
            print(a)
        elif n == 2:
            a = 30000
            print(a)
        else:
            print("Invalid Choice")
            exit()

        self.passw = "123"
        self.transactions = []

    def logic(self):
        cnt=1
        while cnt <= 3:
            password = input("Enter password : ")

            if passw == password:
                print("YOUR ACCOUNT IS OPEN SUCCESSFULLY..!")
                break
            else:
                cnt += 1
                if cnt <= 3:
                    print("WRONG PASSWORD...")
                else:
                    print("EXIT")
                    exit()
