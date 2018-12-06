## THE PROJECT
Currently, the program wraps single or several text files into 8 words blocks, query them to yandex and if it suggests a spell correction (like google's "did you mean"), then the original phrase is subtituted by the given suggestion. Otherwise, the phrase reamins the same in the file.

## DEPENDECIES
All you need is python 2 and its standard libraries.

## SET UP
1. Get an API Key at https://tech.yandex.com/xml/ ;
2. In order to grant access to 10.000 quries/day, confirm your cel number at https://passport.yandex.com/profile ;
3. Run ``` git clone https://github.com/PedroBarcha/Context-Spelling-Correction.git``` to clone the repo;
4. From the terminal, navigate to the repo directory and run ``` python config.py ``` , in order to set you API key and username.

## USAGE
From the terminal, run inside the repo's directory: ``` python correction.py PATH_TO_THE_FILE ``` .
If you wish to correct several files, stored in the same directory, use instead: ``` python correction.py PATH_TO_THE_DIR/* ``` .

## ***IMPORTANT***
Before running the program, always make sure that you have your correct IP set at https://xml.yandex.com/settings/

## OUTPUT
- For every file specified in the input, a file with the same name and extension ".corrected" will be generated.
- A single file named "yandex_suggestions.txt" is produced, containing all of Yandex's suggestions for you file(s)
and also runtime statistics at the end of it.

## NOTES
- According to the API's doc., you need to convert special chars into escape sequences.
However, the result of Yandex's spell check field (<text> in XML) is ASCII (bug?), not UTF8. So, we don't make
the conversion of the queries before sending them simply because it doesn't matter for us.
What this means is: any UTF8 char in your text will be rounded to ASCII if a suggestion is made by Yandex.
(e.g: “ and ” turn to ". Also, — will become -).
Unfortunately nothing can be done about it, since it is an API issue.
- Book pages often contain hyphen (-) linking parts of a single word, when it reaches the end of a line. In cases like this, Yandex usually suggests the whole word binded together(without the hyphen) as a spell correction. Eg: "unfor- tunate" becomes "unfortunate".
If you don't want that, you can easily reprogram it to check if the query sent to Yandex, without the hyphen, provides the same result as Yandex's suggestion for it. If so, you can mantain the former query instead of the suggestion.

## TODO
- [ ] Make a new algorithm for wrapper.py. Currently the program wrap the text into N words phrases and query them to Yandex.
	  However, this is problematic as it doesn't really get the context of the phrases.
	  The idea of the new algorithm is to wrap the text according to the dots contained in the text.
- [ ] After the above is done, make a setup.py and publish the program on PyPi


