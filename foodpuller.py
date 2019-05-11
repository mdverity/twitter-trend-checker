from bs4 import BeautifulSoup
import requests


CUISINES = ['african', 'american', 'chinese', 'indian', 'indonesian',
            'italian', 'japanese', 'mexican', 'spanish', 'thai']


def scrape(site):

    # -----------------------------------------------------------------
    # Scrapes a given 'List of <> Dishes' Wikipedia site for food names
    # Needs to be improved, but Wikipedia HTML varies between each page
    #    - Currently functioning on most table-based page formats -
    # -----------------------------------------------------------------

    source = requests.get(site).text
    soup = BeautifulSoup(source, 'lxml')
    foodList = []

    rawSoup = soup.find('div', id='bodyContent')

    for section in rawSoup.find_all('div', class_='mw-parser-output'):
        for item in section.find_all('table', class_='wikitable sortable')[:-1]:
            for i in item.find_all('tr'):
                for j in i.find_all('td')[:1]:
                    print(j.text.strip())
                    foodList.append(j.text)

    return foodList


def dupe_checker(country):

    # --------------------------------------------
    # Checks for duplicate items between every key
    # inside the dictionary, and prints duplicates
    # --------------------------------------------

    from trend_checker import get_file_data

    fileData = get_file_data()

    for item in fileData[country]:
        for key, values in fileData.items():
            for val in values:
                if val == item and key != country:
                    print(key, val)


def save_raw_data(fileName, foodList):
    with open(f'dishes/{fileName}.txt', 'w') as f:
        for line in foodList:
            f.write(line + '\n')


def replace_bad_chars(stringInput):

    # ---------------------------------------------------
    # Replaces any 'bad' characters inside a given string
    # Called inside of data_cleaner function, for clarity
    # ---------------------------------------------------

    badChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', ',', '.', '/', '\\']
    newString = ''

    for letter in stringInput:
        letter = (letter.replace(letter, '') if letter in badChars else letter)
        newString += letter

    return newString


def data_cleaner(fileName):

    # -----------------------------------------------------
    # 'Cleans' the data, removing any bad characters, 'or',
    # 'and', Null, and any words shorter than 2 characters.
    # -----------------------------------------------------

    temp = ''

    with open(f'dishes/{fileName}.txt', 'r') as f:
        for i in f.readlines():
            temp += i.strip().lower() + ' '

    concise_data = list(set(temp.split(' ')))

    with open(f'dishes/csv/{fileName}.csv', 'w', encoding="utf-8") as f:
        for item in concise_data:
            if len(item) >= 3 and item not in ["and", "or"]:
                f.write(f'{replace_bad_chars(item)},')


if __name__ == '__main__':
    foods = scrape('https://en.wikipedia.org/wiki/List_of_Indonesian_dishes')
    save_raw_data('indonesian', foods)
    data_cleaner('indonesian')
