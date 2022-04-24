class User:
    """
    Class that generates new instances of user
    """
    user_list = [] #empty user_list

    def __init__(self, user_name, password):
        
        self.user_name = user_name
        self.password = password
    
    def save_user (self):

        '''
        save_user method saves a new user objects to the user_list
        '''
        User.user_list.append(self)
    
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

    @classmethod
    def verify_login(cls, username, password):
         """
         A method that verifies a user login
         """
         for user in cls.user_list:
             if user.username == username and user.password == password:
                 return user    