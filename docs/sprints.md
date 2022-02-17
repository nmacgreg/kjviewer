# Sprints

* Small steps!

## Completed

* Datestamp the current file...
* Modify server.py to read just the new file
* Build a script to integrate runs, and datestamp individual output files
* My code - deal with multiple input data files
* Push the data into a sqlite DB
* *fully* clean up the data, before inserting it into the SQL table (used a regex)
* Add a "newserver.py" that reads data from the SQL table, & formats it for html
* Expand 'newserver.py' to print out more fields
* In newserver.py, limit the length of the title field
* With data in SQLite, how do you easily edit the data? I could *almost* do it in JSON. "sqlite3" is the answer.

## Next

* "Details" field is very messy

## Later

* Fields "year" and "kms" need to be present, but the scraped data is quite informal about these
* When considering newly scraped data, does the scraper take into account that the price might have changed? Do I need to modify the scraper, or my own code, when the price changes?  And, how do we represent this in the data model
* Track when an item was taken down 
    * that means reviewing all the items in the database, and querying Kijiji whether they're still present or not
    * ... and adding a new field to the data model, maybe two: status ['active', 'sold'] & date_sold
* git submodule, to integrate the scraper into my codebase
* Hack the scraper, and make it your own
    * Write data into a better format, probably directly into the sqlite DB
    * Capture some of the metadata
* Can you identify ads that are just getting re-posted, where the ID changes, but maybe the Details or Descriptions fields are similar?
