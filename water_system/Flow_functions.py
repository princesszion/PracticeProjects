# Importing the classes we need.
from Class_admin import Admin
from Class_client import Client
import random
print('you are welcome to S&V water management system')
Admin_accounts = []
Client_accounts = []
water_supply = 0

# Adding an Admin to the system
def create_account():
    name = input('Enter your name')
    id = random.randint(111 , 999)
    email = input('Enter your email address ')
    # checking if the password enter is 4 integers
    while True:
        try:
            password= int(input("Enter your password, 4 characters long: "))
        except ValueError:
            print("Enter an integer.")
            continue
        else:
           if len(str(password)) != 4:
               continue
           else:
            break
    admin1 = Admin(id,name,email,str(password))
    Admin_accounts.append(admin1)
    print(f'Hello to you {name}, id: {id}')
    return len(str(admin1.password))

# Adding a client to the system
def add_client():
    name = input('Enter your name')
    id = random.randint(1001, 9999)
    email = input('Enter your email address ')
    while True:
        try:
            password= int(input("Enter your password, 4 characters long: "))
        except ValueError:
            print("Enter an interger.")
            continue
        else:
           if len(str(password)) != 4:
               continue
           else:
            break
    client1 = Client(id,name,email,str(password))
    Client_accounts.append(client1)
    new = Client_accounts
    for account in new:
        print(f'you have added a client with name {name}, and id: {id}')


#Use the length of the id number to determine
#who is loging (admin or the client)
def active_user(id):
    current_user = False
    if len(str(id)) == 3:
        current_user = True
    else:
        current_user = False
    return current_user


#login function to permit user to login into the system

def login(id, password):
    # this returns  the  truth value of the active user method.
    present_user = active_user(id)
    present_users = []
    if present_user:
        present_users = Admin_accounts
    else:
        present_users = Client_accounts
    for account in present_users:
        if account.id == id and account.password == password:
            return account
        else:
            return None