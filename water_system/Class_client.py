#Create class client.
class Client():
    def __init__(self, id, name, email, password, access = True, amount_of_water=1, set_temperature=30, max_water_limit=5,
                 default_cost=1000, water_supply = 0, min_water_limit = 0):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.amount_of_water = amount_of_water
        self.water_supply = water_supply
        self.set_temperature = set_temperature
        self.max_water_limit = max_water_limit
        self.default_cost = default_cost
        self.access = access
        self.min_water_limit = min_water_limit

        # Checks amount of water a client has and so far as a client has not used up their maximum limit.
        # We store the truth value, that will help us in pumping water to the client.
    def check_water_limit(self):
        if self.amount_of_water < 5 and self.water_supply < 5:
            return True
        else:
            return False
        # Will enable the admin to check the amount of water that a client has used
        # And then cut the user’s access to water when they reach their maximum water usage
    def water_limit_regulator(self):
        if self.water_supply == 5:
            self.access = False
            return self.access
        elif self.water_supply == 4:
            return self.water_supply
        else:
            return self.access

        # To assign client preferred temperature.
    def temperature_regulator(self):
        while True:
            try:
                client_water_temperature = int(input("Please enter your preferred temperature"))
            except ValueError:
                print("Enter an integer.")
                continue
            self.set_temperature = client_water_temperature
            print(f"Your water temperature has been set to {self.set_temperature} degrees ")
            return self.set_temperature

       # For a client to check the amount of water the have left for a month.
    def check_water_left(self):
        water_left = self.max_water_limit - self.water_supply
        print(f"Water used is {self.water_supply} and water left is {water_left}")
        return water_left

       # To check the bill of a client, we assumed one pump(Whenever water is supplied to a client) is 1000
    def calculate_bill(self):
        one_pump = 1000
        bill = self.default_cost + (self.water_supply * one_pump)
        print(f'Your bill is {bill}')
        return bill





