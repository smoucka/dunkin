import json, csv

fields = ['distance',
			'distanceUnit',
			'address',
			'address2',
			'almond',
			'beverageonly',
			'city',
			'co_brander_cd',
			'combostore',
			'country',
			'county',
			'dma_cd',
			'drivein',
			'dunkincardenabled',
			'dunkinrunenabled',
			'faxnumber',
			'fri_hours',
			'geocodequality',
			'k_cup',
			'lat',
			'lc',
			'lng',
			'loyalty',
			'mobile',
			'mon_hours',
			'mqap_geography',
			'mqap_id',
			'mqap_quality',		
			'n',
			'phonenumber',
			'postal',
			'recordid',
			'sat_hours',
			'sitetype',
			'state',
			'sun_hours',
			't',
			'thu_hours',
			'tue_hours',
			'turbooven',
			'website',
			'wed_hours',
			'wireless',
			'key',
			'name',
			'resultNumber',
			'shapePoints',
			'sourceName']


			
with open('dd_wi.js', 'rb') as f:
	with open('dd_wi.csv', 'wb') as c:
		csvwriter = csv.writer(c)
		csvwriter.writerow(fields)
		data = json.load(f)
		locs = data['searchResults']
		key_array = sorted(locs[0].keys())
		for loc in locs:
			to_append = []
			for key in key_array:
				if isinstance(locs[0][key], dict):
					subkey_array = sorted(loc[key].keys())
					for subkey in subkey_array:
						to_append.append(loc[key][subkey])
				else:
					to_append.append(loc[key])
			csvwriter.writerow(to_append)