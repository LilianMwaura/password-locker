class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = [] #empty credentials_list

    def __init__(self, account_name, account_password):
        
        self.account_name = account_name
        self.account_password =account_password
    
    def save_credentials (self):

        '''
        save_credentials method saves a new credentials objects to the credentials_list
        '''
        Credentials.credentials_list.append(self)
    
    def delete_user (self):

        '''
        delete_user method deletes a new user objects from the user_list
        '''
        User.user_list.remove(self)
    
    @classmethod
    def display_users (cls):

        '''
        method that returns the contact list 
        '''
        return cls.user_list

