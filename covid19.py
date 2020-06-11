# STEP - 1
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
#import matplotlib.pyplot as plt
import json

#print("Executing")

# STEP - 2
extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS = ['S No', 'State/UT', 'Active Cases', 'Cured/Discharged', 'Deaths', 'Total Confirmed cases']

response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents(soup.tr.find_all('th'))

stats = []
all_rows = soup.find_all('tr')
count = 1

for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    #print(stat)
    #print(len(stat))
    if stat:
        #print(len(stat))
        if len(stat) == 5:
            # last row
            stat = ['', *stat]
            stats.append(stat)
            count += 1
        elif len(stat) == 4:
            var_stat = []
            var_stat.append('')
            for i in stat:
                var_stat.append(i)
            stats.append(var_stat)

        elif len(stat) == 6:
            stats.append(stat)

stats[-1][1] = "Total Cases"

#stats.remove(stats[-1])

# STEP 3
'''
objects = []
for row in stats:
    objects.append(row[1])

y_pos = np.arange(len(objects))

performance = []
for row in stats:
    performance.append(int(row[0]) + int(row[2]))
'''

#print(stats)
table = tabulate(stats, headers=SHORT_HEADERS)
print(table)
#print(json.dumps(stats))
# Disable output buffering
# print(json.dumps(mydict), flush=True)

# STEP 4
'''
plt.barh(y_pos, performance, align='center', alpha=0.5,
                 color=(234/256.0, 128/256.0, 252/256.0),
                 edgecolor=(106/256.0, 27/256.0, 154/256.0))

plt.yticks(y_pos, objects)
plt.xlim(1,2000)
plt.xlabel('Number of Cases')
plt.ylabel('State')
plt.title('Corona Virus Cases')
plt.show()
'''
