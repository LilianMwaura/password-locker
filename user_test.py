import unittest # Importing the unittest module
from user import User # Importing the user class
from credentials import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Wambui","1234") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Wambui")
        self.assertEqual(self.new_user.password,"1234")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
    
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Wambui","1234") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)

    def test_display_users(self):
        '''
        method that returns a list of all users saved
        '''
        
        self.assertEqual(User.display_users(),User.user_list)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
     
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_cred = Credentials("Instagram","2020")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_cred.account_name,"Instagram")
        self.assertEqual(self.new_cred.account_password,"2020") 
    
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the creential object is saved into
        the credential list
        '''
        self.new_cred.save_credentials() 
        self.assertEqual(len(Credentials.credentials_list),1)               
    
    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a cred from our cred list
        '''
        self.new_cred.save_credentials()
        test_cred = Credentials("Instagram","2020")
        test_cred.save_credentials()

        self.new_cred.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_display_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list) 
    
if __name__ == '__main__':
    unittest.main()