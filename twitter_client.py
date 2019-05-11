from tweepy import Cursor
from tweepy import API
from tweepy import OAuthHandler
from tweepy import error
import time


def get_twitter_auth():

    # -----------------------------------------------------------
    # Returns correct authentication token for Twitter API access
    # !!  REPLACE VALUES IN key, secret, token FOR API ACCESS  !!
    # -----------------------------------------------------------

    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_secret = ""

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth


def get_twitter_client():

    # -----------------------------------------------------
    # Provides authentication token to Twitter API object
    # Returns Twitter API object for access to Twitter data
    # -----------------------------------------------------

    auth = get_twitter_auth()
    # twitterClient = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    twitterClient = API(auth)
    return twitterClient


def save_data(fileName, statusDump):

    # -----------------------------------------------------
    # Saves tweet data (in /data/) formatted with date/time
    # into the name to maintain individual data sets
    # -----------------------------------------------------

    localtime = time.asctime(time.localtime(time.time())).split(' ')

    listDate = localtime[:3]
    year, date = localtime[4], ''
    for i in [2, 1]:
        date += listDate[i]
    timeNow = localtime[3].replace(':', '')[:-2]

    with open(f'data/{fileName}_{date}{year}_{timeNow}.txt', 'w', encoding="utf-8") as f:
        for line in statusDump:
            f.write(line + '\n')


if __name__ == '__main__':
    api = get_twitter_client()
    tweetDump = []

    try:
        for tweet in Cursor(api.search, q='#food OR #yummy OR #foodporn OR #eeeeeats OR #foodphotography OR #foodgasm',
                            lang='en', tweet_mode='extended').items(2000):
            tweetDump.append(tweet.full_text)
    except error.TweepError as e:
        save_data('tweetDump', tweetDump)
        tweetDump = []
        print(e, '- DATA SAVED, EXITING')
        time.sleep(5)
        exit()

    save_data('tweetDump', tweetDump)
