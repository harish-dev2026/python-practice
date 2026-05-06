import datetime
task=[]
f=open("MY-TO-DO-LIST.txt","a")

while True:
    print("---MY-TO-DO-LIST")

    choice=input("add view remove view file exit: ")

    if(choice=="exit"):
        print("thank you please come again and check task ")
        f.close()
        break

    elif(choice=="add"):
        t=input("enter task for TO-DO-LIST")
        now=datetime.datetime.now()
        dt_string=now.strftime("%d/%m/%y %I:%M %p")
        full_task=(f"{t} task added on: {dt_string}")
        task.append(full_task)
        f.write(f"{full_task} \n")
        print("the task was added to TO-DO-LIST")
        
    elif(choice=="view"):
        for index, t in enumerate(task):
            print(index,t)

    elif(choice=="remove"):
        index=int(input("enter a task number:"))
        if index<len(task):
            task.pop(index)
            f_update=open("MY-TO-DO-LIST.txt","w")
            for t in task:
                f_update.write(f"{t}\n")
            f_update.close()
            print("the task was removed and updated")
                
    elif(choice=="view file"):
        f_read=open("MY-TO-DO-LIST.txt","r")
        content=f_read.read()
        print(content)
        f_read.close()

    else:
        print("choose correct option")
        
