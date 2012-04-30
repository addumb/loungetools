import lounge

smap = lounge.ShardMap()

for (counter, shard) in enumerate(smap.shardmap):
	print " ".join([str(x + 1) for x in shard]), counter
	shard.reverse()
	print " ".join([str(x + 1) for x in shard]), counter

