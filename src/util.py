import json
import requests
import os
from database import fetchScoreboard


def loadSettings():
    with open(os.path.join(os.path.dirname(__file__), '..', 'userdata', 'settings.json')) as settingsFile:
        return json.load(settingsFile)


def loadApiRoute(lang):
    with open(os.path.join(os.path.dirname(__file__), '.', 'data', 'constants.json')) as settingsFile:
        return json.load(settingsFile)["apiRoutes"][lang]


def loadFromApi(url):
    return requests.get(url).json()


def loadText(text):
    with open(os.path.join(os.path.dirname(__file__), '.', 'data', 'constants.json')) as settingsFile:
        return json.load(settingsFile)["text"][text]


def getHighscore(username):
    return fetchScoreboard(username)
