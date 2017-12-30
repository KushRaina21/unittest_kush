import unittest
import Customer


class CustomerTest(unittest.TestCase):
    def setUp (self):
        print("Setting up Customer")
	self.customer1=Customer("Kush")
	self.customer1.set_balance=1000.0
    def tearDown (self):
        print("Cleaning up CustomerTest cases")
    def test_withdraw(self):
	print(" test withdraw functionality")
	self.assertEqual(self.customer1.withdraw(500.0),500.0)
	self.assertRaises(RuntimeError,self.customer1.withdraw,1500.0)
	self.customer1.set_balance=2000.0
	self.assertEqual(self.customer1.withdraw(1500.0),500.0)
    def test_deposit(self):
	print(" test deposit functionality")
	self.assertEqual(self.customer1.deposit(500.0),1500.0)
	self.customer1.set_balance=2000.0
	self.assertEqual(self.customer1.deposit(1500.0),3500.0)
    
if __name__ == ‘__main__’:
    unittest.main()
    