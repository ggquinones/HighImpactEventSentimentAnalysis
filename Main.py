import sys
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main():

	def printTweet(descr, t):
		print(descr)
		print("Username: %s" % t.username)
		print("Retweets: %d" % t.retweets)
		print("Text: %s" % t.text)
		print("Mentions: %s" % t.mentions)
		print("Hashtags: %s\n" % t.hashtags)

	# Example 1 - Get tweets by username
	#tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
	#tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	#printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)

	# Example 2 - Get tweets by query search
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('sandy hook').setSince("2012-12-12").setUntil("2012-12-19").setMaxTweets(100)
	tweets = got.manager.TweetManager.getTweets(tweetCriteria)
	for tweet in tweets:
		printTweet("### Get tweets by query search [sandy hook]", tweet)

	# Example 3 - Get tweets by username and bound dates
	#tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	#tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	#printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)

if __name__ == '__main__':
	main()