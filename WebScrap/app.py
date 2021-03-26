# Import libraries
import csv
from datetime import datetime
from urllib.parse import quote

import bitlyshortener
import requests
from bs4 import BeautifulSoup

from my_tokens import TOKEN

# CONSTANTS
JOB_POSITION = "junior data analyst"
LOCATION = "berlin"
token = TOKEN


def short_url(url):
    """
    Take an URL as input and return a short version of it.
    :param url:
    :return: shorten URL
    """
    # Create a bitlyshortener Object
    shortener = bitlyshortener.Shortener(tokens=[token], max_cache_size=256)
    try:
        short_url = shortener._shorten_url(url)
        return short_url
    except:
        return url


def get_url(position, location):
    """
    Generate a url from position and location
    :param position:
    :param location:
    :return:
    """
    template = 'https://de.indeed.com/jobs?q={}&l={}'
    url = template.format(quote(position), quote(location))
    return url


def get_record(card):
    """
    :param card: A card represents a job description. From each card we scrape the information we need
    :return: a record, is a tuple with all extracted information
    """
    a_tag = card.h2.a
    job_title = a_tag.get("title")
    job_url = "https://de.indeed.com/" + a_tag.get("href")
    company = card.find('span', 'company').text.strip()
    job_location = card.find('div', 'recJobLoc').get('data-rc-loc')
    job_summary = card.find('div', 'summary').text.strip()
    post_date = card.find('span', 'date').text.strip()
    try:
        # In case salary is present
        job_salary = card.find('span', 'salaryText').text.strip()
    except AttributeError:
        job_salary = ''

    record = (job_title,
              company,
              job_location,
              job_summary,
              job_salary,
              post_date,
              short_url(job_url))
    return record


# Just the date from today
today = datetime.today().strftime('%Y-%m-%d')
# Set the url variable passing the job title and location
url = get_url(JOB_POSITION, LOCATION)
# initialize an empty list to store all the records
records = []

print("Start scraping...")
while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    cards = soup.find_all('div', 'jobsearch-SerpJobCard')
    for each in cards:
        record = get_record(each)
        records.append(record)
    try:
        url = "https://de.indeed.com" + soup.find('a', {"aria-label": 'Weiter'}).get("href")
    except AttributeError:
        break

print("Creating file...")
with open('{}_{}_{}.csv'.format(JOB_POSITION.replace(' ', '_'), LOCATION, today), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['JobTitle', 'Company', 'Location', 'Summary', 'Salary', 'DateOfPosting', 'URL'])
    writer.writerows(records)
print("Finished")
