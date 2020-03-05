# script which gathers tweets about certain texts.
# Ogs Ablazo
import csv, tweepy
from lib.ogspeace import OgsPeace
from lib.basics import print_stdout
# tweet filename
namefile = "tweets.csv"
dir_name = os.path.dirname(os.path.abspath(__file__))
#dir_name = "/home/pi/dataset_dump"
#dir_name = os.path.dirname(os.path.realpath(__file__))
file_dir = open(dir_name+"/"+namefile,'r', encoding='ISO-8859-1')
csvFile = open(dir_name+"/"+namefile,'a')
csvreader = csv.reader(file_dir)
csvWriter = csv.writer(csvFile)
row_cnt = sum(1 for row in file_dir)
class Conn:
    def __init__(self, *args):
        
api = OgsPeace().ogs_gath03()

def gather_tweets(query_word,twt_lmt):
    counter = 0
    for tweet in list(tweepy.Cursor(api.search, q=query_word).items(twt_lmt)):
        csvWriter.writerow([tweet.text, tweet.user.screen_name, tweet.created_at, tweet.user.location, tweet.retweet_count, tweet.favorite_count])
        counter = counter + 1
    return counter

q_words = ['Duterte', 'President Duterte', 'digong']
limit_num = 1500
t_lmt = limit_num // len(q_words)
new_rc = row_cnt
for q in q_words:
    new_rc += gather_tweets(q, t_lmt)
print_stdout("initial rows: %s\ngathered rows: %s"%(row_cnt,new_rc-row_cnt))
csvFile.close()
