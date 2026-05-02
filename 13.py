print("smart shop bill")
prices = {
    "rice": 45,
    "oil": 150,
    "sugar": 30
}

while True:
    item = input("enter item or exit: ")
    if (item == "exit"):
        print("thank you sir come again")
        break
        
    if item in prices:
        item_price = prices[item]
        print(f"product: {item}, price: {item_price}")
        
        quantity = int(input(f"how many kg or liter you want for {item}: "))
        total_price = quantity * item_price
        print("for", quantity, "kg", "price: ", total_price)
        
    else:
        print("there product are not available")
        
        add_product = input("do you want add new product yes or no: ")
        if (add_product == "yes"):
            new_product = int(input(f"enter price for {item}: "))
            prices[item] = new_product
            print(f"{item} stored in a smart shop bill")
