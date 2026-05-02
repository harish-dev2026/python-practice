balance = 5000
print("atm machine")

while True:
    print("\nno.1 check balance", "no.2 cash withdrawal", "no.3 exit")
    
    choice = input("1 2 3: ")
    user_pin = 7717
    pin = int(input("enter your pin: "))
    
    if (choice == "1" and user_pin == pin):
        print("your current balance", balance)
        
    elif (choice == "2" and user_pin == pin):
        amount = int(input("enter your amount: "))
        if (amount <= balance):
            balance = balance - amount
            print("cash withdrawal completed", "balance amount:", balance)
        else:
            print("insuficient balance", "or wrong pin")
            
    elif (choice == "3" and user_pin == pin):
        print("thank you please come again")
        break
    else:
        print("sorry wrong pin")
