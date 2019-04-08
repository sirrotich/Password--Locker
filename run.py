#!/usr/bin/env python3.6
from credentials  import Credentials
from account  import Account
import random

def create_account(aname, uname,phone):
    '''
    function to create a new account
    '''
    new_account = Account(aname,uname,phone)
    return new_account


def save_accounts(account):
    '''
    function to save account
    '''
    account.save_account()


def find_account(password):
    '''
    Function that finds an account by password and returns the account
    '''
    return Account.find_by_password(password)

def check_existing_accounts(password):
    '''
    Function that check if a account exists with that password and return a Boolean
    '''
    return Account.account_exist(password)  

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()


 ##                             CREDENTIALS


def create_credentials(credentials_name,usr_name,password):
    '''
    Function to create a new account
    '''
    new_credentials = Credentials(credentials_name,usr_name,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save account
    '''
    credentials.save_credentials()    

def del_credentials(credentials):
    '''
    Function to delete a account
    '''
    credentials.delete_credentials(usr_name)    


def find_credentials(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Credentials.find_by_name(name)    

def check_existing_credentials(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Credentials.credentials_exist(name)    

def display_credentials():  
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_credentials() 

def copy_credentials():

    '''
    Function to copy and paste
    '''
    return Credentials.copy_credential(credential_name)

def main():
    print("                                     \033[1;34;40m")
    print("                                     *" * 20)
    print("                                      MAKE YOUR DOCS SAFE WITH PASSWORD LOCKER")
    print("                                     *" * 20)
    print("                                     \033[1;34;40m")
    print("                                     \033[1;37;1m")

    print("To continue tell me your name!") 
    user_name = input()

    print(f"\t\t\t\t\tGreat {user_name}. sign up to continue!")
    print('\n')

    while True:
        print("Check this instructions : SU - sign up, LN - login , SA - see your saved accounts info, LO - logout of the locker")

        inst = input().upper()

        if inst == 'SU':
            print("\t\t\t\t\tNEW ACCOUNT")

            print("Account name")
            a_name = input()

            print("User name")
            u_name = input()

            print("Your password")
            p_password = input()


            save_accounts(create_account(a_name,u_name,p_password)) 
            print('\n')
            print("\033[1;33;40m \n")
            print(f"\t\t\t\t\tNew Account {a_name} {u_name} created")
            print("\033[1;33;40m \n")
            print(f"\t\t\t\tYou can now login to your {a_name} account using your password.")
            print ('\n')

        
        elif inst == 'SA':

            
            if display_accounts():
                    print("\t\t\t\t\tYour accounts")
                    print('\n')

                    for account in display_accounts():
                            print(f"\t\t\t\t\t{account.account_name} {account.user_name} .....{account.phone_password}")

                    print('\t\t\t\t\t\n')
            else:
                    print('\t\t\t\t\t\n')
                    print("\t\t\t\t\tYou dont seem to have any accounts saved yet")
                    print('\n')

        elif inst == 'LN':
            print("\t\t\t\t\tEnter your password to login.")
            search_account = input()
            if check_existing_accounts(search_account):
                    search_cred = find_account(search_account)
                    print("\033[1;32;1m   \n")
                    print(f"\t\t\t\t\tYou are now logged in to your {a_name} account")
                    print("\033[1;37;1m   \n")
            
                #========================================CREDENTIALS AREA=======================================================================
                    while True:
                        print("\033[1;35;40m   \n")
                        print('''\t\t\t\t\t
                        Use these instructions:
                        CA -> Create new credential.
                        DC -> Display your credentials list
                        ex ->Log out your credentials account
                        DL ->Delete credential
                        COP ->Copy credential.''')
                        print("\033[1;35;40m    \n")

                        inst = input().lower()
                        if inst == "ca":
                                print("\t\t\t\t\tCreate new credential")
                                print('_' * 20)
                                credentials_name = input('Credential name:')
                                print('\n')
                                usr_name = input(f"{credentials_name} user name:")
                                print('\n')
                                print('\t\t\t\t\t*' * 20)

                                while True:
                                        print('Please choose \n mp- my pass, gp - generate')
                                        short_code = input().lower()
                                        if short_code == 'mp':
                                                print("cred pass:")
                                                password = input(f"{credentials_name} password:")
                                                break
                                        elif short_code == 'gp':
                                                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                                                password = "".join(random.choice(chars) for _ in range(10))
                                                break

                                save_credentials(create_credentials(credentials_name,u_name,password))
                                print(f"\t\t\t\tA New {credentials_name} Account with the user name  {usr_name} has been created.")
                                print ('\n')
                        elif inst == 'dc':
                                if display_credentials():
                                    print("\t\t\t\t\tHere is your credentials")
                                    print('\n')
                                    for credentials in display_credentials():
                                        print(f"\t\t\t\t\tCredential name:{credentials.credentials_name}  User name: {credentials.usr_name} Password:{credentials.password}")
                                        print('\n')
                                else:
                                    print('\n')
                                    print("\t\t\t\t\tYou don't seem to have created any account yet")
                                    print('\n')

                        elif inst == 'dl':
                                print("\t\t\t\t\tenter the account name of credential you want to delete")
                                deleted_account = input()
                                if del_credentials(deleted_account):
                                        del_credentials(deleted_account)
                                

                        elif inst == 'cop':
                                print(' ')
                                credential_name = input('Enter the cridentials name for the credential password to copy: ')
                                copy_credential(credential_name)
                                print('')
        

                        elif inst == "ex":
                                print('\n')
                                print(f"\t\t\t\t\tYou have logged out your {a_name} account")
                                print('\n')
                                break

                        else:
                                print('\n')
                                print("\t\t\t\t\tWRONG PASSWORD!! PLEASE ENTER CORRECT PASSWORD TO LOGIN")
                                print('\n')
                                print('\n')
                    
        elif inst == "LO":
                    print(f"\t\t\t\t\tThanks {user_name} for your time.I hope you enjoyed my service.Bye...")
                    break

        else:
                    print("\t\t\t\tI really didn't get that. Please use the instructions given")     

        

if __name__ == '__main__':

    main()
    