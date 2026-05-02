def calculate_landandrate(sqft, rate):
    total = sqft * rate
    
    if (total > 5000000):
        discount = total / 10
        finalprice = total - discount
        print("discount rate:", discount)
        return finalprice
    else:
        print("no discount applied.")
        return total

s = int(input("sqft: "))
p = int(input("rate: "))
result = calculate_landandrate(s, p)
print("total rate:", result)
