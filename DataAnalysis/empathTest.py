from empath import Empath
import os,csv
lexicon = Empath()
# Dictionary of all categories from Empath
# cats = lexicons.cats

# Remember to unzip directory 'processedTweets' before running script
	
def getEmotionalCategories():
	# Pre-Built empath categories which match one of our 16 emotional categories
	answer =['ambiguous','anticipation','love','submission','joy','sadness','optimism','neutral','remorse','contempt','disgust','awe','anger','surprise','disapproval','trust','fear','aggression']
	# Need to build the other ones
	# categoriesToMake = ['submission','remorse','contempt','awe','disapproval','ambiguous','neutral']
	# Making categories : could improve seeding choices and amount
	lexicon.create_category("awe",["amazing","wonder","wow"])
	lexicon.create_category("disapproval",["no","different","disagree"])
	lexicon.create_category("submission",["whatever","alright","anything"])
	lexicon.create_category("remorse",["regret","guilt","compassion"])
	lexicon.create_category("contempt",["despise","hate","disrespect"])
	answer.append("awe")
	answer.append("disapproval")
	answer.append("submission")
	answer.append("remorse")
	answer.append("contempt")
	# Not sure if tese count. If you don't include these we have 16 emotions!
	#answer.append(lexicon.create_category("ambiguous",["no","different","disagree"]))
	#answer.append(lexicon.create_category("neutral",["whatever","alright","anything"]))
	return answer

# Removes the emotional categories with scores of 0.0
def removeZeros(analysisDict):
	ans = {}
	for key,value in analysisDict.iteritems():
		if value > 0.0:
			ans[key] = value
	return ans

# Start of Script
emotionalCats = getEmotionalCategories()
for filename in os.listdir("processedTweets"):
	with open('processedTweets/'+filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			row = " ".join(row) # remove commas, and turn token list into string
			try:
				# Analyze text over all set emotional categories normalized by words in each tweet:
				analysis=removeZeros(lexicon.analyze(row, categories=emotionalCats, normalize=True))
				if len(analysis) !=0:
					print(analysis)
			except:
				pass
	break # remove break to keep iterating through directory 'processedTweets'
			
			
