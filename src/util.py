import json
import requests
import os
from database import fetchScoreboard, pushScore
from api import getText
from datetime import datetime


# loads constants from constants.json
def loadConstants():
    with open(os.path.join(os.path.dirname(__file__), '.', 'data', 'strings.json')) as settingsFile:
        return json.load(settingsFile)


# checks if a language exists (hardcoded on client)
def checkIfLangExists(lang):
    langs = []
    for _lang in loadConstants()["languages"]:
        langs.append(_lang)

    if langs.__contains__(lang):
        print("Your language was changed.")
        return True
    else:
        print("Your language was not changed please try again.")
        return False


# logic for handling the type test
def startTyping(username):
    counter = 0
    all = getText(username)
    allWords = all.split(" ")
    del allWords[-1]
    print(all + "\n")
    beforeTyping = datetime.now()
    typeInput = input("type: ")
    afterTyping = datetime.now()

    for wordWritten in typeInput.split(" "):
        for wordGiven in allWords:
            if wordWritten == wordGiven:
                counter += 1

    finalTime = afterTyping - beforeTyping
    ratio = round(counter / len(typeInput.split(" ")), 2)
    correctWordsPerMinute = round(counter / finalTime.seconds * 60, 2)

    print("You completed the text in: " + finalTime.__str__())
    print("Your writing accuracy: " + (ratio * 100).__str__() + "%")
    print("Correct words per minute: " + correctWordsPerMinute.__str__())
    pushScore(username, correctWordsPerMinute)


# loads languages from constants.json
def loadLanguages():
    languages = []

    for _language in loadConstants()["languages"]:
        languages.append(_language)

    return languages


# loads api constants from constants.json
def loadApiRoute(lang):
    with open(os.path.join(os.path.dirname(__file__), '.', 'data', 'constants.json')) as settingsFile:
        return json.load(settingsFile)["apiRoutes"][lang]


# calls functions from api.py
def loadFromApi(url):
    return requests.get(url).json()


# loads texts from strings.json
def loadText(text):
    with open(os.path.join(os.path.dirname(__file__), '.', 'data', 'constants.json')) as settingsFile:
        return json.load(settingsFile)["text"][text]


# calls function from database.py
def getHighscore(username):
    return fetchScoreboard(username)
