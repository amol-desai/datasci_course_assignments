import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    scores = dict()
    with open(sys.argv[1],'rb') as sent_file:
        for line in sent_file:
            term,score = line.split("\t")
            scores[term] = int(score)

    state_score = dict()
    with open(sys.argv[2],'rb') as tweet_file:
        for line in tweet_file:
            tweet = json.loads(line)
            if tweet.get('place',None) != None:
                if tweet.get('place').get('country_code') == "US":
                    tweet_text = tweet.get('text',None)
                    if tweet_text != None:
                        tweet_text = tweet_text.encode('utf-8')
                        terms = tweet_text.split() 
                    else:
                        terms = []
                    sentiment_score = 0
                    for term in terms:
                        sentiment_score += float(scores.get(term,0))

                    if tweet.get('user').get('location').encode('utf-8')[-4:-3] == ',':
                        state = tweet.get('user').get('location').encode('utf-8')[-2::]
                    if tweet.get('place').get('full_name').encode('utf-8')[-4:-3] == ',':
                        state = tweet.get('place').get('full_name').encode('utf-8')[-2::]

                    if state in state_score:
                        state_score[state] += sentiment_score
                    else:
                        state_score[state] = sentiment_score

    print max(state_score, key=state_score.get)
        
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()

