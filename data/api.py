import requests
import json

def getAllData():
      req_2019 = requests.get("https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=234400034_temperature-quotidienne-regionale-2016-2017&rows=365&sort=-date&facet=date&facet=region&refine.date=2019")
      req_2018 = requests.get("https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=234400034_temperature-quotidienne-regionale-2016-2017&rows=365&sort=-date&facet=date&facet=region&refine.date=2018")
      req_2017 = requests.get("https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=234400034_temperature-quotidienne-regionale-2016-2017&rows=365&sort=-date&facet=date&facet=region&refine.date=2017")
      req_2016 = requests.get("https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=234400034_temperature-quotidienne-regionale-2016-2017&rows=365&sort=-date&facet=date&facet=region&refine.date=2016")

      rec_2019 = json.loads(req_2019.content)["records"]
      rec_2018 = json.loads(req_2018.content)["records"]
      rec_2017 = json.loads(req_2017.content)["records"]
      rec_2016 = json.loads(req_2016.content)["records"]

      allTemp = rec_2019 + rec_2018 + rec_2017 + rec_2016

      return allTemp
