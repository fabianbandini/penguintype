import json
import requests
import os
from database import fetchScoreboard, pushScore
from api import getText
from datetime import datetime


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


def startTyping(username):
    counter = 0
    all = getText(username)
    allWords = all.split(" ")
    print(all + "\n")
    beforeTyping = datetime.now()
    typeInput = input("type: ")
    afterTyping = datetime.now()

#this logic is not correct
    for wordWritten in typeInput.split(" "):
        for wordGiven in allWords:
            if wordWritten != wordGiven:
                counter += 1

    counter += len(allWords) - counter
    finalTime = afterTyping - beforeTyping
    ratio = counter / len(allWords)
    wordsPerMinute = counter / finalTime.seconds * 60

    print("You completed the text in: " + finalTime.__str__())
    print("Your writing accuracy: " + (ratio * 100).__str__() + "%")
    print("Words per minute: " + wordsPerMinute.__str__())
    pushScore(username, finalTime.__str__())

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
