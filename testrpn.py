import unittest

import rpn

class TestBasics(unittest.TestCase):
	# Must start with test_ for unit test to recognize func
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_sub(self):
		result = rpn.calculate('2 1 -')
		self.assertEqual(1, result)

