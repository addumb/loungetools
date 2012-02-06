#!/bin/bash
curl http://$1:5984/_active_tasks | sed 's/},{/},\n{/g'
