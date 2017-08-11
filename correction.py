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

#wraps single or several text files into words_per_query words blocks, query them to yandex and if it 
#suggests a spell correction (like google's "did you mean"), then the original phrase is
#subtituted by the given suggestion. Otherwise, the phrase reamins the same in the file.

from lib import spellcheck, queryenhance, wrapper

import glob
import time
import sys  

#set unicode as default encoding
reload(sys)  
sys.setdefaultencoding('utf8')

time1=time.time()
total_queries=0
yandex_suggestions=0
corrections_file="yandex_suggestions.txt"

#text will be chopped into block with words_per_query words
words_per_query=8

#for every file specified in the terminal input
for filename in sys.argv[1:]:
	corrected_queries=[]

	#wrap file into several phrases
	queries_list=wrapper.textWrap(filename,words_per_query)
	total_queries=total_queries+len(queries_list)

	#checks every query online and substitutes the former phrases for yandex's suggestions, if any
	for i in range (0,len(queries_list)):
		original_query=queries_list[i]
		queries_list[i]=queryenhance.enhanceQuery(queries_list[i]) #makes query ready for Yandex's search
		corrected_queries.append(spellcheck.spellCheck(queries_list[i])) #consult Yandex API for spell checking

		#if Yandex suggested any spell corrections regarding the original query
		if (corrected_queries[i]!=-1):
			yandex_suggestions=yandex_suggestions+1

			#write the corrected phrase in the corrections files
			with open (corrections_file, 'a') as f:
				f.write(str(filename)+'\n'+str(original_query)+'\n'+str(queries_list[i])+'\n'+str(corrected_queries[i])+'\n\n')
			
			#write the corrected phrase in the corrected version of the file that is being spell checked
			with open (filename+".corrected", 'a') as file:
				file.write(corrected_queries[i])
		else:
			#as there were no corrections to be done in the phrase, write it in the in the corrected
			#version of the file that is being spell checked
			original_query=queryenhance.enhanceOriginalQuery(original_query)
			with open (filename+".corrected", 'a') as file:
				file.write(original_query)

time2=time.time()

#write runtime statistics in the corrections file
with open (corrections_file, 'a') as f:
	f.write ("Runtime:"+str(time2-time1))
	f.write('\n')
	f.write ("Queries sent to Yandex:"+str(total_queries))
	f.write('\n')
	f.write ("Corrected Queries:"+str(yandex_suggestions))
