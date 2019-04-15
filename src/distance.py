def square_euclidean_distance(p1, p2):
	'''
	Since we're only comparing distances, we simply
	calculate the Euclidean Distance without taking the
	square root at the end.
	'''
	return sum((x[0] - x[1])**2 for x in zip(p1, p2))


# "distance" is the default implenenation of the distance function.
# In addition to euclidean distances, the haversine formula becomes
# necessary when using latitude and longitude coordinates over
# large distances.
distance = square_euclidean_distance