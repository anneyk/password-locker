from password import Credentials

def create_user(app_name, user_name, password):
  '''
  function to create new password locker user
  '''
  new_user = Credentials(app_name, user_name, password)
  return new_user

