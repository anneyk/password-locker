import unittest #import the unittest module
from password import Credentials #import the userpassword locker accouunt class

class TestCredentials (unittest.TestCase):
  def setUp(self):
    '''
    Set up method to run before each test cases
    '''
    self.new_credentials = Credentials("Password-locker-account","Hellen","myPassword") #create a password locker account object

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_credentials.app_name,"Password-locker-account")
    self.assertEqual(self.new_credentials.user_name,"Hellen")
    self.assertEqual(self.new_credentials.password, "myPassword")

  def test_store_existing_account_credentials(self):
    '''
    test_store_existing_account_credentials test case to test if the password object is stored into the password_list
    '''

if __name__ == '__main__':
  unittest.main()