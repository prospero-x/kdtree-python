from src import find_closest, build_kd_tree, distance
import pandas as pd
import unittest2
import random
import uuid
import time

class TestFindClosest(unittest2.TestCase):

	@classmethod
	def coords_to_df(cld, coords):
		'''
		Takes a list of N-dimensional points, with string labels and returns a pandas dataframe
		in which each column X has an integer name and represents the value along
		axis X. The index of each row is the first element of each tuple.

		ex. coords: (('A', 1, 1, 1), ('B', 2, 4, 5), ('C', 3, 7, 5))
			returns: 
			   pd.DataFrame[
							[   0  1  2]
							[A  1  1  1]
							[B  2  4  5]
							[C  3  7  5]]
		'''
		flattened = list(zip(*coords))
		names, values = flattened[0], flattened[1:]
		data = {axis: vals for axis, vals in enumerate(values)}
		return pd.DataFrame(index = names, data = data)

	def test_basic(self):
		neighbors_coords = [
			('A', -6, 3),
			('B', 2, 2.2),
			('C', 3, -6),
		]
		neighbors_df = TestFindClosest.coords_to_df(neighbors_coords)
		ref_location = (-1, -2)
		tree = build_kd_tree(neighbors_df)
		result = find_closest(ref_location, tree)
		self.assertEqual(result.name, "B")
		self.assertEqual(result.coordinates, (2, 2.2))

	def test_all_points_equal(self):
		neighbors_coords = [
			('A', 0,0),
			('B', 0,0),
		]

		neighbors_df = TestFindClosest.coords_to_df(neighbors_coords)
		ref_location = (0, 0)
		tree = build_kd_tree(neighbors_df)
		result = find_closest(ref_location, tree)

		# Not testing the name here. The algorithm does not
		# promise stable traversal of the tree. 
		self.assertEqual(result.coordinates, (0, 0))

	def test_all_neighbors_equal(self):
		neighbors_coords = [
			('A', 1.1,1.3),
			('B', 1.1,1.3),
		]

		neighbors_df = TestFindClosest.coords_to_df(neighbors_coords)
		ref_location = (-1, -2)
		tree = build_kd_tree(neighbors_df)
		result = find_closest(ref_location, tree)

		# Not testing the name here. The algorithm does not
		# promise stable traversal of the tree. 
		self.assertEqual(result.coordinates, (1.1, 1.3))


	def test_inspection_of_both_sides_of_splitting_plane(self):
		'''
		While walking down the kdtree, find_closest chooses to inspect points
		in the left_child or right_child of a node based on whether the 
		ref_location is on the "left" or "right" side of the splitting plane
		created by the node. 

		If the ref_location is closer to the splitting plane than to the
		current closest, then the true closest neighbor might be on the other
		side of the splitting plane.

		If find_closest is doing *everything else* correctly *except*
		inspecting both sides of the splitting plane (when necessary),
		then find_closest will return "D" as the closest neighbor here,
		rather than "E".
		'''
		neighbors_coords = [
			('A', 1.00, 1.00),
			('B', 1.20, 2.00),
			('C', 2.50, 3.50),
			('D', 3.50, 2.80),
			('E', 3.70, 0.80),
			('F', 4.25, 1.80),
			('G', 6.00, 5.60)
		]
		neighbors_df = TestFindClosest.coords_to_df(neighbors_coords)
		ref_location = (3.36, 0.9)
		tree = build_kd_tree(neighbors_df)
		result= find_closest(ref_location, tree)
		self.assertEqual(result.name, "E")
		self.assertEqual(result.coordinates, (3.7,0.8))

	def test_random_1000_points(self):
		total_runs = 10
		for run_num in range(1, total_runs + 1):
			print("Testing 1000 random points, run %d/%d" % (run_num, total_runs))
			
			def rand_val():
				# Choose values between -1 and 1.
				r = random.randint(-1000, 1000)
				while r == 0:
					r = random.randint(-1000, 1000)
				return 1. / r

			# Make 10 random points, with 10 random names.
			neighbors_coords = [
				(uuid.uuid4().hex, rand_val(), rand_val())
				for _ in range(1000)
			]
			neighbors_df = TestFindClosest.coords_to_df(neighbors_coords)

			# Generate a random reference location.
			ref_location = (rand_val(), rand_val())
			tree = build_kd_tree(neighbors_df)
			result = find_closest(ref_location, tree)
			expected_name, expected_coords = find_closest_with_brute_force(neighbors_df, ref_location)
			self.assertEqual(result.name, expected_name)
			self.assertEqual(result.coordinates, expected_coords)

def find_closest_with_brute_force(neighbors_df, ref_location):
	min_distance = 99999999999
	closest_neighbor_name = closest_neighbor_coords = None
	for name, coords in neighbors_df.iterrows():
		d = distance(ref_location, tuple(coords))
		if d < min_distance:
			min_distance = d
			closest_neighbor_name = name
			closest_neighbor_coords = tuple(coords)

	return closest_neighbor_name, closest_neighbor_coords


if __name__ == '__main__':
	unittest2.main()