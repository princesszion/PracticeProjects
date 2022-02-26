import unittest
from Class_admin import Admin
from Class_client import Client
import Flow_functions



class TestSystemFlow (unittest.TestCase):
    def test_admin_object_is_created_successful(self):  # add assertion here
        admin1 = Admin(223, 'Victor', 'Victor@gmail.com', '1234')
        self.assertTrue(admin1, Admin(223, 'Victor', 'Victor@gmail.com', '1234'))
    def test_check_who_logging_into_the_system_id_is_3(self):
        return_value = Flow_functions.active_user(123)
        self.assertEqual(return_value, True)

    def test_check_who_logging_into_the_system_id_4(self):
        return_value = Flow_functions.active_user(1234)
        self.assertTrue(AssertionError,return_value)
    def test_check_password_not_int(self):
        client1 = Client(2346, 'San', 'san@gmail.com', 2345)
        self.assertTrue(ValueError, Client(2346, 'San', 'san@gmail.com', 'heloo') )

if __name__ == '__main__':
    unittest.main()
