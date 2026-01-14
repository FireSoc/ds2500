'''
    DS2500
    Spring 2025
    Sample code from class -- web scraping and sentiment analysis

    Our goals today:
    - try the sentiment analysis algorithm
    - scrape a simple web page https://khoury.northeastern.edu/home/laney/simple.html
    - find a web page with Bear Season 2 descriptions, scrape it, and get sentiment over time

    Better than basic sentiment algorithm:
    - add/subtract more or less than +1 or =1
    - scale exponentially
    - add/sdubtract more for emphasis words (very, awfully, quite, wicked, etc.)
    - context for the source (is it a serious journal, or casual text?)
    - don't ignore ALL punctuation
    - count emojis/emoticons
    - slang?
    - n-grams, look at phrases and not just words on their own

'''

from bs4 import BeautifulSoup
from textblob import TextBlob
import wordcloud as wc
from urllib.request import urlopen
import matplotlib.pyplot as plt

START_SEASON = 1
END_SEASON = 3
SIMPLE_URL = "https://khoury.northeastern.edu/home/laney/simple.html"
BASE_URL = "https://en.wikipedia.org/wiki/The_Bear_season_"

def season_sents(base_url, classname, season_no):
    ''' given a base URL, a class to look for,
        and a season number to append to the URL,
        create and return a list of sentiment scores per episode
    '''
    url = f"{base_url}{season_no}"
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), "html.parser")
    descriptions = bs.find_all("div", {"class": classname})

    sents = []
    for desc in descriptions:
        blob = TextBlob(desc.get_text())
        sents.append(blob.sentiment.polarity)
    return sents

def sentiment_practice():
    ''' prompt the user for strings and print out
        the sentiment score, just for funsies,
        don't return anything
    '''
    str = ""
    while str != "-1":
        str = input("What text to try?\n")
        blob = TextBlob(str)
        print(blob.sentiment.polarity)

def scrape_practice(url):
    ''' given a url, open the page and print
        various HTML info, just for funsies,
        don't return anything
    '''
    html = urlopen("https://khoury.northeastern.edu/home/laney/simple.html")
    bs = BeautifulSoup(html.read(), "html.parser")
    print(f"Here is the h1 header i found: {bs.h1}\n")
    print("Here are all the links I found <a href='...'>")
    links = bs.find_all({"a": "href"})
    for link in links:
        print(link)

def plot_sentiments(all_sents):
    ''' given a list of sentiment scores,
        plot them over time
    '''
    plt.plot(all_sents, color = "magenta")
    plt.title("The Bear Vibes (Seasons 1-3)")
    plt.xlabel("Episode Number")
    plt.ylabel("Sentiment Polarity Score (-1 to +1)")
    plt.show()
def main():
    # start with sentiment analysis built into the python library
    sentiment_practice()

    # Now a little web scraping, just for fun
    scrape_practice(SIMPLE_URL)


    # combine sentiment analysis skills with webscraping skills
    # to find out what is going to happen on the bear
    # descriptions of episodes are in: <div class="shortSummaryText"...>
    all_sents = []
    for i in range(START_SEASON, END_SEASON + 1):
        all_sents += season_sents(BASE_URL, "shortSummaryText", i)

    # plot the list of sentiment scores
    plot_sentiments(all_sents)


if __name__ == "__main__":
    main()