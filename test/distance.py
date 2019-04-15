from src import square_euclidean_distance
from scipy.spatial import distance
import unittest2
import time
from random import randint


class TestSquareEuclideanDistance(unittest2.TestCase):

	def assertDistancesClose(self, distance, expected):
		absolute_difference = abs(distance - expected)
		fractional_difference = absolute_difference / expected
		self.assertLessEqual(fractional_difference, 0.01)

	def test_equal(self):
		c1 = (1,2)
		c2 = (1,2)
		result = square_euclidean_distance((1,2), (1,2))
		expected = 0
		self.assertEqual(result, expected)

	def test_random_1(self):
		c1 = (1,2)
		c2 = (8,17)	
		result = square_euclidean_distance(c1, c2)
		expected = distance.euclidean(c1, c2) ** 2
		self.assertDistancesClose(result, expected)

	def test_random_2(self):
		c1 = (5,-5)
		c2 = (9,-3)
		result = square_euclidean_distance(c1, c2)
		expected = distance.euclidean(c1, c2) ** 2
		self.assertDistancesClose(result, expected)


if __name__ == '__main__':
	unittest2.main()	