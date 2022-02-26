# Programming-1_Summative-Assignment_Week-13_2021
## Project Title: Water Supply Management System.


Proposed by:


   ##GHEA SANDRINE MAWEN and 
   ##MAIKEM VICTORINE



#Project Description 


In this project, we are looking forward to creating a water management system that will help manage and reduce the wastage of water which is a vital, yet limited resource in areas of the world.
The system will implement a number of functionalities, including:
Water censoring system that will check the amount of water present in the tank, and turn on the water pump(supply water) when the water level is low, and turn off the pump when the water level is high.
An automatic temperature regulator, where the system can automatically turn the water heater on and off depending on a set temperature.
Water limit regulator that will regulate the water usage in a building if it exceeds the limit the system will automatically turn OFF the water supply. But however, the user will be notified when they used up to 80%.
Offer the possibility for a user to check the quantity of water that is still available to them.
Offer a management platform where water dispensing and managing companies, as well as landlords, can manage the distribution of water supply among their clients or tenants.
A system for authorities and for the users to keep a tab on the coming bills.

#PSEUDO CODE:
The class user is the parent class that represents the humans that interact with the system. It includes that characteristic lik user_name, password and has a common method called the login.


Class Admin(User):

This class is a child class of the user class which represents the general manager of the system. The admin has specific methods and actions they can carry out.
 Initialize the variable called water supply and increment it to help us track the number of times the pump has been open,so that we know when the user reaches the maximum limit number of times.  

#PROCEDURE water_pump(amount of water,min water limit,water supply):



#Class Client(User):
The client class represents a client who uses the system and manages the admin.

    PROCEDURE__init__(Amount of water=1, set_temperature=30,  Max_water_limit=5, Min_water_limit=0, default_costs=1000, Water_supply = 0,   Access = True)

Here we are checking to see if the customers preferred temperature is equal to our normal set temperature. So we first ask the users to input her preferred temperature and we compare it to the one set by the system.

def check_water_limit(self):
   if self.amount_of_water < 5:
       return True
   else:
       return False



The water limit regulator will enable the admin to check the amount of water that a client has used  and then cut the user’s access to water when they reach their maximum water usage.

PROCEDURE Water_limitRegulator(water supply,access):
 IF water_supply == 5:
	Self.access = false
	RETURN self.access
IF water_supply == 4:
print(“80%”)
RETURN self.access

 
PROCEDURE temperature_regulator():

Users_water_temp = INPUT(Take input from the user)
set_temperature = Users_water_temp:
Display (‘New temp is ’ + set_temperature )

Here this method allows the user and admin to monitor the amount of water left in the system. We assume that whenever we pump water to a user tank then, it's equal to 20% of the total water available for use for the user in a month.

PROCEDURE Check_waterLeft():

Display (f“Water used is {water_supply} and water left is {max_water_limit - water_supply}”)


Here this method will help the user to check his water bill depending on the amount of water they have used so far. WE assume that, 1 pump is 1000Rwf




PROCEDURE Calculate_bill():

One_pump = 1000Rwf
Bill = default cost + water_used*One_pump
RETURN Bill

Test file:
https://docs.google.com/spreadsheets/d/1UU0bT96DNeILOLP0UQ5tLYpYj6KcaEzlHRZ3lWI7fFI/edit?usp=sharing

## Preinstallation Info
#Pycharm
#initialise git
#Install python3
#Install and import random and system libraries















