from src import find_closest, build_kd_tree
import pandas as pd
import requests
import sys


# Free City of Chicago API, containing JSON data for CTA Train stations
URL = "https://data.cityofchicago.org/resource/8mj8-j3c4.json"

# Usually, something like Apache Thrift is better for serialization.
# However, Pandas dataframes are surprisingly performant with pickle.
PICKLE_FILENAME = "example/pickled_data.gz"


def download_data():
	'''
	Downloads the CTA Train Station locations from the web,
	and formats in into a Pandas Dataframe for use by the KDTree.
	'''
	response = requests.get(URL)
	if response.status_code != requests.codes.ok:
		print(
			"Response status was '%s'" % response.status_code +
			" when requesting '%s'." % URL
		)
		sys.exit(1)

	json_records = response.json()
	df = pd.DataFrame.from_records(json_records)

	# Discard all but the most relevant columns
	df = df[['location', 'station_descriptive_name']]

	# Location values are still dictionaries of the form:
	# {'type': 'Point', 'coordinates': [-87.669147, 41.857908]}.
	# Below, we unpack them.
	df[0] = df['location'].apply(lambda d: d['coordinates'][0])
	df[1] = df['location'].apply(lambda d: d['coordinates'][1])

	# No longer need the original location column
	del df['location']

	# Finally, reindex with the station names.
	df = df.set_index('station_descriptive_name')
	return df


def get_cta_station_locations():
	'''
	Download data if it lives in this directly. Otherwise download
	if from the web and save it locally for future use.
	'''
	try:
		df = pd.read_pickle(PICKLE_FILENAME)
	except Exception:
		df = download_data()
		df.to_pickle(PICKLE_FILENAME, compression = 'gzip')
	return df


if __name__ == '__main__':
	stations_df = get_cta_station_locations()
	tree = build_kd_tree(stations_df)

	the_bean = (-87.6233, 41.8827)
	result = find_closest(the_bean, tree)
	print(
		"The closest CTA stop to The Bean {0} is '{1}' {2}.".format(
			the_bean, result.name, result.coordinates
		)
	)