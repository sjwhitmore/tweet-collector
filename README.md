Tweet Collector

Initial stages -- just collects tweets pertaining to a certain topic and stores them in a MongoDB.

Next steps --  do some cool analysis.

Run by entering "node testnodetwitter.js" on the command line.

Preprocessing ideas (some taken from http://www.cs.columbia.edu/~julia/papers/Agarwaletal11.pdf):
1. Remove words beginning with "@"" (mentions) and URLs, delete "#" from hashtags
2. Use emoticon dict to link emoticons with various levels of sentiment (http://en.wikipedia.org/wiki/List of emoticons)
3. Use abbreviation dict to replace words like "lol" and "gr8" with their written out versions (http://noslang.com)
4. Filter out "stop words" (those commonly ignored by search engines) (http://www.webconfs.com/stop-words.php)
4. Replace words with repeating character sequences with 3 charactes: i.e. "coooooool" to "coool" to standardize yet also retain emphasis.
5. Link negation words with the words they follow... i.e "isn't good" should mean that "good" is replaced by "NOT_good"
6. run the 