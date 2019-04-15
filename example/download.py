import requests
import pandas as pd
import sys
import logging

logger = logging.getLogger(__name__)

URL = "https://data.cityofchicago.org/resource/8mj8-j3c4.json"

def download_data():
	response = requests.get(URL)
	if response.status_code != requests.codes.ok:
		logger.fatal(
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
