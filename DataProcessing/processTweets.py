import csv
import preprocessor as p
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))
punctuation = [',','.','(',')','//',':',';','<','>','?','!','@']



with open('qorlandonightclubshooting.csv') as csv_file:
	with open('processedOrlandoShooting.csv', mode='w') as inFile:
		fw = csv.writer(inFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_reader = csv.reader(csv_file, delimiter=';')
		line_count = 0
		for row in csv_reader:
			try:
				tweet = p.clean(row[4])			
				word_tokens = word_tokenize(tweet)			
				filtered_sentence = [w for w in word_tokens if w not in stop_words]
				filtered_sentence = [w for w in filtered_sentence if "/" not in w]
				filtered_sentence = [w for w in filtered_sentence if "\\" not in w]
				filtered_sentence = [w for w in filtered_sentence if w not in punctuation]	
				ans = []
				for tk in word_tokens:
					if "http" in tk or "https" in tk:
						break
					ans.append(tk)
						
				fw.writerow(ans)
				print("Tweet processed...")
			except:
				continue

