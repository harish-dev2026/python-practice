def create_bill():
    print("sathya car care online platform")
    m_service=[]
    m_fault=[]
    no_of_vehicle=[]
    rate_card={"oil change":800,
               "car_full service":5000
               }

    name=input("enter customer name: ")
    f_price=0
    with open("sathya car care.txt","a") as bill_m:
        
    
      import datetime

      while True:
          
          choice=input("add_car or car_fault or finish or view car or remove car or view_rate_card or view bill or exit :")

          if(choice=="add_car"):
              vehicle_name=input("enter your vechicle name and model: ")
              car_no=input("enter your car registration  number: ")
              v_car_no=(f"{vehicle_name}-{car_no}")
              no_of_vehicle.append(v_car_no)
        
          if(choice=="car_fault"):
              car_fault=input("enter customer car trouble: ")
              price=int(input("enter the cost including labour fees: "))
              o_fault=(f"{car_fault}: {price} ")
              m_fault.append(o_fault)
            
            
              f_price=f_price+price

          elif(choice=="view_rate_card"):
               
               service_item=input("what service or item you need: ")
               if service_item in rate_card:
                   f_service=rate_card[service_item]
                   o_service=(f"{service_item}: {f_service}")
                   m_service.append(o_service)
                   f_price=f_price+f_service
                   print(o_service)
                    
                   print("thankyou for buying these service")
               
               else:
                   print("sorry sir currentlty not have these service or item")

                   add_ratecard=input("do you want add new service on rate card:")
                   if(add_ratecard=="yes"):
                       p_service=int(input("enter price for new service: "))
                       rate_card[service_item]=p_service
                       print(f"the {service_item}: {p_service} service added to rate card")

                   else:
                       print("thank you sir")

          elif(choice=="finish"):

               bill_content=(f"name- {name}\ncars- {no_of_vehicle}\nrepaired service- {m_fault}\nbuying service- {m_service}\ntotal price- {f_price}\n")
               now=datetime.datetime.now()
               dt_string=now.strftime("%d/%m/%y %I:%m %p")
               full_content=(f"{bill_content}  {dt_string}\n")
               print("------sathya car care online platform---------")
               print(full_content)
               bill_m.write(full_content)

          elif(choice=="view car"):
               for index, c in enumerate(no_of_vehicle):
                   print(index,c)

          elif(choice=="remove car"):
               index=int(input("enter car slot no: "))
               if(index<len(no_of_vehicle)):
                   no_of_vehicle.pop(index)
                   print(f"car was removed in {index} slot")
            
          elif(choice=="view bill"):
               print("------sathya car care online platform---------")
               bill_f=open("sathya car care.txt","r")
               content=bill_f.read()
               print(content)
               bill_f.close()

          elif(choice=="exit"):
               print("thankyou for visiting sathya car care online platform")
               bill_m.close()
               break
            

            

            
create_bill()
