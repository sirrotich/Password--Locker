import unittest # Importing the unittest module
from account import Account # Importing the account class
import pyperclip #Allows copy and pasting


class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
# Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("James","Muriuki","0712345678") # create account object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"James")
        self.assertEqual(self.new_account.user_name,"Muriuki")
        self.assertEqual(self.new_account.phone_password,"0712345678")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)


    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []


    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0712345678") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

    # More tests above
    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0712345678") # new account
            test_account.save_account()

            self.new_account.delete_account()# Deleting a account object
            self.assertEqual(len(Account.account_list),1)

    def test_find_account_by_password(self):
        '''
        test to check if we can find a account by phone password and display information
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0711223344") # new account
        test_account.save_account()

        found_account = Account.find_by_password("0711223344")

        # self.assertEqual(found_account.email,test_account.email)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0711223344") # new account
        test_account.save_account()

        account_exists = Account.account_exist("0711223344")

        self.assertTrue(account_exists)

    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(Account.display_accounts(),Account.account_list)



### FAILED TO ADD TEST AS PER PYPERCLIP
### FAILED TO ADD TEST AS PER PYPERCLIP
### FAILED TO ADD TEST AS PER PYPERCLIP


    # def test_copy_email(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found account
    #     '''
    
    #     self.new_account.save_account()
    #     Account.copy_email("0712345678")
    
    #     self.assertEqual(self.new_account.email,pyperclip.paste())


    


if __name__ == '__main__':
    unittest.main()
