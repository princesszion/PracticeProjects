import unittest
from Class_client import Client

class MyTestCase(unittest.TestCase):
    def test_check_if_temperature_updates(self):
        client1 = Client(253, 'san', 'san@gmail.com', '1234')
        self.assertEqual(client1.temperature_regulator(), client1.set_temperature)

    def test_check_if_temperature_is_int(self):
        client1 = Client(253, 'san', 'san@gmail.com', '1234')
        self.assertRaises(TypeError, client1.temperature_regulator(), 'cold')

if __name__ == '__main__':
    unittest.main()
