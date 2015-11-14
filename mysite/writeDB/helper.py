#!/usr/bin/python
# This Python file uses the following encoding: utf-8
#import sys
"""content = Add.: E-608, Shakurpur
New Delhi
Pin: 110034
Delhi
Phone: 91-11-27183937
Mobile: 91-97178 17747
Email: varunpmk@gmail.com
Website:
Contact Person: Kandaiyan
Purpose : Child education.
Aims/Objectives/Mission : Our mission at AICCO is to provide quality services for the poor and underprivileged within the slums of India and reaching out to the rural areas as well. Our services will focus on assessing individual strengths and needs, setting personal goals, and providing an environment that encourages growth and development. AICCO’S ultimate goal is to help its beneficiaries live independent."""

#print sys.getdefaultencoding()
def parse_content(content, result):
	first_split = content.encode('utf8').split('Phone:')
	#first_split = content.split('Phone:')
	address = first_split[0].split('Add.:')[1].replace('\n', ' ').strip()
	result.append(address)
	second_split = first_split[1].split('Mobile:')
	phone = second_split[0].replace('\n', ' ').strip()
	result.append(phone)
	third_split = second_split[1].split('Email:')
	mobile = third_split[0].replace('\n', ' ').strip()
	result.append(mobile)
	fourth_split = third_split[1].split('Website:')
	email = fourth_split[0].replace('\n', ' ').strip()
	result.append(email)
	fifth_split = fourth_split[1].split('Contact Person:')
	website = fifth_split[0].replace('\n', ' ').strip()
	result.append(website)
	sixth_split = fifth_split[1].split('Purpose :')
	contact_person = sixth_split[0].replace('\n', ' ').strip()
	result.append(contact_person)
	seventh_split = sixth_split[1].split('Aims/Objectives/Mission :')
	purpose = seventh_split[0].replace('\n', ' ').strip()
	result.append(purpose)
	aim = seventh_split[1].replace('\n', ' ').strip()
	result.append(aim)
	#print result
	return result

#print "Address "+address+"\nPhone "+phone+"\nMobile "+mobile+"\nEmail "+email+"\nWebsite "+website+"\nContact Person "\
#+contact_person+"\nPurpose "+purpose+"\nAim "+aim

