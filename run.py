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
    input("Enter your username: ")
    input("Enter password: ")
    print("\n")
    print("account successfully created!")
    print("\n")

  print(f"Hello {user_name}, What would you like to do? ")
  print("\n")
 
  while True:
    print("Use these short codes : cc - create new credential, dc - display all credentials, ex - exit credential list ")
    
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


if __name__ == '__main__':
  main()

