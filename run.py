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