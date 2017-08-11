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
#NOTE: according to Yandex's API's doc., you need to convert special chars into escape sequences.
#However, the result of Yandex's spell check field (<text> in XML) is ASCII (bug?), not UTF8.. So, we don't make
#the conversion simply because it doesn't matter for us.
#What this means is: any UTF8 char in your text will be rounded to ASCII if a suggestion is made by Yandex.
#Unfortunately nothing can be done about it, since it is an API issue.

import re

#enhance the query in order to adequate it to yandex's search
def enhanceQuery(query):
	query=query.replace("\n ",'\n') #sometines '\n'+space is generated due to the spaces added by the wrapper
	query=query.replace(" ",'+') #backspaces need to be replaced by +
	query=query.replace('\n',';~;') #yandex api doesn't support \n, so we have to hide it (using a set of chars that is unlikely to appear in any text)
	query=parenthesisHide(query) #hide query's original parenthesis
	return query

#enhance yandex's suggestion in order to replace it in the original text
def enhanceSuggestion(suggestion):
	suggestion=parenthesisTrim(suggestion) #trim stupid yandex's suggestion parenthesis
	suggestion=parenthesisUnhide(suggestion) #unhide query's original parenthesis
	suggestion=suggestion.replace(';~;','\n') #put former newlines markers back
	return suggestion

#enhance the query that dind't receive any Yandex's suggestion
def enhanceOriginalQuery(query):
	query=query.replace("\n ",'\n') #sometines '\n'+space is generated due to the spaces added by the wrapper
	return query

#sometimes yandex returns its suggestion inside parenthesis (not sure why tho), so we need to remove them
def parenthesisTrim(text):
	text = re.sub('[()]', '', text)
	return text

#we need to hide query's parenthesis so we don't confuse them with those yielded by Yandex's suggestions, as mentioned above.
#we do that by replacing them with a set of chars that is unlikely to appear in any text
def parenthesisHide(text):
	text=text.replace('(','~;~')
	text=text.replace(')',';0;')
	return text

#unhide query's former parenthesis
def parenthesisUnhide(text):
	text=text.replace('~;~','(')
	text=text.replace(';0;',')')
	return text

