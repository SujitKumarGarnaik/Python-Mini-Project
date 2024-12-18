def SingleTonclass(arg):
    l=[]
    def inner():
        if len(l)==0:
            obj=arg()
            l.append(obj)
        return l[0]
    return inner

@SingleTonclass
class movie1():
    def __init__(self):
        self.name='Salar The Case Fire'
        self.maximum_ticket=259
    def Booking(self):
        print(f'The movie name is {self.name}')
        print(f'Available Ticket For the {self.name} is {self.maximum_ticket}')
        require_ticket=int(input('How Many Ticket Do You Want!!'))
        if require_ticket<=self.maximum_ticket:
            print(f'Your Ticket is booked for {self.name}')
            self.maximum_ticket-=require_ticket
        else:
            print('Ticket is not avilable write now')

@SingleTonclass
class movie2():
    def __init__(self):
        self.name='Animal'
        self.maximum_ticket=339
    def Booking(self):
        print(f'The movie name is {self.name}')
        print(f'Available Ticket For the {self.name} is {self.maximum_ticket}')
        require_ticket=int(input('How Many Ticket Do You Want!!'))
        if require_ticket<=self.maximum_ticket:
            print(f'Your Ticket is booked for {self.name}')
            self.maximum_ticket-=require_ticket
        else:
            print('Ticket is not avilable write now')

@SingleTonclass
class movie3():
    def __init__(self):
        self.name='Leo'
        self.maximum_ticket=339
    def Booking(self):
        print(f'The movie name is {self.name}')
        print(f'Available Ticket For the {self.name} is {self.maximum_ticket}')
        require_ticket=int(input('How Many Ticket Do You Want!!'))
        if require_ticket<=self.maximum_ticket:
            print(f'Your Ticket is booked for {self.name}')
            self.maximum_ticket-=require_ticket
        else:
            print('Ticket is not avilable write now')

def bookmyshow():
    display_movies()
    option=int(input('Enter the Movie Option From the section:'))
    if option==1:
        user=movie1()
        user.Booking()
    elif option==2:
        user=movie2()
        user.Booking()
    elif option==3:
        user=movie3()
        user.Booking()
    else:
        print(f'The Movie Is not avilable!!')

def paytm():
    display_movies()
    option=int(input('Enter the Movie Option From the section:'))
    if option==1:
        user=movie1()
        user.Booking()
    elif option==2:
        user=movie2()
        user.Booking()
    elif option==3:
        user=movie3()
        user.Booking()
    else:
        print(f'The Movie Is not avilable!!')

def display_movies():
    print("Available Movies:")
    print("1) Salar The Case Fire - Action, Rating: 8.5/10")
    print("2) Animal - Drama, Rating: 9.0/10")
    print("3) Leo - Thriller, Rating: 8.8/10")

print('Welecome to the Innoviate Movieplex')

bookmyshow()
print('*****************')
paytm()
print('*****************')
bookmyshow()
print('*****************')
bookmyshow()
print('*****************')
paytm()