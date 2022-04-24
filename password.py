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