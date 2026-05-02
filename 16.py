balance = 5000
history = []
f = open("my personal bank.txt", "a")

while True:
    operation = input("\nspend or check or deposit or transaction history or view file or exit: ")
    
    if (operation == "spend"):
        item = input("enter a item: ")
        amount = int(input("enter amount for item: "))
        if (amount <= balance):
            balance = balance - amount
            log = f"debited: {item} - {amount}"
            history.append(log)
            f.write(log + "\n")
            print("debited amount", amount, "for", item)
        else:
            print("no more money")
            
    elif (operation == "check"):
        print("you have currently", balance)
        
    elif (operation == "deposit"):
        purpose = input("how you get this money: ")
        amount = int(input("enter amount for item: "))
        balance = balance + amount
        log = f"credited: {purpose} - {amount}"
        history.append(log)
        f.write(log + "\n")
        print(amount, "was credited to personal bank")
        
    elif (operation == "transaction history"):
        for item in history:
            print(item)
            
    elif (operation == "view file"):
        f_read = open("my personal bank.txt", "r")
        content = f_read.read()
        print(content)
        f_read.close()
        
    elif (operation == "exit"):
        print("save more money")
        f.close()
        break
