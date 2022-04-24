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

  def test_store_account_credentials(self):
    '''
    test_store_account_credentials test case to test if the credentials object is stored into the credentials_list
    '''
    self.new_credentials.store_credetials() #store the new credentials
    self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
  unittest.main()