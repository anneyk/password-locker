from tkinter import Y
from password import Credentials
import random

def create_user(app_name, user_name, password):
  '''
  function to create new password locker user
  '''
  new_user = Credentials(app_name, user_name, password)
  return new_user

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
    user_name = input("Please enter your username: ")
    password = input("Please enter your password: ")
    print("\n")
    print("Login successful!")
    print("\n")

    
  else:
    print("Follow the instructions to create a password locker account")
    print('\n')
    input("Enter your username: ")
    input("Enter password: ")
    print("\n")
    print("account successfully created!")
    print("\n")

  print(f"Hello {user_name}, What would you like to do ")
  print("\n")
 
  while True:
    print("Use these short codes : cc - create new credential, dc - display all credentials, ex - exit credential list ")
    
    short_code = input().lower()
   
  # Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%*&^()"

  # while 1:
  #   password_len = int(input("What length would you like your password to be: "))
  #   password_count = int(input("How many passwords would you like to generate: "))
  #   for x in range(0, password_count):
  #     password = ""
  #     for x in range(0, password_len):
  #       password_char = random.choice(Chars)
  #       password = password + password_char
  #     print("Here is your random password: ", password)


if __name__ == '__main__':
  main()

