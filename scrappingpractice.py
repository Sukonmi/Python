import requests

import re

import numpy as np

import pandas as pd

from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

page = requests.get(url)

parsed_page = BeautifulSoup(page.content, 'html.parser')

all_names = parsed_page.find_all("div", class_ = "column is-half")

all_titles = []
all_subtitles = []
all_locations = []
all_dates = []

for names in all_names:
    title = names.find("h2", class_ = "title is-5").text
    # append each title to the list
    all_titles.append(title)

    subtitle = names.find("h3", class_ = "subtitle is-6 company").text
    # append each subtitles to the list
    all_subtitles.append(subtitle)

    location = names.find("p", class_ = "location").text
    # append each location to the list
    all_locations.append(location)

    date = names.find("p", class_ = "is-small has-text-grey").text
    # append each date to the list
    all_dates.append(date)

# Create the dataframe
dataset = {"JobTitles": all_titles, "JobSubTitles": all_subtitles,
           "JobLocation": all_locations, "JobDate": all_dates}

# Convert to Dataframe
df = pd.DataFrame(dataset)

df.to_csv("jobListing.csv", index = False)
print("Done converting.....")