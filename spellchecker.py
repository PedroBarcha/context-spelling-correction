#correctedQuery = Google's "did you mean?"
####TODO######
#Move apy_key to global configs

import urllib2
import xml.etree.ElementTree as ET
import queryenhancer
import time


API_key="03.521135671:6bcae650bac36e850d21a09f20ff4e85"
user="pphbc"

def spellCheck(query):
	connected=None 

	#try searching the query online, until successful connection is stablished with Yandex's server
	while not connected:
		try:
			search_result=urllib2.urlopen("https://yandex.com/search/xml?user="+user+"&key="+API_key+"&query="+query).read()
			connected=True
		except:
			print "Couldn't connect to Yandex's server. Please check your internet connection. Trying again..."
			pass

	#get the root of the XML returned from the query
	root=ET.fromstring(search_result)

	corrected_query=[]
	#search for the element <text>, which provides the misspell
	for child in root.iter("text"):
		corrected_query=child.text

	if (corrected_query):
		#sometimes yandex returns the suggestion inside parenthesis (not sure why tho), so we need to remove them
		corrected_query=queryenhancer.enhanceSuggestion(corrected_query)
		return corrected_query
	else:
		return -1 	#returns -1 if Yandex gives no misspell suggestion


	