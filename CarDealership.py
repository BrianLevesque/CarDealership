class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        engine_on = False

    def start_engine(self):
        print("Starting engine...")
        engine_on = True

    def make_noise(self):
        print("Beep beep!")

    def __str__(self):
        return f' {self.make}: with {self.miles} miles and costs {self.price}'


class Truck(Vehicle):
    def __init(self, make, miles, price):
        Vehicle.__init__(self,make,miles,price)
        self.cargo = False

    def load_cargo(self):
        print("Loading the truck bed...")
        self.cargo = True


class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        Vehicle.__init__(self, make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print("Vroom vroom!")

    def __str__(self):
        return f' {self.make}: with {self.miles} miles and a top speed of {self.top_speed} costs {self.price}'

# creating motorcycle objects and adding to the bike list

mc1 = Motorcycle("Harley Davidson", 5000, 15000,160)
mc2 = Motorcycle("BMW", 6000, 12000,190)
mc3 = Motorcycle("Indian", 3000, 20000,150)

bikes = [mc1, mc2, mc3]

# creating the truck objects and adding them to the truck list
tk1 = Truck("Ram", 50000,65000)
tk2 = Truck("Chevy", 100000,25000)
tk3 = Truck("Ford", 25000,75000)
trucks = [tk1, tk2, tk3]

# creating an empty vehicle to compare list

vehicles_to_compare = []


print("Welcome to GC Bikes & Trucks!")
compare = True
view = True
while view:
    BorT = input("Would you like to view bikes or trucks? (b or t) ")
    if BorT == "b":
        # prints out all bikes in bike list
        print("1.", bikes[0])
        print("2.", bikes[1])
        print("3.", bikes[2])
        com = input("Would you like to compare one of these vehicle today? (y or n)")
        if com == "y":
            # adds bike to vehicles_to_compare list  and prints out it is added while taking out of the bike list
            vehicle1 = int(input("Which vehicle would you like to compare? (please list number)")) - 1
            vehicles_to_compare.append(bikes[vehicle1])
            print(f"{bikes[vehicle1].make} added!")
            bikes.pop(vehicle1)
            show_compare = input("Would you like to compare vehicles now?(y/n) ")
            if show_compare == "y":
                for i in vehicles_to_compare:
                    print(i)
                    i.make_noise()
                # takes user out of view loop
                view = False

        elif com != "n":
            print("please enter valid input")

        # takes user out of view loop
    elif BorT == "t":
        # prints out all trucks in truck list
        print("1.", trucks[0])
        print("2.", trucks[1])
        print("3.", trucks[2])

        # checks if user wants to compare vehicles
        com = input("Would you like to compare one of these vehicle today? (y or n)")
        if com == "y":
            vehicle1 = int(input("Which vehicle would you like to compare? (please list number)")) - 1
            # adds truck to vehicles_to_compare list  and prints out it is added while taking out of the trucks list
            vehicles_to_compare.append(trucks[vehicle1])
            print(f"{trucks[vehicle1].make} added!")
            trucks.pop(vehicle1)
            show_compare = input("Would you like to compare vehicles now?(y/n) ")
            if show_compare == "y":
                # prints out vehicles to compare
                for i in vehicles_to_compare:
                    print(i)
                    i.make_noise()
                # takes user out of view loop
                view = False

            elif com == "n":
                show_compare = input("Would you like to compare vehicles now?(y/n) ")
                if show_compare == "y":
                    # takes user out of view loop
                    # prints out vehicles to compare
                    for i in vehicles_to_compare:
                        print(i)
                        i.make_noise()
                    view = False
            else:
                print("please enter valid input")

    else:
        # prints out when user does not enter valid response to view trucks or bikes
        print("please enter valid response")










