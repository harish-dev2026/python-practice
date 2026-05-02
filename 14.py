balance = 5000
history = []

while True:
    operation = input("spend or check or exit or deposit or transaction history: ")
    
    if (operation == "exit"):
        print("save more money")
        break
        
    elif (operation == "spend"):
        item = input("enter a item: ")
        amount = int(input("enter amount for item: "))
        if (amount <= balance):
            balance = balance - amount
            history.append(f"spend: {item} - {amount}")
            print(amount, "was spent for", item)
        else:
            print("currently have a", balance, "only")
            
    elif (operation == "check"):
        print(balance)
        
    elif (operation == "transaction history"):
        print(history)
        
    elif (operation == "deposit"):
        amount = int(input("enter amount for deposit: "))
        balance = balance + amount
        history.append(f"deposit - {amount}")
        print("currently you have a", balance)
        
    else:
        print("wrong option choosed")
