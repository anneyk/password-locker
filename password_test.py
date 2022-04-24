import unittest #import the unittest module
from password import UserPasswordLockerAccount #import the userpassword locker accouunt class

class TestUserPasswordLockerAccount (unittest.TestCase):
  def setUp(self):
    '''
    Set up method to run before each test cases
    '''
    self.new_password_locker_account = UserPasswordLockerAccount("Password-locker-account","Hellen","myPassword") #create a password locker account object

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_password_locker_account.app_name,"Password-locker-account")
    self.assertEqual(self.new_password_locker_account.user_name,"Hellen")
    self.assertEqual(self.new_password_locker_account.password, "myPassword")

  def test_store_existing_account_credentials(self):
    '''
    test_store_existing_account_credentials test case to test if the password object is stored into the password_list
    '''

if __name__ == '__main__':
  unittest.main()