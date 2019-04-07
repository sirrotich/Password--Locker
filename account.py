import pyperclip #Allows copy  and pasting
## if the pyperclip module not working  run this command-----sudo apt-get install xclip-----
class Account:
    """
    Class that generates new instances of accounts.
    """

    account_list = [] # Empty account list


    def __init__(self,account_name,user_name,password,):

      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.phone_password = password


    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)


    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a account that matches that password.

        Args:
            password: Phone password to search for
        Returns :
            account of person that matches the password.
        '''

        for account in cls.account_list:
            if account.phone_password == password:
                return account

    @classmethod
    def account_exist(cls,password):
        '''
        Method that checks if a account exists from the account list.
        Args:
            password: Phone password to search if it exists
        Returns :
                Boolean: True or false depending if account exists
        '''
        for account in cls.account_list:
            if account.phone_password == password:
                return True

        return False

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    # @classmethod
    # def copy_email(cls,password):
    #     account_found = account.find_by_password(password)
    #     pyperclip.copy(account_found.email)
