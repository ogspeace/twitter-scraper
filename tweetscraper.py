# script which gathers tweets about certain texts.
# Ogs Ablazo
import csv, tweepy, os

class Conn:
    '''
        twitter credentials class
    '''
    def __init__(self, *args):
        self.ck = ''    #consumer key
        self.cs = ''    #consumer secret
        self.at = ''    #access token
        self.ats = ''   #access token secret
    
    def tweep_creds(self):
        auth = tweepy.OAuthHandler(self.ck, self.cs)
        auth.set_access_token(self.at, self.ats)
        return tweepy.API(auth)

#initialize api w/ twitter api credentials object
api = Conn().tweep_creds()

def gather_tweets(query_word,twt_lmt):
    counter = 0
    for tweet in list(tweepy.Cursor(api.search, q=query_word).items(twt_lmt)):
        csvWriter.writerow([tweet.text, tweet.user.screen_name, tweet.created_at, tweet.user.location, tweet.retweet_count, tweet.favorite_count])
        counter = counter + 1
    return counter

# tweet filename
global csvWriter
namefile = "tweets.csv"
dir_name = os.path.dirname(os.path.abspath(__file__))
file_dir = open(dir_name+"/"+namefile,'r', encoding='ISO-8859-1')
csvFile = open(dir_name+"/"+namefile,'a')
csvreader = csv.reader(file_dir)
csvWriter = csv.writer(csvFile)
row_cnt = sum(1 for row in file_dir)


q_words = "" # enter query words here (separate by spaces)
q_words = q_words.split()

t_lmt = tweet_limit = 500 #adjust tweet limit accordingly
limit_num = tweet_limit * len(q_words)
new_rc = row_cnt

for q in q_words:
    new_rc += gather_tweets(q, t_lmt)
print("initial rows: %s\ngathered rows: %s"%(row_cnt,new_rc-row_cnt))
csvFile.close()
