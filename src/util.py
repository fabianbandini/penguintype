import json
import requests
import os
from database import fetchScoreboard

def loadSettings():
    with open(os.path.join(os.path.dirname(__file__), '.', 'data', 'strings.json')) as settingsFile:
        return json.load(settingsFile)


def checkIfLangExists(lang):
    langs = []
    for _lang in loadSettings()["languages"]:
        langs.append(_lang)

    if langs.__contains__(lang):
        return True
    else:
        return False


def loadLanguages():
    languages = []

    for _language in loadSettings()["languages"]:
        languages.append(_language)

    return languages

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
