filename = "out1.txt"
from bs4 import BeautifulSoup
import requests
import re
import urllib2
import json
import config

def get_latlong(addr):
	url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+addr+'&key='+config.key
	response = urllib2.urlopen(url)
	address = response.read()
	the_dict = json.loads(address)
	list_components = the_dict['results']
	for element in list_components:
		if element['geometry']:
			point = element['geometry']['location']
			f.write(str(point) + '\n\n')
			print point
			break

url = "http://delhi.ngosindia.com/delhi-ngos/"
flag = True
def form_request(url):
	req  = requests.get(url)
	data = req.text
	return(BeautifulSoup(data))

with open(filename, 'w') as f:
	while(flag):
		soup = form_request(url)
		categ_list = soup.find('div', {'class': 'ngo-postcontent clearfix'})
		for a_tag in categ_list.find_all('a'):
			link = a_tag['href']
			name = a_tag.get_text()
			if "Next" in name:
				url = a_tag['href']
				flag = True
			else:
				if "Previous" not in name:
					f.write(link.encode('utf8') + '\n')
					ngo_info = form_request(link)
					description = ngo_info.find('meta', {'name': 'description'})
					if description is None: #Bad URL
						continue
					address = (description['content']).encode('utf8')
					f.write(str(address) + '\n')
					#print str(address)+"\n"
					b = str(address).split("Pin" , 1)[0].split(":")[1].strip()
					c = re.split("-|/| ", b)
					d = '+'.join(c)
					get_latlong(d)
					#f.write(d + '\n')
					#print str(address)+"\n"
				flag = False
