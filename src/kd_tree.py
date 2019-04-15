from .stack import Stack
from .distance import distance


class KdNode:
	def __init__(self, coords, left_child, right_child, name = None, axis = 0):
		self.coordinates = coords
		self.name = name
		self.left_child = left_child
		self.right_child = right_child
		self.axis = axis

	def get_next_and_opposite_nodes(self, ref_location):
		ref_val = ref_location[self.axis]
		this_val = self.coordinates[self.axis]

		if ref_val <= this_val:
			return self.left_child, self.right_child
		else:
			return self.right_child, self.left_child

	def get_distance(self, ref_location):
		return distance(self.coordinates, ref_location)

	def get_distance_to_splitting_plane(self, ref_location):
		# Determining the distance between the ref_location
		# and the splitting plane (described by this node) is
		# simply a matter of finding the distance between the ref_location
		# and point X, where point X is the closest point on the splitting
		# plane to the ref_location
		#
		# Point X is calculated by preserving all values of ref_location
		# except self.axis.
		closest_plane_point = list(ref_location).copy()
		closest_plane_point[self.axis] = self.coordinates[self.axis]
		return distance(ref_location, closest_plane_point)

	def __eq__(self, other):
		# Return True if all children under this node are equal to all children
		# under "other"
		if not isinstance(other, KdNode):
			return False

		node_pair_stack = Stack()
		node_pair_stack.push((self, other))

		while not node_pair_stack.empty():

			my_node, other_node = node_pair_stack.pop()

			# Coordinates
			if my_node.coordinates != other_node.coordinates:
				return False

			# Left Child nonetype checks.
			if (my_node.left_child is None and
						other_node.left_child is not None):
				return False

			elif my_node.left_child is not None:
				next_pair = (my_node.left_child, other_node.left_child)
				node_pair_stack.push(next_pair)

			# Right Child nonetype checks.
			if (my_node.right_child is None and
						other_node.right_child is not None):
				return False

			elif my_node.right_child is not None:
				next_pair = (my_node.right_child, other_node.right_child)
				node_pair_stack.push(next_pair)

		return True


def build_kd_tree(neighbors, depth = 0, num_dimensions = 2):

	if neighbors is None or neighbors.empty:
		return None

	axis = depth % num_dimensions

	sorted_df = neighbors.sort_values(by=[axis])

	median_idx = int(len(sorted_df) / 2)

	next_root = sorted_df.iloc[median_idx]
	next_root_coords = tuple(next_root)
	return KdNode(
		next_root_coords,
		build_kd_tree(sorted_df.iloc[:median_idx], depth = depth + 1),
		build_kd_tree(sorted_df.iloc[median_idx + 1:], depth = depth + 1),
		name = next_root.name,
		axis = axis
	)
