import requests
import csv
import pandas as pd

base = "https://www.obos.no"

links = []
responses = {"400":[], "200": [], "other": []} 

with open("master.csv") as f:
        lines = csv.reader(f)
        for line in lines:
            if len(line)>0:
                if "ï»¿" in line[0] or "gammel URL" in line[0]:
                    pass
                else:
                    links.append(line[0].split("|"))
            else:
                pass

for link in links:
    link1= base+link[0]
    a = requests.get(link1)
    if a.status_code == 200:
        responses["200"].append([link1, a.url, a.status_code])
    elif a.status_code == 404:
        responses["400"].append([link1, a.url, a.status_code])
    else:
        responses["other"].append([link1, a.url, a.status_code])


