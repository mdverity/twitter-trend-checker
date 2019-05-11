import csv
import random
import matplotlib.pyplot as plt
import numpy as np


# ----------------------------------------------------------
# Constant for the cuisines with current csv files to check
# 'thai' has been throwing many false positives (
# ----------------------------------------------------------

CUISINES = ['african', 'american', 'chinese', 'indian', 'indonesian',
            'italian', 'japanese', 'mexican', 'spanish']
# CUISINES.append('thai')


def take_first(elem):
    return elem[1]


class FoodCounter(object):
    """
    A simple counter object that:

        - Populates a dictionary (self.cuisineCount) with {<cuisine type>: 0,
                                                           <cuisine type>: 0,
                                                           <cuisine type>: 0, etc.}

        - Has an increment function to add one to value of given cuisine.

        - toString prints formatted values of self.cuisines
    """

    def __init__(self):
        self.cuisineCount = {}
        self.containedWords = []

    def __str__(self):
        toString = ''
        for i, j in self.cuisineCount.items():
            toString += f'{i.title()}: {j}\n'

        return toString

    def add_word(self, word):
        self.containedWords.append(word)

    def contained_word_count(self):
        r = []
        for x in set(self.containedWords):
            r.append((self.containedWords.count(x), x))
        r.sort(key=take_first)
        return r

    def populate_cuisines(self):
        for country in CUISINES:
            self.cuisineCount[country] = 0

    def inc_cuisine(self, country):
        self.cuisineCount[country] += 1


def get_file_data():

    # -------------------------------------
    # Pulls data from individual csv files
    # Returns list with items as dictionary
    # -------------------------------------

    fileData = {}

    for country in CUISINES:
        fileData[country] = []
        with open(f'dishes/csv/{country}.csv') as fd:
            temp = csv.reader(fd, delimiter=',')
            for line in temp:
                fileData[country] += line

    return fileData


def check_string(inputString, cuisineDict, strict=True):

    # ----------------------------------------------------
    # Checks for a match between an input string and words
    # inside each cuisine, then increments correct counter
    # ----------------------------------------------------
    containedWord = False

    if strict:
        for word in inputString.split(' '):
            for cuisine in cuisineDict:
                if word.lower() in cuisineDict[cuisine]:
                    foodCounter.inc_cuisine(cuisine)
                    foodCounter.add_word(word.lower())
                    containedWord = True
    else:
        for cuisine in cuisineDict:
            for foodItem in cuisineDict[cuisine]:
                if foodItem in inputString.lower():
                    foodCounter.inc_cuisine(cuisine)
                    foodCounter.add_word(foodItem)
                    containedWord = True

    if not containedWord:
        print(inputString)


def word_gen(numWords):

    # -------------------------------------------------------
    # Used for testing purposes, creates a fake data set
    # Generates a set number of words from foodData in a list
    # Adjust the initial randint rolls to change test weights
    # -------------------------------------------------------

    for _ in range(numWords):
        temp = random.randint(1, 100)
        if temp <= 8:
            yield random.choice(foodData['american'])
        elif temp <= 13:
            yield random.choice(foodData['chinese'])
        elif temp <= 18:
            yield random.choice(foodData['mexican'])
        else:
            yield random.choice(foodData[random.choice(list(foodData.keys()))])


def plot_data(counter):

    # -------------------------------------------------
    # Plots data on a bar graph with appropriate labels
    # -------------------------------------------------

    objects = list(counter.cuisineCount.keys())
    y_pos = np.arange(len(objects))
    performance = list(counter.cuisineCount.values())

    plt.bar(y_pos, performance, align='center')
    plt.xticks(y_pos, objects)
    plt.ylabel('Mentions')
    plt.title('Current Food Trends\nby Keyword\n')

    plt.show()


if __name__ == '__main__':
    foodData = get_file_data()
    foodCounter = FoodCounter()
    foodCounter.populate_cuisines()

    # testStrings = word_gen(500)

    with open('data/tweetDump_11May2019_1046.txt', 'r', encoding="utf-8") as f:
        tweetDump = f.readlines()

    for tweet in tweetDump:
        if len(tweet) >= 3:
            check_string(tweet, foodData, strict=False)

    for item in sorted(foodCounter.contained_word_count()):
        print(item)

    print(foodCounter)
    plot_data(foodCounter)
