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

#Chops the given file into phrases with "chop_size" words, that will later be sent as queries to yandex,
#returning: list of phrases(strings).
#Attention: chop is done according to spaces, so "would , you come, son?", yields:
#[would],[,],[you],[come,],[son?]. However, those are 4 words only.

import string

def textWrap(file,chop_size):
	chops_list=[]
	chop_aux=[]
	words_count=0

	with open (file, 'r') as document:
		for line in document:
			#for every word
			for word in line.split():
				chop_aux.append(word)
				#chops with no words, like [,], don't account to chop_size
				if (word not in string.punctuation): 
					words_count=words_count+1
				#phrase complete => adds query to queries list
				if (words_count == chop_size): 
					#bind words that form the phrase into a single string
					chop_aux=' '.join(chop_aux)

					#adds space in the end of the phrase so it wont get binded to its neighbours in the final output
					chop_aux=chop_aux+' '

					#add query to queries list
					chops_list.append(chop_aux)

					#reset vars
					del chop_aux
					chop_aux=[]
					words_count=0

			chop_aux.append('\n') #end of line

	#add last words of the file to the chop list (as those altogether didn't reach chop_size)
	if (words_count != 0):
		#removes extra \n that was previously added to the end of the very last line of the file
		chop_aux.pop()

		#adds last words to chop list
		chop_aux=' '.join(chop_aux)
		chops_list.append(chop_aux)
	
	return chops_list

