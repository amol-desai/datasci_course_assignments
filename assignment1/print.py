import urllib
import json

def printResults(query,pages):

    for pagenum in range(1,pages+1):
        response = urllib.urlopen("http://search.twitter.com/search.json?q="+query+"&page="+str(pagenum))
        print "*********NEXT PAGE**********"
        for result in json.load(response)['results']:
            print result['text']
