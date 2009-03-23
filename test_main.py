"""
sample test module
"""


import unittest

import main


class mainTestCase(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testDummyReturnsNone(self):
		"""dummy returns None by default"""
		expected = None
		self.assertEqual(expected, main.dummy())


if __name__ == "__main__":
	unittest.main()

