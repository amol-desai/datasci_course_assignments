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
            new_terms = []
            for term in terms:
                score = float(scores.get(term,0))
                if score == 0:
                    new_terms.append(term)
                else:
                    sentiment_score += score
            for term in new_terms:
                print term+" ",float((sentiment_score+1)/len(terms))
        
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
