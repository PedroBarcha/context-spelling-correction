import spellchecker
import queryenhancer
import wrapper
import glob
import time
import sys  

#set unicode as default encoding
reload(sys)  
sys.setdefaultencoding('utf8')

time1=time.time()
total_queries=0
yandex_suggestions=0
errors_file="/home/banshee/Pictures/ocr-images/Database/yandex-spell-check/errors-5"


##(rec)#TODO####
#put this variable in future pack's config
words_per_query=5 #text will be chopped into block with words_per_query words

#for every file yielded by the OCR process
#wrapper turns them into queries for google
for filename in glob.glob("/home/banshee/Pictures/ocr-images/Database/300dpi/tesseract/ocr/*"):

	queries_list=wrapper.textWrap(filename,words_per_query)

	total_queries=total_queries+len(queries_list)

	corrected_queries=[]
	#checks every query online and substitutes the former phrases for yandex's suggestions 
	for i in range (0,len(queries_list)):
		original_query=queries_list[i]
		queries_list[i]=queryenhancer.enhanceQuery(queries_list[i]) #makes query ready for Yandex's search
		corrected_queries.append(spellchecker.spellCheck(queries_list[i]))

		#if Yandex suggested something regarding the original query
		if (corrected_queries[i]!=-1):

			with open (errors_file, 'a') as f:
				f.write(filename)
				f.write('\n')
				f.write(original_query)
				f.write("\n")
				f.write(queries_list[i])
				f.write('\n')
				f.write(corrected_queries[i])
				f.write("\n\n")
			
			yandex_suggestions=yandex_suggestions+1

			with open (filename+".corrected", 'a') as file:
				file.write(corrected_queries[i])
		else:
			original_query=queryenhancer.enhanceOriginalQuery(original_query)
			with open (filename+".corrected", 'a') as file:
				file.write(original_query)


time2=time.time()

with open (errors_file, 'a') as f:

	f.write ("tempo total:"+str(time2-time1))
	f.write('\n')
	f.write ("numero de queries:"+str(total_queries))
	f.write('\n')
	f.write ("numero de queries corrigidas:"+str(yandex_suggestions))
