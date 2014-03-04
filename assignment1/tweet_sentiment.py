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

    with open(sys.argv[2],'rb') as tweet_file:
        for line in tweet_file:
            tweet = json.loads(line)
            tweet = tweet.get('text',None)
            if tweet != None:
                tweet = tweet.encode('utf-8')
                terms = tweet.split()
            else:
                terms = []
            sentiment_score = 0
            for term in terms:
                sentiment_score += float(scores.get(term,0))
            print float(sentiment_score)
        
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()

