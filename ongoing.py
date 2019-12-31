#Import Dependencies
import requests,ast, json
from requests_oauthlib import OAuth1
from datetime import datetime,date,time

#URL - response
url = "https://clist.by/api/v1/json/contest/" + YOUR_API_KEY
payload = "{}"
response = requests.request("GET",url,data=payload)
a = response.text
parsed_json = json.loads(a)
total = parsed_json['meta']['total_count']
total = str(total)
j_count = int(total[:2])
today = datetime.today().day
toyear = datetime.today().year
tomonth = datetime.today().month
count = 0

for j in range(j_count+1):
  k = str(j*1000)
  url = "https://clist.by/api/v1/json/contest/?limit="+total+"&offset="+k+"YOUR_API_KEY"
  payload = "{}"
  response = requests.request("GET",url,data=payload)
  print("OFFSET:",k,"\n","RESPONSE:",response,"\n\n")
  a = response.text
  parsed_json = json.loads(a)
  if j == j_count:
    print("INSIDE END")
    for i in range(int(total) - int(k)):
      endyear = int(parsed_json['objects'][i]['end'][:4])
      endmonth = int(parsed_json['objects'][i]['end'][5:7])
      endday = int(parsed_json['objects'][i]['end'][8:10])
      startyear = int(parsed_json['objects'][i]['start'][:4])
      startmonth = int(parsed_json['objects'][i]['start'][5:7])
      startday = int(parsed_json['objects'][i]['start'][8:10])
      if startyear < toyear and endyear > toyear:  
        print("Event:",i,"=",parsed_json['objects'][i])
        count+=1
      elif startyear == toyear and endyear > toyear:
        if startmonth < tomonth:
          print("Event:",i,"=",parsed_json['objects'][i])
          count+=1
        elif startmonth == tomonth:
          if startday <= today:
            print("Event:",i,"=",parsed_json['objects'][i])
            count+=1
      elif startyear == toyear and endyear == toyear:
        if startmonth < tomonth and endmonth > tomonth:
          print("Event:",i,"=",parsed_json['objects'][i])
          count+=1
        elif startmonth < tomonth and endmonth == tomonth:
          if today <= endday:
            print("Event:",i,"=",parsed_json['objects'][i])
        elif startmonth == tomonth and endmonth == tomonth:
          if startday <= today and endday >= today:
            print("Event:",i,"=",parsed_json['objects'][i])
            count+=1
        elif startmonth == tomonth and endmonth > tomonth:
          print("Event:",i,"=",parsed_json['objects'][i])
          count+=1
      elif startyear < toyear and endyear == toyear:
        if endmonth == tomonth:
          if endday >= today:
            print("Event:",i,"=",parsed_json['objects'][i])
            count+=1
        elif endmonth > tomonth:
          print("Event:",i,"=",parsed_json['objects'][i])
          count+=1
  else:
    for i in range(1000):
      endyear = int(parsed_json['objects'][i]['end'][:4])
      endmonth = int(parsed_json['objects'][i]['end'][5:7])
      endday = int(parsed_json['objects'][i]['end'][8:10])
      startyear = int(parsed_json['objects'][i]['start'][:4])
      startmonth = int(parsed_json['objects'][i]['start'][5:7])
      startday = int(parsed_json['objects'][i]['start'][8:10])
      if startyear < toyear and endyear > toyear:  
        print("Event:",i,"=",parsed_json['objects'][i])
        count+=1
      elif startyear == toyear and endyear > toyear:
        if startmonth < tomonth:
          print("Event:",i,"=",parsed_json['objects'][i])
          count+=1
        elif startmonth == tomonth:
          if startday <= today:
            print("Event:",i,"=",parsed_json['objects'][i])
            count+=1
      elif startyear == toyear and endyear == toyear:
        if startmonth < tomonth and endmonth > tomonth:
          print("Event:",i,"=",parsed_json['objects'][i])
          count+=1
        elif startmonth < tomonth and endmonth == tomonth:
          if today <= endday:
            print("Event:",i,"=",parsed_json['objects'][i])
        elif startmonth == tomonth and endmonth == tomonth:
          if startday <= today and endday >= today:
            print("Event:",i,"=",parsed_json['objects'][i])
            count+=1
        elif startmonth == tomonth and endmonth > tomonth:
          print("Event:",i,"=",parsed_json['objects'][i])
          count+=1
      elif startyear < toyear and endyear == toyear:
        if endmonth == tomonth:
          if endday >= today:
            print("Event:",i,"=",parsed_json['objects'][i])
            count+=1
        elif endmonth > tomonth:
          print("Event:",i,"=",parsed_json['objects'][i])
          count+=1
print(count)
