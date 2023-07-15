import requests

# format= input('Please enter the format: ')
# starttime= input('Please enter the starttime: ')
# endtime= input('Please enter the endtime: ')
# latitude= input('Please enter the latitude: ')
# longitude= input('Please enter the longitude: ')
# maxradiuskm= input('Please enter the maxradiuskm: ')
# minmagnitude= input('Please enter the minmagnitude: ')
format= 'geojson' 
    # input('Please enter the format: ')
starttime= '2019-01-01'
    # input('Please enter the starttime: ')
endtime='2019-05-01'
    # input('Please enter the endtime: ')
latitude= '51.51'
    # input('Please enter the latitude: ')
longitude='-0.12'
    # input('Please enter the longitude: ')
maxradiuskm=2000
    # input('Please enter the maxradiuskm: ')
minmagnitude=2
    # input('Please enter the minmagnitude: ')

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept':'application/json'}, params={
		'format': format,
		'starttime':starttime,
		'endtime':endtime,
		'latitude':latitude,
		'longitude':longitude,
		'maxradiuskm':maxradiuskm,
        'minmagnitude':minmagnitude
	})

data = response.json()

i=0
while i<len(data['features']):
    place=data['features'][i]['properties']['place']
    mag=data['features'][i]['properties']['mag']
    print(f'{i+1}. Place: {place}. Magnitude: {mag}.')
    i+=1


