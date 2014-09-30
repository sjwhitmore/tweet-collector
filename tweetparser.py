# For analyzing tweets!

import re
import string
import pickle

#Get slang dictionary
slangdict = pickle.load( open( "slangdict.p", "rb" ) )

# Get list of tweets
# TODO: connect to mongodb collection of tweets

# Assume going through tweet by tweet:
# Step 1: Remove @mentions, urls, hashtag symbols and replace slang (for now! Simple parser!)
tweet = "@Apple iPhone 5 - 32GB - Black  Unlocked ICU Smartphone A1428 http://t.co/InExq45Hqt So I now haven't got an #iPhone or #iPad charger, well g2g done Chloe"
#remove punctuation: tweet_text = tweet.translate(string.maketrans("",""), string.punctuation)
words = tweet.split(" ")
for w in words:
	w2 = w.lower()
	if "http" in w2:
		words.remove(w)
	try:
		if w2[0] == "#":
			index = words.index(w)
			words[index] = words[index][1:]
		if w2[0] == '@':
			words.remove(w)
	except IndexError:
		words.remove(w)
	if w2 in slangdict:
		index = words.index(w)
		words[index] = slangdict[w2]

			
print words