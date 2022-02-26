# Importing the files and classes we will used
import Flow_functions
import sys

# Allowing the user to chose from a menu.
while True:
    register = input('''Are you registered as
     1. admin 
     2. Client ''')

    # The user is a Admin we display a menu to them
    if register == '1':
            action = input('''Would you want to
             a. Create an Account 
             b. Login to your Account ''')
            if action == 'a':
                # call the create account function from Flow_function file
                Flow_functions.create_account()

            elif action == 'b':
                # check to see if the user is already registered in the system
                while True:
                    try:
                        id = int(input("Please enter your id number "))
                    except ValueError:
                        print("Your id is an integer, Enter an integer.")
                        continue
                    else:
                        break
                password = input("Please enter your password ")
                # Noting that length of the id for admin is 3 we need to check,
                # if the present user logging in has an id of length 3
                if len(str(id)) != 3:
                    print("No admin with this credentials")
                    sys.exit()
                logedin_account = Flow_functions.login(id, password)
                if logedin_account is None:
                    print("Invalid Credentials")
                    exit()
                print("Admin login Succesful")
                # Display admin menu
                while True:
                    admin_menu = input('''Would you want to
                             a. Add a Client
                             b. Supply water to a Client
                             c. Control Access to water
                             ''')
                    if admin_menu == 'a':
                        Flow_functions.add_client()
                    elif admin_menu == 'b':
                        # checking to see if the client the admin wants to supply water to is found in the system
                        client_id = input("Please enter client ID ")
                        new = Flow_functions.Client_accounts
                        found_account = False
                        for account in new:
                            if account.id == int(client_id):
                                print('client found')
                                # checking if the client has not exceed his/her total number of water supply.
                                status = account.check_water_limit()
                                if status is False:
                                    print('Sorry we can not pump water to this client')
                                    break
                                # Increment the water supply if the client we have pump water to.
                                account.water_supply += 1
                                print(f'you have pump water to {account.id}, {account.water_supply} time(s)')
                                found_account = True
                                # Updating the value of the amount of water of a client we just supplied water to.
                                account.amount_of_water = account.water_supply
                            if found_account is False:
                                print('Account not found')

                    elif admin_menu == 'c':
                        # checking to see if the client the admin wants their water access value is found in the system
                        client_id = input("Please enter client ID ")
                        new = Flow_functions.Client_accounts
                        found_account = False
                        for account in new:
                            if account.id == int(client_id):
                               status = account.water_limit_regulator()
                               if status is False:
                                   print('This client is out of water supply')
                               elif status == 4:
                                   print('Warning this client has used uo 80% of their water supply')
                               else:
                                   print('this client still has access to water')
                    else:
                        print('Invalid input')
                        continue
                    # Checking to see if the logged in admin will like to perform another action.
                    user_proceed = input('Would you like to continue? yes or no ')
                    if action == 'yes' or 'Y' or 'y':
                        continue
                    elif action == 'no' or 'N' or 'n':
                        break
                    else:
                        print('invalid input')
                        break
    elif register == '2':
            # Logging in the client into the system
            while True:
                try:
                    id = int(input("Please enter your id number "))
                except ValueError:
                    print("Your id is an integer. Enter an integer.")
                    continue
                else:
                    break
            password = input("Please enter your password ")
            # Checking the length of password entered as all client needs to have passwords of length 4
            if len(str(id)) != 4:
                print("No client with this credentials")
                sys.exit()
            # Checking if the current user trying to login exists in the system
            logedin_account = Flow_functions.login(id, password)
            if logedin_account is None:
                print("Invalid Credentials")
                exit()
            print("Client login Succesful")
            while True:
                #Client Menu
                client_menu = input('''Would you want to
                                         a. Regulate your temperature level
                                         b. Check Amount of water left
                                         c. Check bills
                                         ''')
                if client_menu == 'a':
                    # Call the temperature regulator function from the class class
                    logedin_account.temperature_regulator()
                elif client_menu == 'b':
                    # checking the water left for the login client using check water left function from the class class
                    logedin_account.check_water_left()

                elif client_menu == 'c':
                    # Calculating the bill of the login client using the calculate bill function from the class class
                    logedin_account.calculate_bill()
                else:
                    print('Invalid input')
                # Checking to see if the logged in  client will like to perform another action.
                action = input('Would you like to continue? yes/no ')
                if action == 'yes' or 'Y' or 'y':
                    continue
                elif action == 'no' or 'N' or 'n':
                    break
                else:
                    print('invalid input')
                    break



