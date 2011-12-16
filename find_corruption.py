#TODO: change doc name to avoid conflicts
#TODO: decide on httplib or urllib
import lounge
import httplib2
import urllib
import simplejson

h = httplib2.Http(".cache")

smap = lounge.ShardMap()

def probe_node(node):
	try:
		resp, dbs =  h.request(node + '_all_dbs')
	except:
		#Just keep movin', we put localhost:666 in for dead nodes :-\
		return

	for db in simplejson.loads(dbs):
		if db[0] != "_":
			test_write(node + urllib.quote(db,''))

def test_write(db):
	doc = "%s/derptest" % db
	try:
		resp, write = h.request(doc, "PUT", body="{}")
		rev = simplejson.loads(write)['rev']
		resp, baleeted = h.request(doc + ("?rev=%s" % rev), "DELETE")
	except:
		print "Failed to write to %s" % db

def main():
	for n in smap.nodes():
		probe_node(n)

if __name__ == "__main__":
	main()
