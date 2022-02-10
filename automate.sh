#!/bin/bash 

set -e 

SOURCE='/home/nmacgreg/.kijiji_scraper/ads.json'

# Calculate a current timestamp
STAMP=`date +%Y%m%d`
echo "Target date stamp: $STAMP"	

if [ -f $SOURCE ];  # does $SOURCE exist?
then
	echo "New input file exists $SOURCE"
	DEST="data/ads.$STAMP.json"
	if [ -f DEST ]; then
		echo "Destination file exists, not copying this file"
	else
		echo "Copying $SOURCE to $DEST"
		cp $SOURCE $DEST
	fi


fi
