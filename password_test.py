import unittest #import the unittest module
from password import Credentials #import the userpassword locker accouunt class

class TestCredentials (unittest.TestCase):
  def setUp(self):
    '''
    Set up method to run before each test cases
    '''
    self.new_credentials = Credentials("Password-locker-account","Hellen","myPassword") #create credentials object

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_credentials.app_name,"Password-locker-account")
    self.assertEqual(self.new_credentials.user_name,"Hellen")
    self.assertEqual(self.new_credentials.password, "myPassword")

  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    Credentials.credentials_list = [] #Empty the credentials_list

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
  
  def test_delete_credentials(self):
    '''
    test_delete_credentials to test if we can remove credentials from our credentials list
    '''
    self.new_credentials.store_credentials()
    test_credentials = Credentials("Test app","new username","password") #new credentials
    test_credentials.store_credentials()
    self.new_credentials.delete_credentials()#Delete credentials object
    self.assertEqual(len(Credentials.credentials_list),1)

  def test_display_credentials(self):
    '''
    method that returns a list of all credentials saved
    '''
    self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

  def test_find_credential_by_app_name(self):
    '''
    test to check if we can find an account credentials by app name and display information
    '''
    self.new_credentials.store_credentials()
    test_credentials = Credentials("app-name","username","password")
    test_credentials.store_credentials()
    found_credentials = Credentials.find_by_app_name("app-name")
    self.assertEqual(found_credentials.user_name, test_credentials.user_name)

  def test_credentials_exist(self):
    '''
    test to check if the credentials exist by returning a boolean
    '''
    self.new_credentials.store_credentials()
    test_credentials = Credentials("app-name","username","password")
    test_credentials.store_credentials()
    credentials_exist = Credentials.credentials_exist("app-name")
    self.assertTrue(credentials_exist)

if __name__ == '__main__':
  unittest.main()