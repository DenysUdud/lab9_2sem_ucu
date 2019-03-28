import unittest
from class_lab.square_preceding import square_preceding


class TestSquare_preceding(unittest.TestCase):
	def test_square_preceding(self):
		l = [1, 2, 3]
		square_preceding(l)
		self.assertEqual([0, 1, 4], l)
		l = [2, 3, 9]
		square_preceding(l)
		self.assertEqual([0, 4, 9], l)
		l = [0, 1, 0]
		square_preceding(l)
		self.assertEqual([0, 0, 1], l)
		l = []
		square_preceding(l)
		self.assertEqual([], l)
		l = 1
		square_preceding(l)
		self.assertEqual(1, l)








if __name__ == '__main__':
    unittest.main()
