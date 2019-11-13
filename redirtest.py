import requests
import csv

base = "https://www.obos.no"

links = []
responses = {"400":[], "200": [], "other": []} 

with open("redir.csv") as f:
        lines = csv.reader(f)
        for line in lines:
            links.append(line)

for link in links[1:]:
    link1= base+link[0]
    a = requests.get(link1)
    if a.status_code == 200:
        responses["200"].append([link1, a.url, a.status_code])
    elif a.status_code == 404:
        responses["400"].append([link1, a.url, a.status_code])
    else:
        responses["other"].append([link1, a.url, a.status_code])


