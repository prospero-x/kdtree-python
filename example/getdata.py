from download import download_data
import pandas as pd


# Usually, something like Apache Thrift is better for serialization. 
# However, Pandas dataframes are surprisingly performant with pickle.
PICKLE_FILENAME = "example/pickled_data.gz"

def get_cta_station_locations():
	try:
		df = pd.read_pickle(PICKLE_FILENAME)
	except Exception:
		df = download_data()
		df.to_pickle(PICKLE_FILENAME, compression = 'gzip')
	return df
