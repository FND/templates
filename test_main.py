"""
sample test module
"""


import main

import unittest


class dummyTestCase(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testReturnsNone(self):
		"""dummy returns None by default"""
		actual = main.dummy()
		expected = None
		self.assertEqual(actual, expected)


if __name__ == "__main__":
	unittest.main()
