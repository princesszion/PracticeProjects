import unittest
from Class_client import Client


#create and instantiate test class.
class TestFunctions(unittest.TestCase):
    def test_client_object_is_created_successful(self):  # add assertion here
        client1 = Client(223,'Vic','Vic@gmail.com','1234')
        self.assertTrue(client1, Client(223,'567','Vic@gmail.com','1234'))

    def test_check_amount_water(self):  # add assertion here
        client1 = Client(253,'san','san@gmail.com','1234', amount_of_water=3)
        self.assertRaises(TypeError,client1.check_water_limit(), 3 )
    def test_check_water_limit_true(self):  # add assertion here
        client1 = Client(253, 'san', 'san@gmail.com', '1234', amount_of_water=3)
        self.assertEqual(client1.check_water_limit(), True)

    def test_water_limit_false(self):  # add assertion here
        client1 = Client(253, 'san', 'san@gmail.com', '1234', amount_of_water= 8)
        self.assertEqual(client1.check_water_limit(), False)

    def test_check_water_limit_different_type(self):  # add assertion here
        client1 = Client(253, 'san', 'san@gmail.com', '1234', amount_of_water= 8)
        self.assertRaises(TypeError,client1.check_water_limit(), "good" )

    def test_check_water_limit_regulator_false(self):  # add assertion here
        client1 = Client(253,'san','san@gmail.com','1234', water_supply=5 )
        self.assertEqual(client1.water_limit_regulator(), False)

    def test_check_water_limit_regulator_true(self):  # add assertion here
        client1 = Client(253, 'san', 'san@gmail.com', '1234', water_supply = 2)
        self.assertEqual(client1.water_limit_regulator(), True)

    def test_check_water_limit_regulator_4(self):  # add assertion here
        client1 = Client(253, 'san', 'san@gmail.com', '1234', water_supply = 4)
        self.assertEqual(client1.water_limit_regulator(), client1.water_supply)

    def test_check_water_limit_regulator_4_true(self):  # add assertion here
        client1 = Client(253, 'san', 'san@gmail.com', '1234', water_supply=4)
        self.assertRaises(TypeError,client1.water_limit_regulator(), True)

    def test_check_water_limit_regulator_5(self):  # add assertion here
        client1 = Client(253, 'san', 'san@gmail.com', '1234', water_supply=5)
        self.assertRaises(TypeError,client1.water_limit_regulator(), client1.water_supply)
    def test_check_water_left(self):
          client1 = Client(253, 'san', 'san@gmail.com', '1234',max_water_limit=5,water_supply=3)
          self.assertEqual(client1.check_water_left(),  client1.max_water_limit - client1.water_supply)

    def test_calculate_bill(self):
        client1 = Client(253, 'san', 'san@gmail.com', '1234', default_cost=1000, water_supply=3)
        self.assertEqual(client1.calculate_bill(), client1.default_cost + (client1.water_supply * 1000))




if __name__ == '__main__':
    unittest.main()
