import json
import requests
import os
from database import loadLang
from random import randrange

textLength = 10


def loadApiRoute(lang):
    with open(os.path.join(os.path.dirname(__file__), '.', 'data', 'constants.json')) as settingsFile:
        return json.load(settingsFile)["apiRoutes"][lang]


def loadFromApi(url):
    return requests.get(url).json()


def fetchData(username):
    open(os.path.join(os.path.dirname(__file__), 'data', 'texts.txt'), 'w').close()
    data = loadFromApi(loadApiRoute(loadLang(username)))
    return data


def generateText(username):
    data = fetchData(username)
    text = ""
    counter = 0

    while counter < textLength:
        word = data["words"][randrange(len(data["words"]) - 1)]
        text += (word + " ")
        counter += 1

    saveText(text)
    return text


def saveText(text):
    file = open(os.path.join(os.path.dirname(__file__), 'data', 'texts.txt'), "a")
    file.write(text + "\n")
    file.close()


def getText(username):
    text = generateText(username)
    if text == "":
        return "Error occurred api.py line:42"
    return text
