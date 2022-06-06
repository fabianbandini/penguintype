import json
import requests


def loadSettings():
    with open('../userdata/settings.json') as settingsFile:
        return json.load(settingsFile)


def loadApiRoute(lang):
    with open('./data/constants.json') as settingsFile:
        return json.load(settingsFile)["apiRoutes"][lang]


def loadFromApi(url):
    return requests.get(url).json()
