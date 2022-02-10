*

Dependency on [kijiji-scraper](https://github.com/CRutkowski/Kijiji-Scraper)

## Using Kijiji-Scraper

* To cause the scraper to capture data: ```python3  main.py --skipmail```
* To view the raw data: ```cat /home/nmacgreg/.kijiji_scraper/ads.json | jq | less```

## My interpretive code: 

* To put up a web UI to view the data in ads.json: ```python server.py```
* This does a literal translation of the JSON format into an HTML table.  That's a quick first step, but we can do better

## Next steps

* Small steps!
* Build a script to integrate runs
* Datecodes on ads.json files
* My code - deal with multiple files
* Hack the scraper, and make it your own
    * Write data into a better format, probably into a sqlite
    * Capture some of the metadata

