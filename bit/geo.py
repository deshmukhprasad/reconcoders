from mapbox import Geocoder
from .models import Doctor
from .models import Disease

def foo(add):
	a=Doctor.objects.all()
	b=[]
	coordinates=[]
	geocoder=Geocoder(access_token="pk.eyJ1Ijoib21rYXIyMSIsImEiOiJjanRxc3hoamcwZDNtNGRxZGNnaXF2ZHU3In0.Ovq0lb6DSdnLkIMMb32UPA")
	for i in add:
		response=geocoder.forward(i)
		collection=response.json()
		coordinates.append(collection['features'][0]['center'][0])
		coordinates.append(collection['features'][0]['center'][1])
	print(coordinates)
	return(coordinates)

def months():
	a=Disease.objects.all()
	n=len(a)
	s=(a[n-1].date)
	m = int(s[5:7])