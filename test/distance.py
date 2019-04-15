from src import square_euclidean_distance
from scipy.spatial import distance
import unittest2


class TestSquareEuclideanDistance(unittest2.TestCase):

	def assertDistancesClose(self, distance, expected):
		absolute_difference = abs(distance - expected)
		fractional_difference = absolute_difference / expected
		self.assertLessEqual(fractional_difference, 0.01)

	def test_equal(self):
		c1 = (1, 2)
		c2 = (1, 2)
		result = square_euclidean_distance(c1, c2)
		expected = 0
		self.assertEqual(result, expected)

	def test_2D_random_1(self):
		c1 = (1, 2)
		c2 = (8, 17)
		result = square_euclidean_distance(c1, c2)
		expected = distance.euclidean(c1, c2) ** 2
		self.assertDistancesClose(result, expected)

	def test_2D_random_2(self):
		c1 = (5, -5)
		c2 = (9, -3)
		result = square_euclidean_distance(c1, c2)
		expected = distance.euclidean(c1, c2) ** 2
		self.assertDistancesClose(result, expected)

	def test_10D_random_1(self):
		c1 = (-1, 5, -10, 5, 1, 7, 7, -8, -3, -9)
		c2 = (-8, -5, 5, 6, -10, 9, -8, 9, -6, -6)
		result = square_euclidean_distance(c1, c2)
		expected = distance.euclidean(c1, c2) ** 2
		self.assertDistancesClose(result, expected)

	def test_10D_random_2(self):
		c1 = (-6, -2, -1, -4, 10, -5, 6, 3, -10, -8)
		c2 = (-10, 8, -6, 9, -10, 2, 4, -9, 10, 7)
		result = square_euclidean_distance(c1, c2)
		expected = distance.euclidean(c1, c2) ** 2
		self.assertDistancesClose(result, expected)


if __name__ == '__main__':
	unittest2.main()