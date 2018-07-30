import tweepy
import re
from datetime import *
import time
import sys
import json
import urllib
import urlparse
import datetime
import threading
import time
ckey="p8wcVKxVvoA3kS54qdMssYmgQ"
csecret="Ys7jrwPlRH2FQeMVi3Tu4DQQJXWfvEU9el8Z0O0GerT4RfnC6N"
atoken="2161947279-J5yvfzpnhDQcRV1EC956yRCGGTNxeufI1bha9dw"
asecret="r6iXNyXEVKtGe8qlu3nrtQHtEibv0UDfAncxNkMQe5RKk"
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
list_of_extra_words = ['the','a', 'i', ,'yes', 'no', 'very', 'after', 'to', 'my', 'in', 'an','as','if', 'of', 'is','are','they', 'this', 'that', 'u', 'you', 'were','was','has','have', 'or','and','by','because', '_vulpix', '__', 'when','which','what','why','how', 'so', 'me', 'for', 'on', 'it', 'he', 'she', 'with', 'but', 'at', 'our', 'from', 'your', 'be', 'been', 'being', 'all', 'not', 'dont', 'do', 'does', 'about', 'we', 'us']
cnt = 0

def unshorten_url(url):
    fp = urllib.urlopen(url)
    domain_name = urlparse.urlparse(str(fp.geturl()))
    domain_name = domain_name.netloc
    domains_count[domain_name] = domains_count.get(domain_name,0)+1 

def clean_tweet(tweet_text):
    text = ' '.join(re.sub("(@[A-Za-z0-9_]+)|([^0-9A-Za-z_ \t]) | (\w +:\ / \ / \S + _) | https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", " ", tweet_text).split())
    return text
def countWords(text):
    words = text.split()
    for word in words:
        if word.lower() not in list_of_extra_words:
            words_count[word.lower()] = words_count.get(word.lower(),0)+1 


def showReport1():
    time.sleep(60)
    showReport()
def showReport():
  threading.Timer(60.0, showReport).start()
  if len(users_count) != 0:
    print "REPORT 1"
    print ""
    for i,j in users_count.items():
        print str(i.encode('utf-8')) + " tweeted " + str(j) + " tweets"
    print "----------------------------------------------"
    print "REPORT 2"
    print ""
    print "List Of Unique Domains"
    keys = sorted(domains_count, key=domains_count.__getitem__, reverse = True)
    for i in range(len(domains_count)):
        x = keys[i]
        print str(x.encode('utf-8')) + " appeared " + str(domains_count[x]) + " times"
    print "----------------------------------------------"
    print "REPORT 3"
    print ""
    print "List Of top 10 unique words"
    keys = sorted(words_count, key=words_count.__getitem__, reverse = True)
    if len(keys) >= 10:
        for i in range(10):
            x = keys[i]
            print str(keys[i].encode('utf-8'))+" "+  str(words_count[x])+ " times"
    print ""
    print "----------------------------------------------"
    print "*************End Of Report********************"
    print ""
    print ""






keyword = raw_input("enter a keyword:  ")
print ""
i = 0
cnt = 0
users_count = dict()
domains_count = dict()
words_count = dict()
showReport()
start_date = datetime.datetime.now() - timedelta(days=1)
start_date = start_date.strftime('%Y-%m-%d')
end_date = datetime.datetime.now() 
end_date = end_date.strftime('%Y-%m-%d')
for tweet in tweepy.Cursor(api.search,q = keyword + ' -filter:retweets', result_type='recent', monitor_rate_limit=True, wait_on_rate_limit=True, lang="en").items():
    for i in tweet.entities['urls']:
        unshorten_url(i['expanded_url'])
    countWords(clean_tweet(tweet.text))
    users_count[tweet.author._json['name']] = users_count.get(tweet.author._json['name'],0)+1             


