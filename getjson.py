import simplejson
import urllib2

def getjson(url):
	return simplejson.load(urllib2.urlopen(url))
