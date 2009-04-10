"""
sample test module
"""

import main

import unittest

from unittest import TestCase
#from testsuite import TestCase # exit on first failure


class dummyTestCase(TestCase):

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
