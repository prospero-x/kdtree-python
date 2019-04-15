from .stack import Stack


def find_closest(ref_location, kd_tree):
	'''
	:param ref_location: tuple of (longitude, latitude) of current location
	:param kd_tree: kd-tree representing locations of neighbors
	:return: the KDNode object of the closest neighbor to ref_location
	'''
	search_stack = Stack()

	# Start with the distance to the root
	search_stack.push(kd_tree)
	closest = kd_tree
	distance_to_closest = closest.get_distance(ref_location)

	while not search_stack.empty():
		current_node = search_stack.pop()

		distance_to_node = current_node.get_distance(ref_location)

		if distance_to_node < distance_to_closest:
			closest = current_node
			distance_to_closest = distance_to_node

		next_node, opposite_node = current_node.get_next_and_opposite_nodes(
			ref_location
		)

		if next_node is not None:
			search_stack.push(next_node)

		# If the ref_location is closer to the splitting plane than to the
		# current closest, then the true closest neighbor might be on the
		# other side of the plane.
		dist_to_split = current_node.get_distance_to_splitting_plane(
			ref_location
		)
		if distance_to_closest > dist_to_split and opposite_node is not None:
			search_stack.push(opposite_node)

	return closest
