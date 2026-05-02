items = {
    "rice": 60,
    "dal": 33,
    "sugar": 45,
}

while True:
    item = input("enter your item, exit: ")
    
    if (item == "exit"):
        print("thankyou please come again")
        break
        
    if item in items:
        price = items[item]
        print(f"product={item} price={price}")
        
        quantity = int(input("how many kg you need: "))
        totalprice = quantity * price
        print("for", quantity, "kg", "price:", totalprice, "rupees")
    else:
        print("sorry currently item arenot available")
