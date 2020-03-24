import tweepy, re
from textblob import TextBlob
import matplotlib.pyplot as plt
import matplotlib
# plt.switch_backend('qt')
# matplotlib.use("qt5agg")
matplotlib.use('TKAgg')


class SentimentAnalysis:

    def __init__(self, tweet_name, no_of_terms):
        self.search_term = tweet_name
        self.no_of_terms = no_of_terms
        self.tweets = []
        self.tweetText = []

    def DownloadData(self):
        error = 0
        # authenticating
        consumerKey = '3jdMRJTAl0tLYvU3x4aggUKIV'
        consumerSecret = '49oMn4tnwWe4ojbr2GaT90w3pWRgvE7THZQw4LHZVTDI4HOQ6Q'
        accessToken = '1039892146071973888-djA3Gm2owDL9yNIGCXYd6N13cEGnxX'
        accessTokenSecret = 'osQBhnEf39Lm3Cok3UhZoIs5ejvs437KcCPG3iQusEJ7a'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        # input for term to be searched and how many tweets to search
        searchTerm = self.search_term  # input("Enter Keyword/Tag to search about: ")
        NoOfTerms = self.no_of_terms  # int(input("Enter how many tweets to search: "))

        # searching for tweets
        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang="en").items(NoOfTerms)

        # creating some variables to store info
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0

        # iterating through tweets fetched
        for tweet in self.tweets:
            # Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            # print (tweet.text.translate(non_bmp_map))    #print tweet's text
            analysis = TextBlob(tweet.text)
            # print(analysis.sentiment)  # print tweet's polarity
            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later

            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                wpositive += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                spositive += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                wnegative += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative += 1


        # finding average of how people are reacting
        positive = self.percentage(positive, NoOfTerms)
        wpositive = self.percentage(wpositive, NoOfTerms)
        spositive = self.percentage(spositive, NoOfTerms)
        negative = self.percentage(negative, NoOfTerms)
        wnegative = self.percentage(wnegative, NoOfTerms)
        snegative = self.percentage(snegative, NoOfTerms)
        neutral = self.percentage(neutral, NoOfTerms)
        polarity = polarity / NoOfTerms

        #data = {'positive': positive, 'wpositive': wpositive, 'spositive': spositive, 'negative':negative, 'wnegative': wnegative,
        #        'snegative': snegative, 'neutral': neutral}
        # finding average reaction
        '''
        # printing out data
        print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
        print()
        print("General Report: ")
        
        if (polarity == 0):
            print("Neutral")
        elif (polarity > 0 and polarity <= 0.3):
            print("Weakly Positive")
        elif (polarity > 0.3 and polarity <= 0.6):
            print("Positive")
        elif (polarity > 0.6 and polarity <= 1):
            print("Strongly Positive")
        elif (polarity > -0.3 and polarity <= 0):
            print("Weakly Negative")
        elif (polarity > -0.6 and polarity <= -0.3):
            print("Negative")
        elif (polarity > -1 and polarity <= -0.6):
            print("Strongly Negative")

        print()
        print("Detailed Report: ")
        print(str(positive) + "% people thought it was positive")
        print(str(wpositive) + "% people thought it was weakly positive")
        print(str(spositive) + "% people thought it was strongly positive")
        print(str(negative) + "% people thought it was negative")
        print(str(wnegative) + "% people thought it was weakly negative")
        print(str(snegative) + "% people thought it was strongly negative")
        print(str(neutral) + "% people thought it was neutral")
        '''

        try:
            pass;
            # self.plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm,
            #              NoOfTerms)

        except:
            error = 1

        finally:
            return polarity, error, positive, wpositive, spositive, negative, wnegative, snegative, neutral

    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return ' '.join(re.sub("(@[A-Za-z0-9_]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    # (\w+:\/\/\S+) remove link
    # re.sub(r'http:\/\/.*[\r\n]*', '', tweet) - removing link
    # \t = skip over spaces and tabs*
    # Keep in mind that you should not provide any blank space else it will consider it as a
    # pattern and also tries to to match the pattern having some blank space in it.

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    def plotPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm,
                     noOfSearchTerms):
        labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]',
                  'Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]',
                  'Strongly Negative [' + str(snegative) + '%]']
        sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
        colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

        # plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
        # mpld3.enable_notebook()
        # mpld3.show()


def tweet(tweet_name, no_of_terms):
    sa = SentimentAnalysis(tweet_name, no_of_terms)
    return sa.DownloadData()
