import csv
import plotly.express as px

CITIES = 'uscities.csv'
UFO = 'archive/complete.csv'


def build_location_mapping():
	loc_map = {}
	with open(CITIES) as f:
		csv_reader = csv.reader(f)
		next(csv_reader) # skip the first line in the file
		for row in csv_reader:
			# make these lowecase to combine the data
			city = row[1].strip().lower()
			state = row[2].strip().lower()
			lat = float(row[6])
			lon = float(row[7])
			loc_map[(city, state)] = (lat, lon)
	return loc_map


def parse_year(datetime):
	"""
	This funciton takes in a string in the form "mont/date/year time" and gives back the year as an int
	"""
	splits = datetime.split()
	date = splits[0]
	date_splits = date.split('/')
	year = date_splits[2]
	return int(year)


def clean_data(line):
	"""
	This function formats user data so that it better matches the data in the uscities.csv
	"""
	if 'mt.' in line:
		line = line.replace('mt.', 'mount')
	if 'ft.' in line:
		line = line.replace('ft.', 'fort')
	return line


def read_ufo_data(loc_map):
	df = {'latitudes': [], 'longitudes': [], 'years': []}
	with open(UFO) as f:
		csv_reader = csv.reader(f)
		next(csv_reader)
		for row in csv_reader:
			# make them both lowercase to combine the data
			year = parse_year(row[0])
			city = row[1].lower()
			city = clean_data(city)
			state = row[2].lower()
			if (city, state) in loc_map:
				lat, lon = loc_map[(city, state)]
				df['latitudes'].append(lat)
				df['longitudes'].append(lon)
				df['years'].append(year)

	print(sorted(df.keys()))
	return df

def plot_data(year_dict):
	fig = px.scatter_geo(year_dict, lat=year_dict['latitudes'], lon=year_dict['longitudes'], color=year_dict['years'], projection="natural earth")
	fig.show()


def main():
	loc_map = build_location_mapping()
	year_dict = read_ufo_data(loc_map)
	plot_data(year_dict)


# these are extra functions that Juliette was playing around with to see how we could store the data
# feel free to check them out if you want to see other ways to plot the data
def read_ufo_data_by_year(loc_map):
	df = {}
	with open(UFO) as f:
		next(f)
		for line in f:
			line = line.strip()
			row = line.split(',')
			# make them both lowercase to combine the data
			date = parse_year(row[0])
			city = row[1].lower()
			city = clean_data(city)
			state = row[2].lower()
			country = row[3]
			if date not in df:
				df[date] = {'latitudes': [], 'longitudes': []}
			if (city, state) in loc_map:
				# print("We do know this location")
				# input()
				lat, lon = loc_map[(city, state)]

				# add to the dictionary for a specific year
				year_dict = df[date]
				year_dict['latitudes'].append(lat)
				year_dict['longitudes'].append(lon)
	print(sorted(df.keys()))
	return df


def store_data_by_count(loc_map):
	df = {}
	with open(UFO) as f:
		next(f)
		for line in f:
			line = line.strip()
			row = line.split(',')
			city = row[1].lower()
			city = clean_data(city)
			state = row[2].lower()
			if (city, state) in loc_map:
				# print("We do know this location")
				# input()
				lat, lon = loc_map[(city, state)]
				if (city, state) not in df:
					df[(city, state)] = {'count': 1, 'coords': (lat,lon)}
				else:
					df[(city, state)]['count'] += 1
	return df


def plot_bubble(df):
	lats = [val['coords'][0] for key, val in df.items()]
	lons = [val['coords'][1] for key, val in df.items()]
	counts = [val['count'] for key, val in df.items()]
	new_df = {'lats': lats, 'lons': lons, 'counts': counts}
	fig = px.scatter_geo(new_df, lat=new_df['lats'], lon=new_df['lons'], size=new_df['counts'])
	fig.show()


def plot_data_by_year(year_dict):
	year = int(input("Please enter the year you want to plot: "))
	if year not in year_dict:
		print("Sorry, we don't have any data for that year")
	else:
		year_data = year_dict[year]
		year2 = 1929
		year_data2 = year_dict[year2]
		# plot the data
		fig = px.scatter_geo(year_data, lat=year_data['latitudes'], lon=year_data['longitudes'], projection="natural earth")
		fig = px.scatter_geo(year_data2, lat=year_data2['latitudes'], lon=year_data2['longitudes'], color='red', projection="natural earth")
		fig.show()


if __name__ == "__main__":
	main()
