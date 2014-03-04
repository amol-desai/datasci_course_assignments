import sys
import json
import operator

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    hashtags = dict()
    with open(sys.argv[1],'rb') as tweet_file:
        for line in tweet_file:
            tweet = json.loads(line)
            tweet = tweet.get('entities',None)
            if tweet != None:
                tags = tweet.get('hashtags')
            else:
                tags = []
            if len(tags) > 0:
                for tag in tags:
                    ht = tag.get('text').encode('utf-8')
                    if ht not in hashtags.keys():
                        hashtags[ht] = 1
                    else:
                        hashtags[ht] += 1
    sorted_hashtags = sorted(hashtags.iteritems(),key=operator.itemgetter(1))[::-1]
    for i in range(10):
        print sorted_hashtags[i][0]+" ",float(sorted_hashtags[i][1])

        
if __name__ == '__main__':
    main()

