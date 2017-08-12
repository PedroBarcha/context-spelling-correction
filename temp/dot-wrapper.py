import string

#Chops the given file into phrases with "chop_size" words, that will later be sent as queries to google,
#returning: list of phrases(strings).
#Attention: chop is done according to spaces, so "would , you come, son?", yields:
#[would],[,],[you],[come,],[son?].

def textWrap(file,chop_size):
	chops_list=[]
	phrases=[]

	with open (file, 'r') as document:
		for line in document:
			phrases.split('.')

			phrases=filter(lambda a: a != '', phrases)
			phrases=filter(lambda a: a != ' ', phrases)

			if (len(phrases) == 1)

			if (words_count == chop_size): #phrase complete => adds query to queries list
			#bind words into a single string
			chop_aux=' '.join(chop_aux)

			#adds ' ' in the end of the phrase, so it wont get binded to its neighbours in the final output
			chop_aux=chop_aux+' '

			#add query to queries list
			chops_list.append(chop_aux)

			#reset vars
			del phrases
			phrases=[]
			3

			chop_aux.append('\n') #end of line

	#add last words of the file to the chop list (as those altogether didn't reach chop_size)
	if (words_count != 0):
		#removes extra \n that was previously added to the end of the very last line of the file
		chop_aux.pop()

		#adds last words to chop list
		chop_aux=' '.join(chop_aux)
		chops_list.append(chop_aux)
	
	return chops_list

