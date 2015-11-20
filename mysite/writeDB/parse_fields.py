filename = "out.txt"
from bs4 import BeautifulSoup
import requests
import re
import urllib2
import json
import config
from helper import parse_content
import time

import ssl
from functools import wraps
def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar

ssl.wrap_socket = sslwrap(ssl.wrap_socket)

import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()


def get_latlong(addr):
	print addr
	#print "In get_latlong"
	url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+addr+'&key='+config.key
	#response = urllib2.urlopen(url)
	#address = response.read()
	response = requests.get(url, auth=('user', 'pass'))
	address = response.text
	#response.close()
	the_dict = json.loads(address)
	list_components = the_dict['results']
	if list_components:
		for element in list_components:
			if element['geometry']:
				point = element['geometry']['location']
				#f.write(str(point) + '\n\n')
				return point['lat'], point['lng']
				#break
	else:
		global f
		f.write(str(addr) +'\n')
		return 0.0,0.0


def form_request(url):
	req  = requests.get(url)
	data = req.text
	return(BeautifulSoup(data))

def get_result():
	#url = "http://delhi.ngosindia.com/delhi-ngos-55/"
	url = "http://delhi.ngosindia.com/delhi-ngos/"
	flag = True
	ngo_website = ""
	ngo_name = ""
	ngo_address = ""
	ngo_latitude = 0.0
	ngo_longitude = 0.0
	ngo_contact = ""
	total_result = []
	global f
	f = open(filename, 'w')
	while(flag):
		time.sleep(1)
		soup = form_request(url)
		categ_list = soup.find('div', {'class': 'ngo-postcontent clearfix'})
		for a_tag in categ_list.find_all('a'):
			link = a_tag['href']
			name = a_tag.get_text()
			if "Next" in name and a_tag['title'] != "Contact Us":
				url = a_tag['href']
				flag = True
			else:
				if "Previous" not in name and a_tag['title'] != "Contact Us":
					ngo_website = link.encode('utf8')
					#f.write(link.encode('utf8') + '\n')
				        time.sleep(1)	
					ngo_info = form_request(link)
					description = ngo_info.find('meta', {'name': 'description'})
					if description is None: #Bad URL
						continue
					heading = ngo_info.find('h1', {'class': 'ngo-postheader entry-title'})
					ngo_name = heading.get_text()
					article = heading.parent
					content = article.find('p').get_text()
					result = []
					result.append(ngo_name)
					result = parse_content(content, result)
					#print result
					#print "In get_result"
					ngo_address = result[1]
					b = ngo_address.split("Pin" , 1)[0].strip()
					c = re.split("-|/| ", b)
					d = '+'.join(c)
					latitude, longitude = get_latlong(d)
					result.append(latitude)
					result.append(longitude)
					ngo_website = result[4]
					ngo_contact = result[2]
					ngo_aim = result[7]
					#print ngo_aim.encode("ascii", "ignore")
					total_result.append(result)
					print result
					#f.write(ngo_aim+"\n")
					#f.write(content.encode('utf8')+"\n")
				flag = False
	f.close()
	return total_result
#result = get_result()
# result
