import unittest
import functionCheckout

class TestCheckoutFunction(unittest.TestCase):
	def test_that_get_questions_exist(self):
		functionCheckout.get_questions("purchase" , [], [], [])

	

