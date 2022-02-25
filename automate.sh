#!/bin/bash 

set -e 

# Run the scraper, to generate a new file:
echo "*** Run scraper ***"; echo
pushd Kijiji-Scraper
python3  main.py --skipmail
popd
echo; echo "*** Scraper successful ***"

echo; echo "*** Copy scraper output, only if new ***"
SOURCE='/home/nmacgreg/.kijiji_scraper/ads.json'
if [ -f $SOURCE ];  # does $SOURCE exist?
then
	# Calculate a current timestamp
	STAMP=`date +%Y%m%d`
	echo "Target date stamp: $STAMP"	
	echo "New input file exists $SOURCE"
	DEST="data/ads.$STAMP.json"
	if [ -f DEST ]; then
		echo "Destination file exists, not copying this file"
	else
		echo "Copying $SOURCE to $DEST"
		cp $SOURCE $DEST
	fi
fi
echo; echo "*** Copying output was successful ***"


