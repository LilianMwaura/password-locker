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
    
    def delete_credentials (self):

        '''
        delete_credentials method deletes a new credentials objects from the credentials_list
        '''
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def display_credentials(cls):

        '''
        method that returns the credentials list 
        '''
        return cls.credentials_list
    
    @classmethod
    def get_credentials(cls, account_name):
        """
        A method that finds and returns credentials
        """
        for credential in cls.credentials_list:
            credential.account_name == account_name
            return credential
