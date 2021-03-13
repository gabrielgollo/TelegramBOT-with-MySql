import requests
import json

class Covid19Infos:
	def __init__(self):
		try:
			self.getApi = requests.get("https://api.covid19api.com/summary")
			self.jsonInfos = self.getApi.json()
			self.problem = False
			self.listbyAllCountries = self.__getApiInfos()
			#print(self.jsonInfos)

		except json.decoder.JSONDecodeError:
			print("there is and error")
			self.problem = True

	def getCountry(self, country):
		try:
			return self.listbyAllCountries[country]
		except KeyError:
			return {"country":"Not Found"}

	def __getApiInfos(self):
		if self.problem:
			print("There is a problem into COVID19API!")
			return {}

		loadJson = self.jsonInfos
		#print(loadJson["Countries"])
		loadJson = self.__getDictKeysbyCountries(loadJson["Countries"])

		try:
			return loadJson
		except KeyError:
			return {"country":"Not Found"}

	def __getDictKeysbyCountries(self, jsonFile):
		theDict = {}
		for i in jsonFile:
			theDict[i["Country"]] = i
		return theDict

	def getStatus(self):
		if self.problem:  # IF THERE IS A PROBLEM
			return False
		else:
			return True



#x = Covid19Infos()
#print(x.getCountry("Brazil"))