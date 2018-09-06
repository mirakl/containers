#!/bin/bash

trap 'exit 0' KILL INT

view-cache() {
  grep dentry /proc/slabinfo | awk '{print "Dentry cache - Active: " $2 " Total: " $3 " Size: " $3*$4 " bytes" }'
}

fill-cache() {
  R=$RANDOM
  for i in $(seq 1 1000); do
    stat "/tmp/$R$i" >/dev/null 2>&1
  done
}

while true; do
  view-cache
  fill-cache
done
