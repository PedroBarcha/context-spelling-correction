## THE PROJECT
Currently, the program wraps the text into 5 words blocks, query them to google and print whether they produced a "did you mean" (and if so, what was it). However it still doesn't subtitute the given suggestion for the original excerpt. In the middle of the project I found out that google provides only 100 queries per day which isn't quite enough for me (if you need more than this you need to pay A LOT) and, hence, I've been looking for free alternative search engines, leaving this project in standby for now.

## USAGE
1. Get an API Key at https://console.developers.google.com/apis/credentials
2. Put your key inside the brackets  in "API_key" field, at spellchecker.py file
3. From the terminal, run inside the programs's directory: python main.py

## NOTES
- According to the API's doc. , you need to convert special chars in escape sequences.
However, exlusively the result of Yandex's spell check field is ASCII (bug?), not UTF8. So, we don't make
the conversion simply because it doesn't matter for us.
What this means is: any UTF8 char in your text will be rounded to ASCII (e.g: 	“ and ” turn to ". Also, — will become -).
Unfortunately nothing can be done about it, since it is ans API issue
- Book pages often contain hyphen (-) linking parts of a single word, when it reaches the end of the line. When the program
reach a case like this, Yandex usually suggest the liked together (without the hyphen). If you don't want that, you can easily
reprogram it to check if the query sent to Yandex, without the hyphen, provides the same result as Yandex's suggestion for it. If so,
you can mantain the former query instead of the suggestion.

## TODO
- [ ] Substituter: substitute google's suggestions for the original phrases
- [ ] Make a Python Package, with config to the cx and api_key

