# Twitter Food Trend Tracker

This is a collection of python scripts that creates a list of unique keywords based on data pulled from 'List of <cuisine> Dishes' Wikipedia pages, stored in a `<cuisine name>: [list of keywords]` style dictionary, which is checked against a list of Tweets aquired via access to Twitter's API. The resulting matches are displayed on a simple bar graph based on the amount of mentions for any specific cuisine.

## Getting Started

- Use `foodpuller.py` to parse any additional food keywords you want.
- Clean the parsed data and save to a csv using the same script.
- Pull and save Twitter data using Twitter API/Tweepy Cursor using `twitter_client.py`.
- Use `trend_checker.py` to check saved Twitter data against stored keywords.

### Prerequisites

Aside from Python 3, this set of scripts utilizes the following external libraries:  

```
tweepy
beautifulsoup4
requests
numpy
matplotlib
```

### Installing

These can be obtained via the `pip install` command, used in CMD/Terminal:

```
pip install <module>
```

For example:

```
pip install tweepy
pip install beautifulsoup4
etc.
```

Numpy is a dependancy of matplotlib, and should be installed first.


## To-Do:  


- More/better keywords
- Improved non-strict search pattern
- Increased # of tweets in database
- Replace keyword search with NLP/NLTK for better results, maybe?


## Additional information:

##### `trend_checker.py`:

- To add/remove cuisine types, add or remove items from CUISINES constant at the top of the script (appropriate .csv file must exist).
- Contains a simple counter object (foodCounter) that increments each individual cuisine in it's .cuisineCount attribute if/when a matching item is found.
- Contains functionality to open csv files inside /dishes/csv/ individually and store the data, based on current CUISINES.
- Allows the user to check a list of tweets (the content each as a string) against the current keywords contained in the csv files.
- Creates a simple bar graph to display total number of matching occurances between keywords
- Also prints out the following information to the console:
    - Tweets that did not contain any keywords for manual parsing and csv additions.
    - Words triggered, and number of times triggered
    - Graphed data in 'Country: <occurances>' format
- Contains a generator (word_gen(numWords)) that yields random keywords for given number of words (numWords) for testing purposes.


##### `twitter_client.py`:

- Contains the functions to gain authentication to Twitter API, along with unique KEYS as variables (must be input if not present) to connect to API:
	- consumer_key
	- consumer_secret
	- access_token
	- access_secret
- Contains a function that returns a Twitter API object (get_twitter_client).
- Also contains functionality to save the retrieved twitter data in a unique text file formatted with date/time.
- Use this API object for iteration or pagination through tweet data via Tweepy's Cursor object:
	```
    for page in tweepy.Cursor(api.user_timeline).pages(10):
		process_page(page)  
		
	for status in tweepy.Cursor(api.search, q='<search query>', lang='en').items(100):
		process_status(status.text)
    ```  


##### `foodpuller.py`:

- A web scraper that pulls dish names off of Wikipedia pages
	- Must be slightly formatted between uses, as Wikipedia HTML differs between pages
- Contains functionality that cleans and writes the scraped information into a csv file of unique keywords.
- Some manual cleaning of data is still required (generic words, etc.), but the amount is minimal.


## Authors

* **Matt Verity** - [mdverity](https://github.com/mdverity)  


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
