from yaml import serialize
from password import Credentials
import random

def create_new_credentials(app_name, user_name, password):
  '''
  function to create new user credentials
  '''
  new_credentials = Credentials(app_name, user_name, password)
  return new_credentials

def store_credentials(credential):
  '''
  function to store credentials
  '''
  credential.store_credentials()

def delete_credentials(credential):
  '''
  function to delete credentials
  '''
  credential.delete_credentials()

def find_credentials(app_name):
  '''
  function that finds credentials by app name and returns the app name
  '''
  return Credentials.find_by_app_name(app_name)

def check_existing_app_name(app_name):
  '''
  function that checks if credentials exist with that app_name and returns a boolean
  '''
  return Credentials.credentials_exist(app_name)

def display_credentials():
  '''
  Function that returns all the stored credentials
  ''' 
  return Credentials.display_credentials()

def main():
  first_message = input("Hello, Welcome to Password Locker. Do you already have a password locker account? (Y/N) ").upper()
  print('\n')
  
  if first_message == "Y":
    print("Great!")
    print('\n')
    user_name = input("Please enter your username to login: ")
    password = input("Please enter your password: ")
    print("\n")
    print("Login successful!")
    print("\n")

    
  else:
    print("Follow the instructions to create a password locker account")
    print('\n')
    user_name = input("Enter your username: ")
    input("Enter password: ")
    print("\n")
    print("account successfully created!")
    print("\n")

  print(f"Hello {user_name}, What would you like to do? ")
  print("\n")
 
  while True:
    print("Use these short codes : cc - create new credential, dc - display all credentials, fc - find credentials, delc - delete credentials, ex - exit credential list ")
    
    short_code = input().lower()

    if short_code == "cc":
      print("New Credentials")
      print("*"*20)

      print("App name e.g Twitter, Instagram ....")
      app_name = input()

      print("Username ....")
      user_name = input()

      print("Enter password manually(m) or autogenerate(a)")
      password = input("pick (m/a): ")

      if password == "m":
        print("Enter Password Manually")
        password = input()

      else:
        Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%*&^()"
        password_len = int(input("What length would you like your password to be: "))
        password_count = int(input("How many passwords would you like to generate: "))
        for x in range(0, password_count):
            password = ""
            for x in range(0, password_len):
              password_char = random.choice(Chars)
              password = password + password_char
              print("\n")
            print("Here is your random password: ", password)
       
      store_credentials(create_new_credentials(app_name,user_name,password)) #create and save new credentials
      print("\n")
      print(f"New Credentials {app_name} {user_name} {password} created")
      print("\n")
    
    elif short_code == "dc":
      if display_credentials():
        print("Here is a list of all your credentials ")
        print("\n")

        for credential in display_credentials():
          print(f"App name: {credential.app_name}") | print(f"Username: {credential.user_name}") | print(f"Password: {credential.password}")
        print("\n")
      else:
        print("\n")
        print("You don't seem to have any credentials saved yet")
        print("\n")
    
    elif short_code == "fc":
      print("Enter the app name account you want to search for")

      search_app_name = input()
      if check_existing_app_name(search_app_name):
        search_appl_name = find_credentials(search_app_name)
        print(f"Your username is: {search_appl_name.user_name}")
        print(f"Your password is: {search_appl_name.password}")
        print("*"*50)
      else:
        print("That app name account does not exist")
    
    
    
    elif short_code == "delc":
      print("Enter the account name you want to delete")
      print("*"*50)
      search_name = input().lower()
      if find_credentials(search_name):
        search_credentials = find_credentials(search_name)
        print("*"*50)
        search_credentials.delete_credentials()
        print("\n")
        print(f"Your stored information for: {search_credentials.app_name} successfully deleted!")
        print("\n")
      else:
        print("The credentials you want to delete does not exit in your credentials list")
      
    elif short_code == "ex":
      print(f"Bye {user_name}...")
      break
    else:
      print("I did not get that, please use the short codes")

if __name__ == '__main__':
  main()

