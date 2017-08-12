''' 
Context Spell Checker
Copyright (C) 2017

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

#uses Yandex's API to check if the query returns any spell suggestion

import queryenhance

import urllib2
import xml.etree.ElementTree as ET
import time
import glob

def getUserInfos():
	file=open("user_infos.txt",'r')
	lines=file.readlines()
	API_key=lines[0]
	user=lines[1]

	return API_key,user

def spellCheck(query):
	connected=None 

	#try to get user infos. If there is none, exit program.
	try:
		API_key,user=getUserInfos()
		#print "qqqqq"
		print API_key
		print user
		print query
		#print '\n'
	except:
		print ("No user infos found. Please run python config.py")
		raise SystemExit

	#try searching the query online until successful connection is stablished with Yandex's server
	while not connected:
		try:
			search_result=urllib2.urlopen("https://yandex.com/search/xml?user="+user+"&key="+API_key+"&query="+query).read()
			connected=True
		except:
			print "Couldn't connect to Yandex's server. Trying again..."
			pass

	#get the root of the XML returned from the query
	root=ET.fromstring(search_result)

	#search for the element <text>, which provides the misspell
	corrected_query=[]
	for child in root.iter("text"):
		corrected_query=child.text

	#returns Yandex's suggestion if any or -1 otherwise
	if (corrected_query):
		corrected_query=queryenhance.enhanceSuggestion(corrected_query)
		return corrected_query
	else:
		return -1


	