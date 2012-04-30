#!/usr/bin/python
import httplib2
import optparse
import sys
import urllib

from getjson import getjson

def docs(url):
	return int(getjson(url)['doc_count'])

def tasks(host_uri):
	return list(getjson(host_uri + "/_active_tasks"))

def check_replication(task, local_host):
	"""Format is like this:
	{"type":"Replication","task":"b81423: http://bfp5.dev.meebo.com:5984/adsuploader11/ -> adsuploader11","status":"W Processed source update #535","pid":"<0.2178.6425>"}
	"""
	junk, remote, morejunk, local_db = task['task'].split(' ')
	local_docs = docs("%s/%s" % (local_host, local_db))
	remote_docs = docs(remote)
	return local_db, local_docs, remote_docs

def main(host_uri, bad_count):
	for task in tasks(host_uri):
		if 'type' in task.keys() and task['type'] == 'Replication':
			db, local, remote = check_replication(task, host_uri)
			if abs(local - remote) >= bad_count:
				print "%s local has %s, remote has %s" % (db, local, remote)


if __name__ == '__main__':
	parser = optparse.OptionParser()
	parser.set_defaults(count=1)
	parser.add_option("-p", "--primary", help="URI to primary couchdb socket, e.g. http://localhost:5984")
	parser.add_option("-c", "--count", help="A number for document count discrepancies to become a bad thing (defaults to 1)", type="int")

	options, args = parser.parse_args()
	main(options.primary, options.count)
