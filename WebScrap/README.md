# Job Searchers

A python project that scrapes the german [Indeed](https://de.indeed.com/?r=us) job portal. Creates a
`.csv` file with all the findings.

## How to use the app

### Dependencies

First there are some libraries needed to install in order to run the code without problems. The code can be modified to
run without these libraries but this is up to the developer.

- `pip install bitlyshortener`

The app uses the bitly URL shortener API to shorten the link driving to each job advertisement. To use the API you need
to make an account and acquire a token. Put the token in a python file with the name `my_token.py`

- `pip install beautifulsoup4`

The games Beautifulsoup library to parse and extract all the information needed from the site.

### Add CONSTANTS

After install the dependencies in the `app.py` file you have to edit the constants. Add your preferred job title and
location.

### Run the code

To run the code

`cd /directory-file/`

`python app.py`

After code is done executing a `.csv` file will appear. 