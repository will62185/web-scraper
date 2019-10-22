# web-scraper

### Project Motivation

I have to get an oil change on my car every so often, and I always go to the same dealership. However, they don't always have the best deal, but they will match prices from competing dealerships.

So instead of searching google for other dealerships in the area, and going to each website to see their "Service Specials" let's have python scrape the websites and email back the information.

### Current Project Roadmap

* Get the web-scrapper working again
* Get email working to email the results
* Dockerize the app to live in there

### Future Project Roadmap
* TBD

### send-email.py [added 10/21/19]
Will send out an email from an email. You need to create a file `.env` and in it must contain the following:
```
EMAIL_FROM=
EMAIL_ADDRESS_PASSWORD=
EMAIL_TO=
```
Right now it's configured to send from a gmail account, you can change that by changing the server in send-email.py `server = SMTP('smtp.gmail.com', 587)`

It will format the data into tables from the pandas `to_html()` method.

Also the subject is currently `"Subject: Test"`, this can be changed in send-email.py as well. Currently only set up for `web-scrape.py`, didn't apply it to `oil-scraper.py`.