import pyperclip


class Credentials:
  '''
  Class creates new instance of user password locker account class
  '''
  credentials_list = [] #store our credentials here by appendng after executing store_credentials()
  
  def __init__(self, app_name, user_name, password):
    self.app_name = app_name
    self.user_name = user_name
    self.password = password

  def store_credentials(self):
    '''
    store_credentials method stores credentials objects into the credentials_list
    '''
    Credentials.credentials_list.append(self)

  def delete_credentials(self):
    '''
    delete_credentials method deletes stored credentials from the credentials_list
    '''
    Credentials.credentials_list.remove(self)
    
  @classmethod
  def display_credentials(cls):
    '''
    method that returns the credentials list
    '''
    return cls.credentials_list
  
  @classmethod
  def find_by_app_name(cls,app_name):
    '''
    Method that takes in an app name and returns a contact that matches that number.
    '''
    for credential in cls.credentials_list:
      if credential.app_name == app_name:
        return credential

  @classmethod
  def credentials_exist(cls,app_name):
    '''
    method that checks if credentials exist in a credentials list
    '''
    for credential in cls.credentials_list:
      if credential.app_name == app_name:
        return True
    return False
  
  @classmethod
  def copy_password(cls, app_name):
    credentials_found = Credentials.find_by_app_name(app_name)
    pyperclip.copy(credentials_found.password)