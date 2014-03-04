import sys
import json

def main():
    term_count = dict()
    total_count = 0
    with open(sys.argv[1],'rb') as livestream:
        for line in livestream:
            tweet = json.loads(line)
            tweet = tweet.get('text',None)
            if tweet != None:
                tweet = tweet.encode('utf-8')
                terms = tweet.split()
            else:
                terms = []
            for term in terms:
                if term not in term_count.keys():
                    term_count[term] = 1
                else:
                    term_count[term] += 1
            total_count += len(terms)
    for term in term_count:
        print term+" ",float(term_count[term]/total_count)


if __name__ == '__main__':
    main()
