# Author: Finn Kearns 13-09-22
# The goal of this program is to make a API request, parse the JSON into a list
# and finally create a pie chart with the information returned.

import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import collections

# creating my variables for the API request
url = ""  # You can add the url here
api_key = "fakeAPIkey123" # add real API key here

# below is a method for setting an epoch time if required by the API request needed
dt = datetime(2015, 1, 1, 0, 0, 0)
epoch_start_date = (datetime.timestamp(dt))
dt1 = datetime.now()
epoch_end_date = datetime.timestamp(dt1)

# headers and parameters as needed can be added here
headers  = {'api-key': api_key, 'Content-Type': 'application/json'}
params = {
  'view': 'detailed',
  'start': epoch_start_date,
  'end': epoch_end_date
}

# making API request
response_json = requests.get(url, headers = headers ,json=params)

# parsing raw JSON to python object
parsed = response_json.json()

# printing out the results as a list
# here the 'results' variable might need to be changed depending on the request
for r in parsed['results']:
  print(r)

# creating pie chart of various types of incidents
# first creating a numpy array in order to count unique accidents
a = np.array([])

# adding all the incidents to the array
for r in parsed['results']:
  a = np.append(a, r['type'])

# counting the number of each type of accident
counter = collections.Counter(a)

# Finally I created two arrays, one for the values of each individual accident and then one for the corrisponding label.
# This is one method of visualising some data and adding labels. It can be adjusted depending on the request.
answer = np.array([])
newLabels = np.array([])
for pie in counter:
    answer = np.append(answer, counter[pie])
    newLabels = np.append(newLabels, pie)

# this is where I visualise and draw the pie chart
plt.pie(answer, labels= newLabels)
plt.show()
