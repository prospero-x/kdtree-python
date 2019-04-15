def square_euclidean_distance(coords1, coords2):
	lon1, lat1 = coords1
	lon2, lat2 = coords2

	return (lat2 - lat1)**2 + (lon2 - lon1)**2


# "distance" is the default implenenation of the distance function.
# In addition to euclidean distances, the haversine formula becomes
# necessary when using latitude and longitude coordinates over
# large distances
distance = square_euclidean_distance