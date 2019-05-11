
TwitterBot Project

Matt Verity
May 10, 2019
Version: 1.0

----------------------------------

General Usage:

	- Use foodpuller.py to parse any additional cuisines you want.
	- Clean the parsed data and save to a csv.
	- Pull Twitter data using Twitter API/Tweepy Cursor.
	- Check words in each tweet against a database of unique words, each with a matching cuisine.

----------------------------------

TO DO:

	- More/better keywords
	- Improved non-strict search pattern
	- Increased # of tweets in database

	- Replace keyword search with NLP/NLTK for better results?

----------------------------------

Required modules:
	- tweepy
	- beautifulsoup4
	- requests
	- matplotlib
	- numpy

----------------------------------


Welcome to my twitter food trend tracker, TwitterBot.

It is a collection of python scripts that:


trend_checker.py:

	- To add/remove cuisine types, add or remove items from CUISINES constant at the top of the script (appropriate .csv file must exist).

	- Contains a simple counter object (foodCounter) that increments each individual cuisine in it's .cuisineCount attribute if/when a matching item is found.

	- Contains functionality to open csv files inside /dishes/csv/ individually and store the data, based on current CUISINES.

	- Allows the user to check a list of tweets (the content each as a string) against the current keywords contained in the csv files.

	- Creates a simple bar graph to display total number of matching occurances between keywords.

	- Also prints out the following information to the console:
		- Tweets that did not contain any keywords for manual parsing and csv additions.
		- Words triggered, and number of times triggered
		- Graphed data in 'Country: <occurances>' format

	- Contains a generator (word_gen(numWords)) that yields random keywords for given number of words (numWords) for testing purposes.


twitter_client.py:

	- Contains the functions to gain authentication to Twitter API, along with unique KEYS as variables (must be input if not present) to connect to API:
		- consumer_key
		- consumer_secret
		- access_token
		- access_secret

	- Contains a function that returns a Twitter API object (get_twitter_client).

	- Use this API object for iteration or pagination through tweet data via Tweepy's Cursor object (ex.):
		
		for page in tweepy.Cursor(api.user_timeline).pages(10):
			process_page(page)

		for status in tweepy.Cursor(api.search, q='<search query>', lang='en').items(100):
			process_status(status.text)

	- Also contains functionality to save the retrieved twitter data in a unique text file formatted with date/time.


foodpuller.py:

	- A web scraper that pulls dish names off of Wikipedia pages
		- Must be slightly formatted between uses, as Wikipedia HTML differs between pages

	- Contains functionality that cleans and writes the scraped information into a csv file of unique keywords.