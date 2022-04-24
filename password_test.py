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

  def test_store_credentials(self):
    '''
    test_store_credentials test case to test if the credentials object is stored into the credentials_list
    '''
    self.new_credentials.store_credentials() #store the new credentials
    self.assertEqual(len(Credentials.credentials_list),1)

  def test_store_multiple_credentials(self):
    '''
    test_store_mutiple_credentials to check if we can store multiple credentials objects to our credentials_list
    '''
    self.new_credentials.store_credentials()
    test_credentials = Credentials("Twitter", "Hellie_","myTwitterPassword") #new account credentials
    test_credentials.store_credentials()
    self.assertEqual(len(Credentials.credentials_list),2)


if __name__ == '__main__':
  unittest.main()