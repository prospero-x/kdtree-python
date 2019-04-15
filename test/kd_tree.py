import unittest2
from src import build_kd_tree, KdNode
import pandas as pd


class TestKdTreeEqualityOperator(unittest2.TestCase):

	def test_none(self):
		tree = KdNode((0, 0), None, None)
		self.assertIsNotNone(tree)

	def test_identical_single_node_trees(self):
		tree1 = KdNode((0, 0), None, None)
		tree2 = KdNode((0, 0), None, None)
		self.assertEqual(tree1, tree2)

	def test_different_single_node_tree(self):
		tree1 = KdNode((0, 0), None, None)
		tree2 = KdNode((1, 0), None, None)
		self.assertNotEqual(tree1, tree2)

	def test_identical_multi_node_unbalanced_trees(self):
		tree1 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = None
				),
				right_child = None
			),
			right_child = None
		)

		tree2 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					(2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = None
				),
				right_child = None
			),
			right_child = None
		)

		self.assertEqual(tree1, tree2)

	def test_multi_node_unbalanced_trees_with_different_root(self):
		tree1 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = None
				),
				right_child = None
			),
			right_child = None
		)

		tree2 = KdNode(
			coords = (-1, -1),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					(2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = None
				),
				right_child = None
			),
			right_child = None
		)

		self.assertNotEqual(tree1, tree2)

	def test_multi_node_unbalanced_trees_with_different_middle_nodes(self):
		tree1 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = None
				),
				right_child = None
			),
			right_child = None
		)

		tree2 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (-1, -1),
				left_child = KdNode(
					(2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = None
				),
				right_child = None
			),
			right_child = None
		)

		self.assertNotEqual(tree1, tree2)

	def test_multi_node_unbalanced_trees_with_different_leafs(self):
		tree1 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = None
				),
				right_child = None
			),
			right_child = None
		)

		tree2 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					(2, 2),
					left_child = KdNode(
						coords = (3, 3),
						left_child = KdNode((4, 4), None, None),
						right_child = None,
					),
					right_child = None
				),
				right_child = None
			),
			right_child = None
		)

		self.assertNotEqual(tree1, tree2)

	def test_identical_multi_node_balanced_trees(self):
		tree1 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = KdNode((4, 4), None, None)
				),
				right_child = KdNode(
					coords = (5, 5),
					left_child = KdNode((6, 6), None, None),
					right_child = None
				)
			),
			right_child = KdNode(
				coords = (7, 7),
				left_child = KdNode(
					coords = (8, 8),
					left_child = KdNode((9, 9), None, None),
					right_child = KdNode((10, 10), None, None)
				),
				right_child = KdNode(
					coords = (11, 11),
					left_child = KdNode((12, 12), None, None),
					right_child = None
				)
			),
		)

		tree2 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = KdNode((4, 4), None, None)
				),
				right_child = KdNode(
					coords = (5, 5),
					left_child = KdNode((6, 6), None, None),
					right_child = None
				)
			),
			right_child = KdNode(
				coords = (7, 7),
				left_child = KdNode(
					coords = (8, 8),
					left_child = KdNode((9, 9), None, None),
					right_child = KdNode((10, 10), None, None)
				),
				right_child = KdNode(
					coords = (11, 11),
					left_child = KdNode((12, 12), None, None),
					right_child = None
				)
			),
		)

		self.assertEqual(tree1, tree2)

	def test_multi_node_balanced_trees_with_different_roots(self):
		tree1 = KdNode(
			coords = (-1, -1),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = KdNode((4, 4), None, None)
				),
				right_child = KdNode(
					coords = (5, 5),
					left_child = KdNode((6, 6), None, None),
					right_child = None
				)
			),
			right_child = KdNode(
				coords = (7, 7),
				left_child = KdNode(
					coords = (8, 8),
					left_child = KdNode((9, 9), None, None),
					right_child = KdNode((10, 10), None, None)
				),
				right_child = KdNode(
					coords = (11, 11),
					left_child = KdNode((12, 12), None, None),
					right_child = None
				)
			),
		)

		tree2 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = KdNode((4, 4), None, None)
				),
				right_child = KdNode(
					coords = (5, 5),
					left_child = KdNode((6, 6), None, None),
					right_child = None
				)
			),
			right_child = KdNode(
				coords = (7, 7),
				left_child = KdNode(
					coords = (8, 8),
					left_child = KdNode((9, 9), None, None),
					right_child = KdNode((10, 10), None, None)
				),
				right_child = KdNode(
					coords = (11, 11),
					left_child = KdNode((12, 12), None, None),
					right_child = None
				)
			),
		)

		self.assertNotEqual(tree1, tree2)

	def test_multi_node_balanced_trees_with_different_middle_nodes(self):
		tree1 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = KdNode((4, 4), None, None)
				),
				right_child = KdNode(
					coords = (5, 5),
					left_child = KdNode((6, 6), None, None),
					right_child = None
				)
			),
			right_child = KdNode(
				coords = (20, 20),
				left_child = KdNode(
					coords = (8, 8),
					left_child = KdNode((9, 9), None, None),
					right_child = KdNode((10, 10), None, None)
				),
				right_child = KdNode(
					coords = (11, 11),
					left_child = KdNode((12, 12), None, None),
					right_child = None
				)
			),
		)

		tree2 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = KdNode((4, 4), None, None)
				),
				right_child = KdNode(
					coords = (5, 5),
					left_child = KdNode((6, 6), None, None),
					right_child = None
				)
			),
			right_child = KdNode(
				coords = (7, 7),
				left_child = KdNode(
					coords = (8, 8),
					left_child = KdNode((9, 9), None, None),
					right_child = KdNode((10, 10), None, None)
				),
				right_child = KdNode(
					coords = (11, 11),
					left_child = KdNode((12, 12), None, None),
					right_child = None
				)
			),
		)

		self.assertNotEqual(tree1, tree2)

	def test_multi_node_balanced_trees_with_different_leafs(self):
		tree1 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = KdNode((4, 4), None, None)
				),
				right_child = KdNode(
					coords = (5, 5),
					left_child = KdNode((6, 6), None, None),
					right_child = None
				)
			),
			right_child = KdNode(
				coords = (7, 7),
				left_child = KdNode(
					coords = (8, 8),
					left_child = KdNode((9, 9), None, None),
					right_child = KdNode((10, 10), None, None)
				),
				right_child = KdNode(
					coords = (11, 11),
					left_child = KdNode((12, 12), None, None),
					right_child = None
				)
			),
		)

		tree2 = KdNode(
			coords = (0, 0),
			left_child = KdNode(
				coords = (1, 1),
				left_child = KdNode(
					coords = (2, 2),
					left_child = KdNode((3, 3), None, None),
					right_child = KdNode((4, 4), None, None)
				),
				right_child = KdNode(
					coords = (5, 5),
					left_child = KdNode((6, 6), None, None),
					right_child = None
				)
			),
			right_child = KdNode(
				coords = (7, 7),
				left_child = KdNode(
					coords = (8, 8),
					left_child = KdNode((9, 9), None, None),
					right_child = KdNode((10, 10), None, None)
				),
				right_child = KdNode(
					coords = (11, 11),
					left_child = KdNode((99, 99), None, None),
					right_child = None
				)
			),
		)

		self.assertNotEqual(tree1, tree2)


class TestBuildKdTree(unittest2.TestCase):

	def coords_to_df(self, coords):
		'''
		Takes a list of N-dimensional points and returns a pandas dataframe
		in which each column X has an integer name and represents the value
		along axis X. There is no index.

		ex. coords: ((1, 1, 1), (2, 4, 5), (3, 7, 5))
			returns:
				pd.DataFrame[
							[   0  1  2]
							[0  1  1  1]
							[1  2  4  5]
							[2  3  7  5]]
		'''
		data = {axis: vals for axis, vals in enumerate(zip(*coords))}
		return pd.DataFrame(data = data)

	def test_build_empty_list(self):
		tree = build_kd_tree(None)
		self.assertIsNone(tree)

	def test_build_single_node(self):
		df = self.coords_to_df([(0, 0), ])

		tree = build_kd_tree(df)
		expected = KdNode((0, 0), None, None)

		self.assertTrue(tree == expected)

	def test_build_two_nodes(self):
		df = self.coords_to_df([(0, 0), (1, 1)])
		result = build_kd_tree(df)
		expected = KdNode(
			coords = (1, 1),
			left_child = KdNode((0, 0), None, None),
			right_child = None
		)

		self.assertEqual(result, expected)

	def test_build_three_nodes(self):
		df = self.coords_to_df([(0, 0), (1, 1), (2, 2)])
		result = build_kd_tree(df)
		expected = KdNode(
			coords = (1, 1),
			left_child = KdNode((0, 0), None, None),
			right_child = KdNode((2, 2), None, None)
		)

		self.assertEqual(result, expected)

	def test_build_many_nodes_1(self):
		'''
		Many nodes tests: The idea is that if we choose random datasets
		for each test, two random datasets might overlap such that the two
		tests are actually testing the same thing.

		In order to cover more corner cases, we start with a non-trivial
		dataset and change it slightly for each new test.
		'''
		df = self.coords_to_df([(2, 7), (5, 4), (9, 6), (4, 3), (8, 1)])
		result = build_kd_tree(df)
		expected = KdNode(
			coords = (5, 4),
			left_child = KdNode(
				coords = (2, 7),
				left_child = KdNode((4, 3), None, None),
				right_child = None
			),
			right_child = KdNode(
				coords = (9, 6),
				left_child = KdNode((8, 1), None, None),
				right_child = None
			)
		)

		self.assertEqual(result, expected)

	def test_build_many_nodes_2(self):
		'''
		One more node than the previous test.
		'''
		df = self.coords_to_df(
			[(2, 7), (5, 4), (9, 6), (4, 3), (8, 1), (7, 2)]
		)
		result = build_kd_tree(df)
		expected = KdNode(
			coords = (7, 2),
			left_child = KdNode(
				coords = (5, 4),
				left_child = KdNode((4, 3), None, None),
				right_child = KdNode((2, 7), None, None)
			),
			right_child = KdNode(
				coords = (9, 6),
				left_child = KdNode((8, 1), None, None),
				right_child = None
			)
		)

		self.assertEqual(result, expected)

	def test_build_many_nodes_3(self):
		'''
		One more node than the previous test.
		'''
		df = self.coords_to_df(
			[(2, 7), (5, 4), (9, 6), (4, 3), (8, 1), (7, 2), (10, 3)]
		)
		result = build_kd_tree(df)
		expected = KdNode(
			coords = (7, 2),
			left_child = KdNode(
				coords = (5, 4),
				left_child = KdNode((4, 3), None, None),
				right_child = KdNode((2, 7), None, None)
			),
			right_child = KdNode(
				coords = (10, 3),
				left_child = KdNode((8, 1), None, None),
				right_child = KdNode((9, 6), None, None)
			)
		)

		self.assertEqual(result, expected)

	def test_build_many_nodes_4(self):
		'''
		One more node than the previous test.
		'''
		df = self.coords_to_df(
			[(2, 7), (5, 4), (9, 6), (4, 3), (8, 1), (7, 2), (10, 3), (11, 0)]
		)
		result = build_kd_tree(df)
		expected = KdNode(
			coords = (8, 1),
			left_child = KdNode(
				coords = (5, 4),
				left_child = KdNode(
					coords = (7, 2),
					left_child = KdNode((4, 3), None, None),
					right_child = None
				),
				right_child = KdNode((2, 7), None, None)
			),
			right_child = KdNode(
				coords = (10, 3),
				left_child = KdNode((11, 0), None, None),
				right_child = KdNode((9, 6), None, None)
			)
		)

		self.assertEqual(result, expected)
