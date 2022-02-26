
from Class_admin import Admin
from Class_client import Client
import sys
import random

print('you are welcome to S&V water management system')

water_supply = 0

#Adding a client to the system
def create_account():
    name = input('Enter your name')
    id = random.randint(111, 999)
    email = input('Enter your email address ')
    # checking if the password enter is 4 integers
    while True:
        try:
            password = int(input("Enter your password, 4 characters long: "))
        except ValueError:
            print("Enter an interger.")
            continue
        else:
            if len(str(password)) != 4:
                continue
            else:
                break
    # Adding the admin we have created to admin file.
    toWrite = f"{id} {name} {email} {password} \n"
    # opening the admin file
    f = open("admins.txt", "a+")
    f.write(toWrite)
    # closing the admin file
    f.close()
    print(f'Hello to you {name}, id: {id}')

# Adding a client to the system
def add_client():
    name = input('Enter your name')
    id = random.randint(1001, 9999)
    email = input('Enter your email address ')
    while True:
        try:
            password = int(input("Enter your password, 4 characters long: "))
        except ValueError:
            print("Enter an interger.")
            continue
        else:
            if len(str(password)) != 4:
                continue
            else:
                break
    # Adding the client we have created to client file.
    toWrite = f"{id} {name} {email} {password} 1 1 30 5 1000 0 0 \n"
    # opening the file in read mode
    f = open("clients.txt", "r")
    # reading the information the client file line after line
    allLines = f.readlines()
    f.close()
    # Appending the all client information to the client file
    allLines.append(toWrite)

    #opening the client file on write mode
    f = open("clients.txt", "w")
    f.writelines(allLines)
    f.close()
    print(f'you have added a client with name {name}, and id id: {id}')


# Use the length of the id number to determine
# who is loging in that is the admin or the client.
def active_user(id):
    current_user = False
    if len(str(id)) == 3:
        current_user = True
    else:
        current_user = False
    return current_user




while True:
    register = input('''Are you registered as
     1. admin
     2. Client ''')

    if register == '1':
        action = input('''Would you want to
            a. Create an Account
            b. Login to your Account ''')
        if action == 'a':
            create_account()
        elif action == 'b':
            # read the saved admin
            adminLogin = open("admins.txt", "r")
            while True:
                try:
                    id = int(input("Please enter your id number "))
                except ValueError:
                    print(" Id is  an integer.")
                    continue
                else:
                    break
            if len(str(id)) != 3:
                print("No admin with this credentials")
                sys.exit()
            # search for line starting with id
            foundAcc = False
            adminInfo = None
            password = input("Please enter your password ")
            logedin_account = None
            # searching for id and password in the file and comparing it with the one entered by the admin.
            for admin in adminLogin:
                # splitting the information in the file in order to access the password and id
                if admin.split(' ', 1)[0] == str(id) and admin.split(' ')[3] == password:
                    foundAcc = True
                    adminInfo = admin
                # pass the information into the logedin account so we can keep track of who is logging into the system
                    logedin_account = Admin(admin.split(' ')[0], admin.split(' ')[1], admin.split(' ')[2],
                                            admin.split(' ')[3])
            # Closing the admin file.
            adminLogin.close()
            if foundAcc is False:
                print("not found or invalid credentials")
                sys.exit()

            print("Admin login Successful")

            # Display admin menu
            while True:
                admin_menu = input('''Would you want to
                            a. Add a Client
                            b. Supply water to a Client
                            c. Control Access to water
                            ''')
                if admin_menu == 'a':
                    add_client()
                elif admin_menu == 'b':
                    # open the client file in read mode so as to extract some information from it
                    clientSearch = open("clients.txt", "r")
                    client_id = input("Please enter client ID")
                    found_account = False
                    # counting the indexing in the file
                    counter = 0
                    alllines = clientSearch.readlines()
                    # close the client file
                    clientSearch.close()
                    # searching for id and password in the file and comparing it with the one entered by the admin.
                    for client in alllines:
                        if client.split(' ', 1)[0] == str(client_id):
                            found_account = True
                            clientInfo = client
                            # pass the information into the client account so we can keep track of who the admin is pumping water to.
                            client_account = Client(client.split(' ')[0], client.split(' ')[1], client.split(' ')[2],
                                                    client.split(' ')[3])
                            client_account.water_supply = int(client.split(' ')[-3])

                            # checking if the client has not exceed his/her total number of water supply.
                            status = client_account.check_water_limit()
                            if status is False:
                                print('Sorry this client is out of water supply')
                                break
                            client_account.water_supply += 1
                            # Coping the line we want to edit from the client file after the counter has return the index.
                            alllines[counter] = f"{client_account.id} {client_account.name} {client_account.email} {client_account.password} {client_account.access} {client_account.amount_of_water} {client_account.set_temperature} {client_account.max_water_limit} {client_account.default_cost} {client_account.water_supply} {client_account.min_water_limit} \n"
                            # open the file in write mode and update the new information for water supply to teh particular client we have supplied water to.
                            updateFile = open("clients.txt", "w")
                            updateFile.writelines(alllines)
                            updateFile.close()
                            print(f'you have pump water to {client_account.id}, {client_account.water_supply} time(s)')
                        counter += 1
                    if found_account is False:
                        print('Account not found')

                elif admin_menu == 'c':
                    client_id = input("Please enter client ID")
                    found_account = False
                    counter = 0
                    #open the file in read mode to read the information client file.
                    f = open("clients.txt", "r")
                    alllines = f.readlines()
                    f.close()
                    for i in alllines:
                        # checking to see if the id we get from the file is equal to the client id the admin inputs.
                        if i.split(' ', 1)[0] == str(client_id):
                            found_account = True
                            # pass the information into the client account so we can keep track of who the admin is pumping water to.
                            client_account = Client(i.split(' ')[0], i.split(' ')[1], i.split(' ')[2],
                                                    i.split(' ')[3])
                            #comparing the water supply, maximum limit and min water limit to the one stored in the file
                            client_account.water_supply = int(i.split(' ')[-3])
                            client_account.max_water_limit = int(i.split(' ')[7])
                            client_account.min_water_limit = int(i.split(' ')[-2])
                            # checking if the client has not exceed his/her total number of water supply.
                            status = client_account.water_limit_regulator()
                            if status is False:
                                print('This client is out of water supply. Access updated to False!')
                                # Coping the line we want to edit from the client file after the counter has return the indexes.
                                alllines[counter] = f"{client_account.id} {client_account.name} {client_account.email} {client_account.password} {client_account.access} {client_account.amount_of_water} {client_account.set_temperature} {client_account.max_water_limit} {client_account.default_cost} {client_account.water_supply} {client_account.min_water_limit} \n"
                            elif status == 4:
                                print('Warning this client has used 80`%` of their water supply')
                            else:
                                print('This client still has access to water')
                                # Open the file in write mode and update the information
                            f = open("clients.txt", "w")
                            f.writelines(alllines)
                            f.close()
                        counter += 1
                    if found_account is False:
                        print('Account not found')
                else:
                    print('Invalid input')
                    continue
                # Checking to see if the user will like to perform another action.
                user_proceed = input('Would you like to continue? yes or no ')
                if user_proceed == 'yes' or 'y' or 'Y' or 'yea':
                    continue
                elif user_proceed == 'no' or 'n' or 'N':
                    break
                else:
                    print("Invalid input")
    elif register == '2':
        while True:
            try:
                id = int(input("Please enter your id number "))
            except ValueError:
                print(" Id is  an integer.")
                continue
            else:
                break
        if len(str(id)) != 4:
            print("No client with this credentials")
            sys.exit()
        # search for line starting with id
        foundAcc = False
        password = input("Please enter your password ")
        client_account = None
        counter = 0
        f = open("clients.txt", "r")
        alllines = f.readlines()
        f.close()
        # checking to see if the information we get from the file is equal to the client infromation the currently login.
        for line in alllines:
            if line.split(' ')[0] == str(id) and line.split(' ')[3] == password:
                foundAcc = True
                client_account = Client(line.split(' ')[0], line.split(' ')[1], line.split(' ')[2], line.split(' ')[3])
                client_account.water_supply = int(line.split(' ')[-3])
                client_account.max_water_limit = int(line.split(' ')[7])
                client_account.min_water_limit = int(line.split(' ')[-2])
                client_account.access = bool(line.split(' ')[4])
                client_account.set_temperature = int(line.split(' ')[6])
                client_account.default_cost = int(line.split(' ')[8])
                client_account.amount_of_water = int(line.split(' ')[5])
                break
            counter += 1

        if foundAcc is False:
            print("not found or invalid credentials")
            sys.exit()

        while True:
            # Client Menu
            client_menu = input('''Would you want to
                                     a. Regulate your temperature level
                                     b. Check Amount of water left
                                     c. Check bills
                                     ''')
            if client_menu == 'a':
                client_account.temperature_regulator()
                f = open("clients.txt", "w")
                # Coping the line we want to edit from the client file after the counter has return their indexes.
                alllines[counter] = f"{client_account.id} {client_account.name} {client_account.email} {client_account.password} {client_account.access} {client_account.amount_of_water} {client_account.set_temperature} {client_account.max_water_limit} {client_account.default_cost} {client_account.water_supply} {client_account.min_water_limit} \n"
                f.writelines(alllines)
                f.close()
            elif client_menu == 'b':
                client_account.check_water_left()

            elif client_menu == 'c':
                client_account.calculate_bill()

            else:
                print('Invalid input')
            #checking to see if the client will like to perform another action
            action = input('Would you like to continue? yes/no')
            if action == 'yes' or 'y' or 'Y' or 'yeah':
                continue
            elif action == 'no' or 'n'or'N' or 'nope' :
                break
            else:
                print('invalid input')
                break


