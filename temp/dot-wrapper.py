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
			for word in line.split():
				print("word: "+word)
				chop_aux.append(word)

				#punctuation in the word =>end of query 
				if (re.search('\W',word) is not None):
					print("pontuacao: "+word)
					#add query to queries list
					chops_list.append(chop_aux)

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

	#!!!TA ENTRANDO COM CHOP_AUX TENDO SO \N
	#add last words of the file to the chop list (as those might still not be there, because there wasn't a final puctuation)
	if (chop_aux):
		print ("tratando dos bufferizado: "+str(chop_aux))
		#removes extra \n that was previously added to the end of the very last line of the file
		chop_aux.pop()
		#!!!E SE NAO TIVER NENHUMA PONTUACAO NO ARQUIVO???????
		#adds last words to chop list
		chop_aux=' '.join(chop_aux)
		chops_list.append(chop_aux)
	
	return chops_list


a=textWrap(sys.argv[1])
#print a

