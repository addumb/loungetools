import lounge

smap = lounge.ShardMap()

print "digraph Lounge {"
for (counter, shard) in enumerate(smap.shardmap):
	print " -> ".join([str(x + 1) for x in shard]), '[label=%s];' % counter
	shard.reverse()
	print " -> ".join([str(x + 1) for x in shard]), '[label=%s];' % counter

print "}"
