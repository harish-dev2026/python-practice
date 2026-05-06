subjects = {
    "tamil": "completed",
    "english": "completed",
    "accountancy": "completed",
}

while True:
    subject = input("enter subject, exit: ")
    if (subject == "exit"):
        print("all the best for your exam")
        break
        
    if subject in subjects:
        task = subjects[subject]
        print(f"subject: {subject}, your task is: {task}")
    else:
        print("sorry there are no subject available")
        newsubject = input("do you want enter new subject yes or no: ")
        if (newsubject == "yes"):
            new_subject = input(f"enter task completed or not for {subject}: ")
            subjects[subject] = new_subject
            print(f"your {subject} task is stored.")
