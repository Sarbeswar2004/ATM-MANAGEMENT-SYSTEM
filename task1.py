import time
print("Please insert your card :")
time.sleep(5)
password=1234
balance=5000
pin=int(input("Enter your ATM pin :"))
if pin==password:
    while True:
        print("1. Balance Enquiry.\n2. Withdraw Balance.\n3. Deposit Balance.\n4. Exit ")
        try:
            option=int(input("Please Enter Your Choice :"))
        except:
            print("==================================================")
            print("==================================================")
            print("Please Enter Valid Option.")
            print("==================================================")
            print("==================================================")

        if option==1:
            print("==================================================")
            print("==================================================")
            print(f"Your current balance is {balance}.")
            print("==================================================")
            print("==================================================")
        if option==2:
            withdraw_amount=int(input("Please Enter Withdraw_Amount :"))
            if balance >= withdraw_amount:
                balance=balance-withdraw_amount
                print("==================================================")
                print("==================================================")
                print(f"{withdraw_amount} is debited successfully.")
                print("==================================================")
                print("==================================================")
                print(f"Your updated balance is {balance}.")
                print("==================================================")
                print("==================================================")
            else:
                print("Insufficient Balance.Please try again later.")
                print("==================================================")
                print("==================================================")
        if option==3:
            deposit_amount=int(input("Please Enter Deposit_Amount :"))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited successfully.")
            print("==================================================")
            print("==================================================")
            print(f"Your updated balance is {balance}.")
            print("==================================================")
            print("==================================================")
            
        if option==4:
            break
    print("Thank You. Visit Again.")
else:
    print("Wrong Pin, Please Try Again Later!\nThank you Have a Nice Day...")
    
