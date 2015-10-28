filename = "out.txt"
from bs4 import BeautifulSoup
import requests
import re
import urllib2
import json
import config
from helper import parse_content

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
ngo_website = ""
ngo_name = ""
ngo_address = ""
ngo_latitude = 0.0
ngo_longitude = 0.0
ngo_contact = ""
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
					ngo_website = link.encode('utf8')
					f.write(link.encode('utf8') + '\n')
					ngo_info = form_request(link)
					description = ngo_info.find('meta', {'name': 'description'})
					if description is None: #Bad URL
						continue
					heading = ngo_info.find('h1', {'class': 'ngo-postheader entry-title'})
					ngo_name = heading.get_text()
					article = heading.parent
					content = article.find('p').get_text()
					#print content
					"""address = (description['content']).encode('utf8')
					f.write(str(address) + '\n')
					#print str(address)+"\n"
					b = str(address).split("Pin" , 1)[0].split(":")[1].strip()
					c = re.split("-|/| ", b)
					d = '+'.join(c)"""
					#get_latlong(d)
					#f.write(d + '\n')
					#f.write(ngo_name.encode('utf8')+"\n")
					result = parse_content(content)
					ngo_address = result[0]
					ngo_website = result[4]
					ngo_contact = result[2]
					ngo_aim = result[7]
					#print ngo_aim.encode("ascii", "ignore")
					print result
					#f.write(content.encode('utf8')+"\n")
				flag = False
