contacts = {
    "jayanthi": 7904727311,
    "sathya": 8015188818
}

while True:
    contact = input("enter a name or exit: ")
    if (contact == "exit"):
        print("back to homescreen")
        break
        
    if contact in contacts:
        number = contacts[contact]
        print(f"contact name: {contact}, number: {number}")
    else:
        print("sorry contact number are not avilabe")
        
        addnumber = input("do you want add new number, yes or no: ")
        if (addnumber == "yes"):
            new_number = input(f"enter number for {contact}: ")
            contacts[contact] = new_number
            print(f"{contact} has been saved into contact")
