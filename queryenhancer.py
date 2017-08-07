import re

#NOTE: according to the API's doc. , you need to convert special chars in escape sequences.
#However, exlusively the result of Yandex's spell check field is ASCII (bug?), not UTF8. So, we don't make
#the conversion simply because it doesn't matter for us.
#What this means is: any UTF8 char in your text will be rounded to ASCII.
#Unfortunately nothing can be done about it, since it is ans API issue

#enhance the query in order to adequate it to yandex's search
def enhanceQuery(query):
	query=query.replace("\n ",'\n') #sometines '\n'+space is generated due to the spaces added by the wrapper
	query=query.replace(" ",'+') #backspaces need to be replaced by +
	query=query.replace('\n',';~;') #yandex api doesn't support \n, so we have to hide it (using a set of chars that is unlikely to appear in any text)
	query=parenthesisHide(query) #hide query's original parenthesis
	return query

#enhance yande's suggestion in order to replace it in the original text
def enhanceSuggestion(suggestion):
	suggestion=parenthesisTrim(suggestion) #trim stupid yandex's suggestion parenthesis
	suggestion=parenthesisUnhide(suggestion) #unhide query's original parenthesis
	suggestion=suggestion.replace(';~;','\n') #put forme newlines markers back
	return suggestion

def enhanceOriginalQuery(query):
	query=query.replace("\n ",'\n') #sometines '\n'+space is generated due to the spaces added by the wrapper
	return query

#sometimes yandex returns its suggestion inside parenthesis (not sure why tho), so we need to remove them
def parenthesisTrim(text):
	text = re.sub('[()]', '', text)
	return text

#we need to hide query's parenthesis so we don't confuse them with tose yielded by Yandex's suggestions, as mentioned above.
#we do that by replacing them with a set of chars that in unlikely to appear in any text
def parenthesisHide(text):
	text=text.replace('(','~;~')
	text=text.replace(')',';0;')
	return text

#unhide query's former parenthesis
def parenthesisUnhide(text):
	text=text.replace('~;~','(')
	text=text.replace(';0;',')')
	return text

