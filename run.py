from password import Credentials

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
  first_message = input("Hello, Welcome to Password Locker. Do you already have a password locker account? (Y/N) ")
  print('\n')
  
  if first_message == "Y":
    print("Great!")
    print('\n')
    user_name = input("Please enter your username: ")
    password = input("Please enter your password: ")

if __name__ == '__main__':
  main()

