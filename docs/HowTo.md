*

Dependency on [kijiji-scraper](https://github.com/CRutkowski/Kijiji-Scraper)

## Using Kijiji-Scraper

* To cause the scraper to capture data: ```python3  main.py --skipmail```
* To view the raw data: ```cat /home/nmacgreg/.kijiji_scraper/ads.json | jq | less```

## My interpretive code: 

* To put up a web UI to view the data in ads.json: ```python server.py```
* View the web UI at: [http://127.0.0.1:5000/list](http://127.0.0.1:5000/list)
* This does a literal translation of the JSON format into an HTML table.  That's a quick first step, but we can do better
