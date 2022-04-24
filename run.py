#!/usr/bin/env python3.9

from user import User
def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    contact.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    contact.delete_contact()

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def login_user(username, password):
    """
    A function that verifies a user login
    """
    check_user = User.verify_login(username, password)
    return check_user

def create_credentials(account_name, account_password):
    """
    A function that creates a new credential
    """
    new_cred = Credentials(account_name, account_password)
    return new_cred   

def save_credentials(cred): 
    """
    A function that saves a credential
    """
    cred.save_credentials()
    
def delete_credentials(cred):
    """
    A function that deletes a credential
    """
    cred.delete_credentials()
    
def get_credentials(account_name):
    """
    A function that finds and returns a credential
    """
    return Credentials.get_credentials(account_name)

def display_credentials():
    """
    A function that displays available credentials
    """
    return Credentials.display_credentials()   

def main():
    print("Hello Welcome to Password Locker. What is your name?")
            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")