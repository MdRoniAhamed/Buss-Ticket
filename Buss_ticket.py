""" Bus Ticket Reservation System """
""" Author: MD Roni Ahamed """
""" Gmail: mdroni0193101@gmail.com """

class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password


class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ['Empty' for i in range(20)]


class PhitronCompany:  # Bus Install for admin
    total_bus = 5
    total_bus_lst = []  # dummy Database

    def install(self):
        bus_no = int(input('Enter Bus NO: '))
        flag = 1
        for bus in self.total_bus_lst:  # checking kono bus already installed na
            if bus_no == bus['coach']:
                print('Bus already installed')
                flag = 0
                break
        if flag:
            bus_driver = input('Enter Bus Driver Name: ')
            bus_arrival = input('Enter Bus Arrival Time: ')
            bus_departure = input('Enter Bus Departure Time: ')
            bus_from = input('Enter Bus Start From: ')
            bus_to = input('Enter Bus Destination To : ')
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival,
                               bus_departure, bus_from, bus_to)
            self.total_bus_lst.append(vars(self.new_bus))
            print('\n Bus installed successfully\n')


class BusCounter(PhitronCompany):
    user_lst = []  # User database
    bus_seat = 20

    def reservation(self):
        bus_no = int(input('Enter Bus NUmber: '))
        flag = 1
        for bus in self.total_bus_lst:
            if bus_no == bus['coach']:
                flag = 0
                passenger = input('Enter your name: ')
                seat_no = int(input('Enter your seat Number : '))
                if seat_no - 1 > self.bus_seat:  # maximum seat checking
                    print('Only 20 seats are available')
                elif bus['seat'][seat_no - 1] != 'Empty':  # not empty kina
                    print('Seat already Booked')
                else:  # oi seat e oi user ke bosiye dicchi
                    bus['seat'][seat_no - 1] = passenger

        if flag:
            print('NO bus number available')

    def showBusInfo(self):  # one bus information
        bus_no = int(input('Enter Bus No : '))
        for bus in self.total_bus_lst:
            if bus['coach'] == bus_no:
                print('*'*50)
                print()
                print(f"{' '*10} {'__'*10} BUS INFO {'__'*10}")
                print(f"Bus Number : {bus_no} \t\t Driver : {bus['driver']}")
                print(
                    f"Arrival : {bus['arrival']} \t\t Departure : {bus['departure']} ")
                print(f"From : {bus['from_des']} \t\t To : {bus['to']} ")
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]} ", end='')
                        a += 1
                    print('\t', end='')
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]} ", end='')
                        a += 1
                    print()

                print('*'*50)

    def get_users(self):
        return self.user_lst

    def create_account(self):
        name = input("Enter your name : ")
        flag = 0
        for user in self.get_users():
            if user.username == name:
                print("Username already exists")
                flag = 1
                break
        if flag == 0:
            password = input('Enter your password : ')
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user))
            print('Account created successfully')

    def available_buses(self):  # All bus information
        if len(self.total_bus_lst) == 0:
            print("No Bus Available")
        else:
            for bus in self.total_bus_lst:
                print('*'*50)
                print()
                print(f"{' '*10} {'__'*10} BUS INFO {bus['coach']} {'__'*10}")
                print(
                    f"Bus Number : {bus['coach']} \t\t Driver : {bus['driver']}")
                print(
                    f"Arrival : {bus['arrival']} \t\t Departure : {bus['departure']} ")
                print(f"From : {bus['from_des']} \t\t To : {bus['to']} ")
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]} ", end='')
                        a += 1
                    print('\t', end='')
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]} ", end='')
                        a += 1
                    print()

                print('*'*50)


if __name__ == '__main__':
    while True:
        counter = BusCounter()
        print("1. Create An Account \n2. Login To your Account \n3. EXIT")
        user_input = int(input("Enter you choice : "))
        if user_input == 3:
            break
        elif user_input == 1:
            counter.create_account()
        elif user_input == 2:
            name = input("Enter your name : ")
            password = input("Enter your password : ")
            isAdmin = False
            flag = 0
            if name == "admin" and password == "123":
                isAdmin = True
            if isAdmin == False:
                for user in counter.get_users():
                    if user['username'] == name and user['password'] == password:
                        flag = 1
                if flag:
                    while True:
                        print(
                            f"\n{' '*10}WELCOME to BUS TICKET BOOKING SYSTEM ")
                        print(
                            "1.Available Buses \n2. Show Bus Info\n3. Reservation\n4.EXIT ")
                        a = int(input("Enter your Choice : "))
                        if a == 4:
                            break
                        elif a == 1:
                            counter.available_buses()
                        elif a == 2:
                            counter.showBusInfo()
                        elif a == 3:
                            counter.reservation()
                    else:
                        print("NO username found")
            else:
                while True:
                    print(
                        "\n{' '*10} HELLO ADMIN WELCOME TO BUS TICKET BOOKING SYSTEM\n ")
                    print(
                        "1. Install Bus\n2.Available Buses\n3. Show Bus Info\n4. EXIT")
                    a = int(input("Enter your Choice : "))
                    if a == 4:
                        break
                    elif a == 1:
                        counter.install()
                    elif a == 2:
                        counter.available_buses()
                    elif a == 3:
                        counter.showBusInfo()

                # 1. create an account -> create_new_account() []
                # 2. login to your account -> authentic User
                #                          -> 1. available_timezones
                #                          -> 2. Reservation
                #                          -> 3. show bus info

                #                          -> Administrator
                #                          ->1. Install Buses
                #                          ->2. See available_buses
                #                          ->3. See total userList
