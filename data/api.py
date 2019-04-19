import requests
import json
import datetime

def getAllData():
      req_2019 = requests.get("https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=234400034_temperature-quotidienne-regionale-2016-2017&rows=365&sort=-date&facet=date&facet=region&refine.date=2019")
      req_2018 = requests.get("https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=234400034_temperature-quotidienne-regionale-2016-2017&rows=365&sort=-date&facet=date&facet=region&refine.date=2018")
      req_2017 = requests.get("https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=234400034_temperature-quotidienne-regionale-2016-2017&rows=365&sort=-date&facet=date&facet=region&refine.date=2017")
      req_2016 = requests.get("https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=234400034_temperature-quotidienne-regionale-2016-2017&rows=365&sort=-date&facet=date&facet=region&refine.date=2016")

      rec_2019 = json.loads(req_2019.content)["records"]
      rec_2018 = json.loads(req_2018.content)["records"]
      rec_2017 = json.loads(req_2017.content)["records"]
      rec_2016 = json.loads(req_2016.content)["records"]

      allTemp = rec_2016 + rec_2017 + rec_2018 + rec_2019

      return processJson(allTemp)

def processJson(json):
      processedJson = []
      for data in json:
            tmpJson = {}
            tmpJson["date"] = data["fields"]["date"]
            tmpJson["dayInYear"] = dayInYearFromString(data["fields"]["date"])
            tmpJson["tmin"] = data["fields"]["tmin"]
            tmpJson["tmoy"] = data["fields"]["tmoy"]
            tmpJson["tmax"] = data["fields"]["tmax"]
            processedJson.append(tmpJson)
      return processedJson

def dayInYearFromString(str):
      monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
      date = datetime.datetime.strptime(str, "%Y-%m-%d")

      value = 0

      if(date.date().day == 29 & date.date().month == 2):
            value+=1

      for x in range(date.date().month-1):
            value += monthDays[x]
            
      value += date.date().day

      return value