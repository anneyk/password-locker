class Credentials:
  '''
  Class creates new instance of user password locker account class
  '''
  def __init__(self, app_name, user_name, password):
    self.app_name = app_name
    self.user_name = user_name
    self.password = password
