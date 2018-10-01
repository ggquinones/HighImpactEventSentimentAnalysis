
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

#---------Download list of stopwords----------
nltk.download('stopwords')
nltk.download('punkt')

#---------Set Language to english----------
stopWords = set(stopwords.words('english')) 

#---------Read the data as a pd dataframe and extract only the text column----------
data = pd.read_csv("parklandShooting.csv")
print(data)
tweets = data[['text']]

#---------Stringify the tweets----------
tokenData = word_tokenize(str(tweets))

tweet_tokens = [] 

#---------Iterate through the tweets to remove stopwords and '/' characters----------
tweet_tokens = [w for w in tokenData if not w in stopWords]
#tweet_tokens = [w for w in tweet_tokens if "/" not in w ]
#tweet_tokens = [w for w in tweet_tokens if "\\" not in w ]

print(tweet_tokens)

#---------Export the tokenized words as a csv----------
#result = pd.DataFrame(tweet_tokens)
#result.to_csv("Sutherland_tokenized.csv", index=False)


