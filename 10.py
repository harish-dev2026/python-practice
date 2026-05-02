def calculate_landandrate(sqft, rate):
    return sqft * rate

s = int(input("enter square feet: "))
c = int(input("enter rate: "))
result = calculate_landandrate(s, c)
print("total rate: ", result)
