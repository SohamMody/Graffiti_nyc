#!/usr/bin/env python3 -V

## python xxx.py 1000000 2019-03-01 2019-04-01 Mar2019.csv Mar2019_clean.csv
# not using Sodapy 
# try to output print  the total row 
import csv
import sys
import json
import requests
import pandas as pd

inputLimit = sys.argv[1]
from_ = sys.argv[2]
to_ = sys.argv[3]
file = sys.argv[4]
outputfile = sys.argv[5]

url ="https://data.cityofnewyork.us/resource/fhrw-4uyv.json"
query = "?$where=created_date BETWEEN '"+from_+"' AND '"+to_+"'"+"&$limit="+str(inputLimit)

link = url+query
jsonData = requests.get(link)
results = json.loads(jsonData.text)

keys=set()
n = 0
for d in results:
    n+=1
    keys.update(d.keys())
    print(n)
    
with open(file,'w',encoding='utf-8') as fi:
    output=csv.DictWriter(fi,fieldnames=keys)
    output.writeheader()
    output.writerows(results)
    
data_311 = pd.read_csv(file,usecols=['complaint_type','unique_key','latitude','longitude','created_date'])

# df.joined = pd.to_datetime(df.joined, format='%m/%d/%y')
data_311_graffiti = data_311[data_311.complaint_type=='Graffiti']
print(data_311.shape,data_311_graffiti.shape)

data_311_graffiti.drop('complaint_type',axis=1,inplace=True)
data_311_graffiti.dropna(inplace=True)
data_311_graffiti['created_date'] = pd.to_datetime(data_311_graffiti.created_date, format='%Y-%m-%d')
data_311_graffiti.to_csv(outputfile,index=False)
