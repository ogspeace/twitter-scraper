# twitter-scraper
simple script to gather tweets from twitter

## prerequisites
1. approved twitter dev access @ dev.twitter.com and,
2. approved twitter app API credentials @ dev.twitter.com
3. preferably a linux (*debian variant) machine.
4. python3

## installation 
1. install pip3: ```apt-get install python3-pip -y```
2. install all package(s) found in requirements file: ```pip3 install -r requirements.txt```

## usage
1. identify what topics or text query will be. (i.e. ```'PewDiePie youtube memes'```)
2. place all keywords (separated by spaces) on the ```q_words``` value.
3. edit the ```limit_num``` value as needed (i limit my scraped tweets to 500 tweets per session)
