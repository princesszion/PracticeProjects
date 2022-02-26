# Omondi is starting a new business, a car renting business.
#
# Omondi starts with five different Cars.
#
# Each car has a model, a year when it was released, a year when Omondi acquired it, the money made from that car, the car's plate number, and the number of times that it has been in business. (It has been rented).
#
# As Omondi is looking into expansion, he wants to be able to rent the cars, add new cars to his collection, remove the cars from his collection, count the number that each car has been rented out, and the money made from each car.
#
# Please help Omondi.
#Dictionary containing the 5 cars that Omondi has to start with

mycars = {
  "car1" : {
    "model" : "Toyota",
    "year_released" : 2004,
    "year_released": 2008,
    "money_made": 100,
    "plate_number":2003,
    "number_times_rented":0,
  },
  "car2" : {
    "model" : "Mercedez",
    "year_released" : 2004,
    "year_released": 2008,
    "money_made": 100,
    "plate_number":2003,
    "number_times_rented":0,
  },
  "car3" : {
    "model" : "Rav4",
    "year_released" : 2004,
    "year_released": 2008,
    "money_made": 100,
    "plate_number":2003,
    "number_times_rented":0,
  }
}

def print_cars():
    #prints the lists of cars in an orderly manner.
    for key, value in mycars.items():
        print(key, ' : ', value)
def rent_cars():
    def cars():
            print_cars()
            y = input("Which car model would you like to rent?")
            for x in mycars:
                while x == y:
                    rented_cars = []
                    if x not in rented_cars:
                        rented_cars.append(mycars[x]["number_times_rented"])
                        mycars[x]["number_times_rented"] += 1
                    for a in rented_cars:
                        print(x,rented_cars)
                    q = input("Would you like to rent another car?  y for yes or n for no")
                    if q == "y":
                        cars()
                    else:
                        print("Thanks")
                        exit()
    cars()


def money_made():
    print_cars()
    car = input("Which car do you want yo check? ")
    num_rented = int(input("How many times was the car rented?"))
    for x in mycars:
        if x == car:
            money = mycars[x]["money_made"] * num_rented
            print(money)

def rent_cars():
    #A  function that prints the available cars,
    #Takes the input from the user on which car to rent,and adds
    #the car to the list of rented cars.

    print_cars()
    rented_cars = []
    q = input("Which car do you want to rent?")
    for x in mycars:
        if q == x and x not in rented_cars:
           rented_cars.append(q)
    print("Car rented",rented_cars)


def add_cars():
    #A function defined to add a new car to the collection
    #by taking the details from user,and adding it to the current collection
    num = input("Input the car number eg car8")
    mod = input("What is the car model?")
    dr = input("When  car released (just the year)")
    da = input("When did you acquire the car (just the year)")
    cost = input("What is the price of the car?")
    pn = input("What is the plate numner?")
    tr = input("How may times has been rented?")
    newcars = {}
    number = num
    model = mod
    year_released = dr
    year_aquired = da
    money_made = cost
    plate_number = pn
    number_times_rented = tr
    #use the eval function to add the newly created car as a child dictionay
    #to the parent dictionary,my cars.
    for variable in ["model","year_released","year_aquired"," money_made","plate_number","number_times_rented"]:
        newcars[variable] = eval(variable)
        mycars[num] = newcars
        print_cars()


def remove_cars():
    #funtion to remove a car from the list of cars
    #prints all cars and request for which one to remove
    print_cars()
    r = input("which car do you want to remove?")
    for x in mycars:
        if r == x:
            del mycars[x]
            print_cars()
            exit()
print("1-Add,2-rent,3-remove,4-check money")
req = input("What do you want to do?")
if req == "1":
    add_cars()
elif req == "2":
    rent_cars()
elif req == "4":
    money_made()
else:
 remove_cars()



