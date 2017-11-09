import unittest

import rpn

class TestBasics(unittest.TestCase):
	# Must start with test_ for unit test to recognize func
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_sub(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_carrot(self):
		result = rpn.calculate('2 4 ^')
		self.assertEqual(6, result)

