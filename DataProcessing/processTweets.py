import csv
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))



with open('parklandShooting.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
    	try:
			tweet = row[4]
			word_tokens = word_tokenize(row[4])
			filtered_sentence = [w for w in word_tokens if "/" not in w]
			filtered_sentence = [w for w in filtered_sentence if "\\x" not in w]		
			filtered_sentence = [w for w in filtered_sentence if  w not in  stop_words]		
			print(filtered_sentence)
			print("-----------")
    	except:
    		continue
