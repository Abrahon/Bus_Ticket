# bus ticket booking system
# Admin 
# Add new bus
# Check available bus
# can check bus

# user 
# check available bus
# can check bus info
# can reserve seat


class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password



class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to):
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.from_des=from_des
        self.to=to
        self.departure=departure
        self.seat=["Empty" for i in range(20)]

# b=Bus(2,"Rahim","12PM","12:30PM","Dhaka","Chittagong")
# print(vars(b))

class Nabil:
    total_bus=5
    total_bus_list=[]

    def add_bus(self):
        bus_no=int(input("Enter Bus No : "))

        flag = 1
        for w in self.total_bus_list:
            if bus_no==w['coach']:
                print("Bus Already Added")
                flag=0
                break
            
        if flag:
            bus_driver=input("enter bus driver name:")
            bus_arrival = input("Enter Bus arrival Time:")
            bus_departure=input("enter Bus Departure Time : ")
            bus_from = input("enter Bus Start From: ")
            bus_to = input("enter Bus Destination : ")
            self.new_bus = Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("\bus added successfully")
        

# company = Nabil()
# company.add_bus()

class Counter(Nabil):
    user_list = []
    
    def reservation(self):
        bus_no=int(input("Enter Bus No : "))
        
        for w in self.total_bus_list:
            if bus_no==['coach']:
                
                passenger=input("Enter your Name : ")
                seat_no=int(input("Enter seat No: "))
                
                if seat_no>40:
                    print("No Seats Are Available!!")
                elif w['seat'][seat_no-1] !="Empty":
                    print("Seat Already Booked")
                else:
                    w['seat'][seat_no-1] = passenger
                    
            else:
                print("No bus available")
        
#         for bus in self.total_bus_list:
#             print(bus['seat']) 

    def show_ticket(self):
        bus_no=int(input("Enter Bus Number : "))
        
        for w in self.total_bus_list:
            if bus_no==w['coach']:
                print('*'*50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number : {bus_no}\t\t\t Driver  : {w['driver']}")
                print(f"Arrival : {w['arrival']}\t\t\t Departure Time : {w['departure']}\n From: \t{w['from_des']}\t\t\t To: \t{w['to']}")
                print()
                
                a=1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a+=1
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a+=1
                    print()
                print('*'*50)
                
    def get_users(self):
        return self.user_list
               
    def create_account(self):
        name = input("Enter your Username:")
        password = input("Enter Your Password:")
        self.new_user=User(name,password)
        self.user_list.append(vars(self.new_user))
        
    def available_buses(self):
        if len(self.total_bus_list)==0:
            print("No Buses available\n")
        else:
            print('*'*50)
            for bus in self.total_bus_list:
                print()
                print(f"{''*10}{'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                print(f"Bus Number : {bus['coach']} \t Driver : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t Departure Time : {bus['departure']} \n From: \t{bus['from_des']} \t\t To: \t{bus['to']}")
            print('*'*50)



while True:
    company=Nabil()
    b=Counter()
    print("1. Create an account\n2. Login to your account \n3.EXIT")

    user_input=int(input("Enter Your Choice : "))

    if user_input==3:
        break
    elif user_input==1:
        b.create_account()
    elif user_input==2:
        name=input("Enter Your Username : ")
        password=input("Enter Your Password: ")

        flag=0
        isAdmin=False

        if name=="admin" and password=="123":
            isAdmin=True
        if isAdmin==False:
            for user in b.get_users():
                if user['username']==name and user['password']==password:
                    flag=1
                    break
            if flag:
                while True:
                    print(f"\n{' '*10}Welcome to BUS TICKET BOOKING SYSTEM")
                    print("1.Available Buses\n2. Show Bus Info \n3.Reservation\n4.EXIT")
                    a=int(input("Enter Your Choice : "))
                    if a==4:
                        break
                    elif a==1:
                        b.available_buses()
                    elif a==2:
                        b.show_ticket()
                    elif a==3:
                        b.reservation()
            else:
                print("No Username Found ")
        else:    
            while True:
                print(f"\n{' '*10}Hello ADMIN Welcome to BUS TICKET BOOKING SYSTEM")
                print("1.Add Bus\n2.Available Buses \n3.Show Bus Info \n4.EXIT")
                a=int(input("Enter Your Choice : "))
                if a==4:
                    break
                elif a==1:
                    b.add_bus()
                elif a==2:
                    b.available_buses()
                elif a==3:
                    b.show_ticket()
   
        
                
            
            
                    
               
                
                
                
                
            
       
            
          
            
                            
                
            
                
            
                       
# company = Nabil()
# company.add_bus()

# c=Counter()
# c.reservation()

# 1.create an account
# 2.login to your account
# 3.exit



# User
# 1.Bus info
# 2.Reservetion

# admin
# 1.add Bus
# 2.Available Buses
# 3.Can check bus info
# 4.Exit
        
        
        
        

        
        
        