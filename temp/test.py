import string
import re
import sys

#Chops the given file according to its puctuation
#returning: list of phrases(strings).

def textWrap(file):
	chops_list=[]
	chop_aux=[]

	with open (file, 'r') as document:
		for line in document:
			chops_list.append(re.split('[.,]',line))

	return chops_list

a=textWrap(sys.argv[1])
print (a)

