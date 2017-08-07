## THE PROJECT
Currently, the program wraps single or several text files into 8 words blocks, query them to yandex and if it suggests a spell correction (like google's "did you mean"), then the original phrase is subtituted by the given suggestion. Otherwise, the phrase reamins the same in the file.

## USAGE
1. Get an API Key at https://tech.yandex.com/xml/
2. Put your API key inside the brackets  in "API_key" field, at spellchecker.py file. Also put your username right bellow, at "user".
3. From the terminal, run inside the programs's directory: python main.py

## IMPORTANT
Before using the program, always make sure that you have your correct IP set at https://xml.yandex.com/settings/

## NOTES
- According to the API's doc., you need to convert special chars in escape sequences.
However, the result of Yandex's spell check field (<text> in XML) is ASCII (bug?), not UTF8. So, we don't make
the conversion of the queries before sending them simply because it doesn't matter for us.
What this means is: any UTF8 char in your text will be rounded to ASCII (e.g: 	“ and ” turn to ". Also, — will become -).
Unfortunately nothing can be done about it, since it is ans API issue.
- Book pages often contain hyphen (-) linking parts of a single word, when it reaches the end of a line. In cases like this, Yandex usually suggests the whole word binded together(without the hyphen) as a spell correction. Eg: "unfor- tunate" becomes "unfortunate".
If you don't want that, you can easily reprogram it to check if the query sent to Yandex, without the hyphen, provides the same result as Yandex's suggestion for it. If so, you can mantain the former query instead of the suggestion.

## TODO
- [ ] Make a Python Package, with config to the cx and api_key
- [ ] Make a new algorithm for wrapper.py. Currently the program wrap the text into N words phrases and query them to Yandex.
	  However, this is problematic as it doesn't really get the context of the phrases.
	  The idea of the new algorithm is to wrap the text according to the dots contained in the text.


